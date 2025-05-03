# Copyright (c) Paillat-dev
# SPDX-License-Identifier: MIT

from dismoji import emojize


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
