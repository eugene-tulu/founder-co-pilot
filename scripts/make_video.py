#!/usr/bin/env python3
"""Generate the StageZero demo video programmatically (slides + TTS + ffmpeg).

Real command outputs are captured live so the video shows genuine artifacts.
Dashboard inserts (neatlogs Traces UI, cfo.ai Model) are marked [RECORD INSERT].
"""
from __future__ import annotations

import re
import subprocess
import sys
import textwrap
import wave
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
DEMO = ROOT / "demo"
PY = "/home/tulu/miniconda3/envs/ndvi/bin/python"
FFMPEG = "/home/tulu/miniconda3/envs/ndvi/lib/python3.13/site-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2"

W, H = 1280, 720
BG = (13, 17, 23)
FG = (201, 209, 217)
GREEN = (63, 185, 80)
YELLOW = (210, 153, 34)
CYAN = (88, 166, 255)
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
MONO_B = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"


def run(cmd: list[str], cwd: Path = ROOT) -> str:
    proc = subprocess.run(cmd, capture_output=True, text=True, cwd=cwd, timeout=300)
    return (proc.stdout + proc.stderr).strip()


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size)


def wrap(text: str, width: int) -> list[str]:
    out: list[str] = []
    for line in text.splitlines():
        out.extend(textwrap.wrap(line, width=width) or [""])
    return out


def render(title: str, body: str, path: Path, accent=FG) -> None:
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)
    f_title = font(MONO_B, 28)
    f_body = font(MONO, 20)
    f_small = font(MONO, 16)
    draw.rectangle([0, 0, W, 60], fill=(22, 27, 34))
    draw.text((26, 15), title, font=f_title, fill=accent)
    draw.text((26, 68), "github.com/eugene-tulu/founder-co-pilot", font=f_small, fill=(110, 118, 129))
    y = 104
    for line in wrap(body, 96)[:24]:
        draw.text((26, y), line, font=f_body, fill=FG)
        y += 26
    img.save(path)


def duration(wav: Path) -> float:
    with wave.open(str(wav)) as w:
        return w.getnframes() / float(w.getframerate())


