"""OpenAI-compatible LLM client. Wrapped with neatlogs when tracing is active."""
from __future__ import annotations

import asyncio

from .config import Settings


class LLM:
    def __init__(self, settings: Settings, tracing_on: bool) -> None:
        self.settings = settings
        self.online = bool(settings.llm_api_key)
        self.client = None
        self.calls = 0
        self.prompt_tokens = 0
        self.completion_tokens = 0
        if self.online:
            import neatlogs
            from openai import OpenAI

            client = OpenAI(api_key=settings.llm_api_key, base_url=settings.llm_base_url)
            self.client = neatlogs.wrap(client) if tracing_on else client

    async def chat(self, system: str, user: str, temperature: float = 0.2, json_mode: bool = False) -> str:
        if not self.online:
            raise RuntimeError("LLM offline: set LLM_API_KEY or run --demo")
        kwargs: dict = {
            "model": self.settings.llm_model,
            "temperature": temperature,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
        }
        if json_mode:
            kwargs["response_format"] = {"type": "json_object"}
        resp = await asyncio.to_thread(self.client.chat.completions.create, **kwargs)
        self.calls += 1
        usage = getattr(resp, "usage", None)
        if usage is not None:
            self.prompt_tokens += int(getattr(usage, "prompt_tokens", 0) or 0)
            self.completion_tokens += int(getattr(usage, "completion_tokens", 0) or 0)
        else:
            self.prompt_tokens += (len(system) + len(user)) // 4
        return resp.choices[0].message.content


async def maybe_llm(llm: LLM, system: str, user: str, fallback: str, json_mode: bool = False) -> str:
    """LLM output when online, deterministic template otherwise. Never raises."""
    if not llm.online:
        return fallback
    try:
        return await llm.chat(system, user, json_mode=json_mode)
    except Exception:
        return fallback


def parse_json_loose(raw: str) -> dict:
    """Extract a JSON object from LLM output, tolerating ```json fences and prose."""
    import json
    import re

    text = raw.strip()
    fence = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
    if fence:
        text = fence.group(1)
    else:
        start = text.find("{")
        end = text.rfind("}")
        if start != -1 and end != -1 and end > start:
            text = text[start : end + 1]
    return json.loads(text)
