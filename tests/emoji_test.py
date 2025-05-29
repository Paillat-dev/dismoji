# Copyright (c) Paillat-dev
# SPDX-License-Identifier: MIT

from dismoji import EMOJI_MAPPING, REVERSE_EMOJI_MAPPING, demojize, emojize


def are_equal(a: str, b: str) -> bool:
    """Check if two emojis are equal."""
    if len(a) != len(b):
        return False
    if len(a) == 1:
        return a == b
    return a[0] == b[0] and set(a[1:]) == set(b[1:])


def test_basic() -> None:
    """Test basic functionality of emojize function."""
    assert emojize("Hello :smile:") == "Hello 😄"


def test_no_match() -> None:
    """Test emojize function with no matches."""
    assert emojize("Hello world") == "Hello world"


def test_not_emoji() -> None:
    """Test emojize function with non-emoji input."""
    assert emojize("Hello :not_an_emoji:") == "Hello :not_an_emoji:"


def test_surrogate() -> None:
    """Test emojize function with surrogate pairs."""
    surrogate_pairs = [
        (":handshake_light_skin_tone_dark_skin_tone:", "🫱🏻‍🫲🏿"),
        (":handshake_dark_skin_tone_light_skin_tone:", "🫱🏿‍🫲🏻"),
        (":handshake_medium_skin_tone_light_skin_tone:", "🫱🏽‍🫲🏻"),
        (":handshake_medium_light_skin_tone_dark_skin_tone:", "🫱🏼‍🫲🏿"),
        (":handshake_medium_dark_skin_tone_light_skin_tone:", "🫱🏾‍🫲🏻"),
    ]

    for emoji_name, surrogate in surrogate_pairs:
        assert emojize(emoji_name) == surrogate


def test_multiple_emojis() -> None:
    """Test emojize function with multiple emojis."""
    assert emojize(":smile: :wave:") == "😄 👋"


def test_complex_sentence() -> None:
    """Test emojize function with a complex sentence."""
    assert emojize("Hello :wave:, what's up? :smile: :white_check_mark: :smile:") == "Hello 👋, what's up? 😄 ✅ 😄"


def test_spaces() -> None:
    """Test emojize function with spaces."""
    space_tests = [
        ("Hello :smile::smile:", "Hello 😄😄"),
        ("Hii what's up :wave:?", "Hii what's up 👋?"),
        ("Hello:wave: :smile:", "Hello👋 😄"),
        ("Hellooo :wave:hru?", "Hellooo 👋hru?"),
        ("Hii:wave:hru?", "Hii👋hru?"),
    ]
    for input_str, expected_output in space_tests:
        assert emojize(input_str) == expected_output


def test_emoji_with_special_characters() -> None:
    """Test emojize function with special characters."""
    special_char_tests = [
        ("Hello :smile:!", "Hello 😄!"),
        ("Hello :smile:?", "Hello 😄?"),
        ("Hello :smile::smile:!", "Hello 😄😄!"),
        ("Hello :smile::smile:?", "Hello 😄😄?"),
        ("Hello :smile::smile::smile:!", "Hello 😄😄😄!"),
        ("Hello :smile::smile::smile:?", "Hello 😄😄😄?"),
    ]
    for input_str, expected_output in special_char_tests:
        assert emojize(input_str) == expected_output


def test_emojize_all() -> None:
    for name, emoji in EMOJI_MAPPING.items():
        assert are_equal(emojize(f":{name}:"), emoji)


def test_demojize_basic() -> None:
    """Test basic functionality of demojize function."""
    assert demojize("Hello 😄") == "Hello :smile:"


def test_demojize_no_match() -> None:
    """Test demojize function with no matches."""
    assert demojize("Hello world") == "Hello world"


def test_demojize_multiple_emojis() -> None:
    """Test demojize function with multiple emojis."""
    assert demojize("😄 👋") == ":smile: :wave:"


def test_demojize_complex_sentence() -> None:
    """Test demojize function with a complex sentence."""
    assert demojize("Hello 👋, what's up? 😄 ✅ 😄") == "Hello :wave:, what's up? :smile: :white_check_mark: :smile:"


def test_demojize_surrogate() -> None:
    """Test demojize function with surrogate pairs."""
    surrogate_pairs = [
        ("🫱🏻‍🫲🏿", ":handshake_light_skin_tone_dark_skin_tone:"),
        ("🫱🏿‍🫲🏻", ":handshake_dark_skin_tone_light_skin_tone:"),
        ("🫱🏽‍🫲🏻", ":handshake_medium_skin_tone_light_skin_tone:"),
        ("🫱🏼‍🫲🏿", ":handshake_medium_light_skin_tone_dark_skin_tone:"),
        ("🫱🏾‍🫲🏻", ":handshake_medium_dark_skin_tone_light_skin_tone:"),
    ]

    for surrogate, emoji_name in surrogate_pairs:
        assert demojize(surrogate) == emoji_name


def test_demojize_all() -> None:
    for emoji, name in REVERSE_EMOJI_MAPPING.items():
        assert demojize(emoji) == f":{name}:"