def main() -> int:
    DEMO.mkdir(exist_ok=True)
    for old in list(DEMO.glob("slide_*")) + list(DEMO.glob("seg_*")):
        old.unlink()

    # ---- live captures -------------------------------------------------
    demo_run = run([PY, "-m", "stagezero", "run", "--idea",
                    "AI agent that chases unpaid invoices for independent consultants", "--demo"])
    m = re.search(r"run (run-\S+) complete", demo_run)
    if not m:
        raise SystemExit(f"could not parse run id:\n{demo_run[:400]}")
    run_id = m.group(1)
    kit = (ROOT / "runs" / run_id / "VALIDATION_KIT.md").read_text().splitlines()
    kit_excerpt = "\n".join(kit[:12] + ["...", kit[-4] if len(kit) > 4 else ""])
    demo_clean = re.sub(r"^\d{4}-\d{2}-\d{2}.*$", "", demo_run, flags=re.M).strip()
    chaos = run([PY, "-m", "stagezero", "run", "--idea", "AI agent that chases unpaid invoices",
                 "--demo", "--fail-at", "discover"])
    chaos_tail = "\n".join(chaos.splitlines()[-3:])
    resume_out = run([PY, "-m", "stagezero", "run", "--idea", "AI agent that chases unpaid invoices",
                      "--resume", "run-20261012-080405-09d5b8"])
    graph_hit = run(["bash", "-lc", "export PATH=$HOME/.local/bin:$PATH; entire graph search --repo . "
                     "--profile full --query 'segment priority scoring' --format agent"])
    graph_lines = "\n".join(graph_hit.splitlines()[:8])
    biz = "\n".join(
        line for line in (ROOT / "business" / "BUSINESS_PLAN.md").read_text().splitlines()
        if line.startswith("|") or "cost per run" in line.lower() or "Inference" in line
    )[:850]
    snap_lines = sum(1 for _ in (ROOT / "runs" / "entire-graph.ndjson").open())

    slides = [
        ("StageZero — customer discovery for founders",
         "neatHack #1 · team tulu\n\nOne idea in: falsifiable problem statement, data-sized\n"
         "segments, Mom Test scripts, proceed/pivot/kill decision.",
         "StageZero is a customer discovery agent for pre-P-M-F founders, built for neatHack. One idea in: a "
         "falsifiable problem statement, data-sized segments, Mom Test scripts, and a decision sourced to real data."),
        ("The problem",
         "Founders skip customer discovery and build the wrong thing.\n\n"
         "ACQ $100M roadmap, Stage 0: \"nothing is happening; get people\n"
         "to try your stuff for free.\" Graduation = helpful unprompted.\n\n"
         "StageZero automates that stage — and never states an\nunsourced number.",
         "Founders skip discovery and build the wrong thing. Stage zero on the roadmap is, get people to try your "
         "stuff for free. StageZero automates that stage, and never states a number it cannot source."),
        ("Architecture",
         "idea -> ingest -> plan -> discover -> analyze -> guardrail -> scriptkit -> report\n"
         "         normalise  3 ICP     segment       score        every       Mom Test     validation kit\n"
         "                   hypoth.   sizing +      segments     number       scripts\n"
         "                   (LLM)     pain signals + decide      traced to\n"
         "                             (Crustdata)   proceed/     tool\n"
         "                                           pivot/kill   output\n\n"
         "Every stage = a neatlogs span. State persists per stage (resumable).",
         "Seven stages. The LLM plans three segments; Crustdata supplies real segment sizes and hiring pain signals; "
         "scoring is transparent; a guardrail blocks unsourced numbers; every stage is a neatlogs span."),
        ("Runtime — offline demo", demo_clean,
         "It runs offline, no keys needed, and reaches a decision in about two seconds."),
        ("The validation kit", kit_excerpt,
         "The kit: a stage diagnosis, a falsifiable problem statement, ranked segments with evidence, ten Mom Test "
         "questions per segment, an experiment plan, graduation gates, and kill criteria."),
        ("neatlogs — traces, failures, recovery",
         "6 traces in \"Eugene's project\", workflow stagezero:\n\n"
         "  fe7451c8...  BEFORE v1 contract: calls failed, 0 companies, pivot\n"
         "  3100c861...  AFTER  fix c5b4cb2: 1.49M / 169,908 / 68,916, proceed\n"
         "  eb9dcc1f...  LLM-planned hypotheses: 5.2M / 2.7M / 2.3M, proceed\n"
         "  caf8a8e3...  7 spans, 6 LLM calls; credits-out surfaced, not zeros\n\n"
         "[RECORD INSERT: neatlogs Traces dashboard — span tree + stage_end events]",
         "Neatlogs: every stage, tool call and guardrail verdict is traced. The before-after pair shows improvement: "
         "the first run failed with zero segments, we read the failing calls from traces, fixed the contract, and the "
         "same idea then produced real segment sizes."),
        ("Recovery — failure injection",
         f"$ python -m stagezero run --idea \"...\" --demo --fail-at discover\n\n{chaos_tail}\n\n"
         "run_state.json records failure + recovery; stages replay on resume.",
         "With fail-at, discover fails once. Failure and recovery are recorded in run state; the agent retries "
         "degraded and still delivers the kit."),
        ("Resume — state across runs",
         f"$ python -m stagezero run --idea \"...\" --resume run-20261012-080405-09d5b8\n\n"
         f"{chr(10).join(resume_out.splitlines()[:4])}\n\nZero API calls; identical kit.",
         "State persists per stage: any past run rebuilds from its state file with zero API calls."),
        ("Entire — code graph",
         f"entire graph snapshot --format ndjson > runs/entire-graph.ndjson ({snap_lines} lines)\n\n"
         f"$ entire graph search --query \"segment priority scoring\"\n{graph_lines}\n\n"
         "Repo on Entire: https://entire.io/gh/eugene-tulu/founder-co-pilot (public)",
         "Entire: CLI and graph plugin are active. The full code graph is committed, and graph search answers "
         "codebase questions with file and line evidence."),
        ("cfo.ai — the business plan",
         f"scripts/make_business_plan.py turns measured run costs into the plan:\n\n{biz}\n\n"
         "[RECORD INSERT: cfo.ai Model — pricing / costs / revenue / runway]",
         "cfo.ai: the plan is generated from measured costs, not guesses. Measured cost is about one and a half cents "
         "per run; scenarios project revenue and margin from one hundred to two thousand customers, with runway on "
         "hackathon credits."),
        ("Close",
         "Founders who validate with evidence ship fewer products nobody wants.\n\n"
         "Repo:     github.com/eugene-tulu/founder-co-pilot\n"
         "neatlogs: 6 traces (IDs in docs/EVIDENCE.md)\n"
         "Entire:   graph snapshot + public repo on Entire\n"
         "cfo.ai:   business/BUSINESS_PLAN.md (+ live Model)\n"
         "Crustdata: live runs + cache\n\nneatHack #1 — team tulu",
         "Founders who validate with evidence ship fewer products nobody wants. All evidence is in the public "
         "repository."),
    ]

    # ---- render + TTS ---------------------------------------------------
    segments = []
    for i, (title, body, narration) in enumerate(slides):
        png = DEMO / f"slide_{i:02d}.png"
        wav = DEMO / f"slide_{i:02d}.wav"
        accent = GREEN if "neatlogs" in title or "Close" in title else (CYAN if "Entire" in title else (YELLOW if "cfo" in title else FG))
        render(title, body, png, accent)
        subprocess.run(["espeak", "-s", "152", "-v", "en-us", "-w", str(wav), narration], check=True)
        dur = duration(wav) + 0.5
        segments.append((png, wav, dur))
        print(f"slide {i:02d}: {title[:42]:42s} {dur:5.1f}s")

    total = sum(d for _, _, d in segments)
    with open(DEMO / "concat.txt", "w") as fh:
        for png, wav, dur in segments:
            seg = DEMO / f"seg_{png.stem}.mp4"
            subprocess.run([
                FFMPEG, "-y", "-loglevel", "error", "-loop", "1", "-i", str(png), "-i", str(wav),
                "-t", f"{dur:.2f}", "-vf", "format=yuv420p", "-c:v", "libx264", "-c:a", "aac",
                "-shortest", str(seg),
            ], check=True)
            fh.write(f"file '{seg.name}'\n")
    subprocess.run([
        FFMPEG, "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", "concat.txt",
        "-c:v", "libx264", "-c:a", "aac", "-movflags", "+faststart", str(DEMO / "stagezero-demo.mp4"),
    ], check=True, cwd=DEMO)
    print(f"\nwrote {DEMO / 'stagezero-demo.mp4'}  ({total:.0f}s, {len(segments)} slides)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
