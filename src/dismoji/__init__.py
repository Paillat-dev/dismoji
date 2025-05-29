# Copyright (c) Paillat-dev
# SPDX-License-Identifier: MIT

from __future__ import annotations

import json
import re
from pathlib import Path

EMOJIS_PATH = Path(__file__).parent / "raw" / "build" / "emojis.json"

with EMOJIS_PATH.open("r", encoding="utf-8") as f:
    EMOJIS = json.load(f)

_VARIATION_SELECTOR = "\ufe0f"  # We remove this as it is not needed by discord and causes issues with tests
EMOJI_MAPPING: dict[str, str] = {
    k: EMOJIS["emojis"][v]["surrogates"].replace(_VARIATION_SELECTOR, "") for k, v in EMOJIS["nameToEmoji"].items()
}

REVERSE_EMOJI_MAPPING: dict[str, str] = {}

for emoji_index_str, emoji_index in sorted(EMOJIS["surrogateToEmoji"].items(), key=lambda x: len(x[0]), reverse=True):
    # Get the first name in the list as the preferred name
    e = EMOJIS["emojis"][emoji_index]
    # If it has multiple diversity parents, use the last name because it is the most specific one
    # e.g. :handshake_light_skin_tone_dark_skin_tone: vs :handshake_tone1_tone5:
    REVERSE_EMOJI_MAPPING[emoji_index_str] = e["names"][-1 if e.get("hasMultiDiversityParent") else 0]

del EMOJIS, _VARIATION_SELECTOR  # Clean up to save memory

EMOJI_PATTERN = re.compile(r":([\w+-]+):")

EMOJI_CHARS_PATTERN = re.compile("|".join(map(re.escape, REVERSE_EMOJI_MAPPING.keys())))


def _replace(match: re.Match[str]) -> str:
    emoji_name = match.group(1)
    if emoji_name in EMOJI_MAPPING:
        return EMOJI_MAPPING[emoji_name]
    return match.group(0)


def emojize(s: str) -> str:
    """Convert a string with emoji names to a string with emoji characters.

    Args:
        s (str): The input string containing emoji names.

    Returns:
        str: The input string with emoji names replaced by emoji characters.

    """
    return EMOJI_PATTERN.sub(_replace, s)


def _reverse_replace(match: re.Match[str]) -> str:
    emoji = match.group(0)
    return f":{REVERSE_EMOJI_MAPPING[emoji]}:"


def demojize(s: str) -> str:
    """Convert a string with emoji characters to a string with emoji names.

    Args:
        s (str): The input string containing emoji characters.

    Returns:
        str: The input string with emoji characters replaced by emoji names.

    """
    return EMOJI_CHARS_PATTERN.sub(_reverse_replace, s)


__all__ = (
    "EMOJI_MAPPING",
    "REVERSE_EMOJI_MAPPING",
    "demojize",
    "emojize",
)
