from __future__ import annotations

import argparse
import asyncio
import sys

from .config import Settings
from .pipeline import run_pipeline


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="stagezero", description="Customer-discovery agent for pre-PMF founders")
    sub = parser.add_subparsers(dest="command", required=True)

    run = sub.add_parser("run", help="run the discovery agent on an idea")
    run.add_argument("--idea", required=True, help="one-sentence startup idea")
    run.add_argument("--demo", action="store_true", help="force offline mode with fixture data (no keys needed)")
    run.add_argument("--resume", metavar="RUN_ID", help="resume a previous run, skipping completed stages")
    run.add_argument("--out", default="runs", help="runs directory (default: runs)")
    run.add_argument("--fail-at", metavar="STAGE", help="inject a failure into STAGE once to demo recovery")
    run.add_argument("--fail-times", type=int, default=1, help="how many times to fail before recovering")

    show = sub.add_parser("show", help="print a previous run's kit")
    show.add_argument("run_id")
    show.add_argument("--out", default="runs")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "run":
        return asyncio.run(_cmd_run(args))
    if args.command == "show":
        return _cmd_show(args)
    return 1


async def _cmd_run(args) -> int:
    settings = Settings.from_env(runs_dir=args.out)
    if args.fail_at:
        settings = Settings(**{**settings.__dict__, "fail_stage": args.fail_at, "fail_times": args.fail_times})
    kit = await run_pipeline(settings, args.idea, resume=args.resume, demo=True if args.demo else None)
    print(f"run {kit.run_id} complete -> {args.out}/{kit.run_id}/VALIDATION_KIT.md")
    print(f"decision: {kit.decision}")
    for seg in sorted(kit.segments, key=lambda s: -s.priority_score):
        print(f"  segment {seg.name}: score={seg.priority_score} companies={seg.company_count}")
    if kit.recovered_from_failure:
        print("  (recovered from a tool failure during this run)")
    return 0


def _cmd_show(args) -> int:
    import json
    from pathlib import Path

    path = Path(args.out) / args.run_id / "validation_kit.json"
    if not path.exists():
        print(f"no run at {path}", file=sys.stderr)
        return 1
    kit = json.loads(path.read_text())
    print(f"idea: {kit['idea']['idea_text']}")
    print(f"decision: {kit['decision']}")
    for seg in sorted(kit["segments"], key=lambda s: -s["priority_score"]):
        print(f"  {seg['name']}: score={seg['priority_score']} companies={seg['company_count']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
