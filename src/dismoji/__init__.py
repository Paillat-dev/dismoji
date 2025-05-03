# Copyright (c) Paillat-dev
# SPDX-License-Identifier: MIT

from __future__ import annotations

import json
import re
from pathlib import Path

EMOJIS_PATH = Path(__file__).parent / "raw" / "build" / "emojis.json"

with EMOJIS_PATH.open("r", encoding="utf-8") as f:
    EMOJIS = json.load(f)

EMOJI_MAPPING: dict[str, str] = {k: EMOJIS["emojis"][v]["surrogates"] for k, v in EMOJIS["nameToEmoji"].items()}

EMOJI_PATTERN = re.compile(r"(?<!\w):([a-zA-Z0-9_-]+):(?!\w)")


def emojize(s: str) -> str:
    """Convert a string with emoji names to a string with emoji characters.

    Args:
        s (str): The input string containing emoji names.

    Returns:
        str: The input string with emoji names replaced by emoji characters.

    """

    def replace(match: re.Match[str]) -> str:
        emoji_name = match.group(1)
        if emoji_name in EMOJI_MAPPING:
            return EMOJI_MAPPING[emoji_name]
        return match.group(0)

    return EMOJI_PATTERN.sub(replace, s)
