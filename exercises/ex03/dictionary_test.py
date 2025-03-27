"""Tests for dictionary functions."""

__author__ = "730830842"

import pytest
from exercises.ex03.dictionary import invert, count, favorite_color, bin_len


def test_invert_use_case():
    """Tests a regular use case with unique values"""
    assert invert({"a": "z", "b": "y", "c": "x"}) == {"z": "a", "y": "b", "x": "c"}


def test_invert_single_pair():
    """Tests an edge case with only one key-value pair."""
    assert invert({"apple": "cat"}) == {"cat": "apple"}


def test_invert_raises_key_error():
    """Tests KeyError is raised when duplicate exists in dictionary"""
    with pytest.raises(KeyError):
        invert({"kris": "jordan", "michael": "jordan"})


def test_count_empty_list():
    """Edge case: an empty list should return an empty dictionary"""
    assert count([]) == {}


def test_count_multiple_repeats():
    """Use case: items repeat multiple times"""
    input_list = ["apple", "banana", "apple", "banana", "apple"]
    expected = {"apple": 3, "banana": 2}
    assert count(input_list) == expected


def test_count_no_repeats():
    """Use case: no repeated items."""
    input_list = ["a", "b", "c"]
    expected = {"a": 1, "b": 1, "c": 1}
    assert count(input_list) == expected


def test_favorite_color_single_entry():
    """Edge case: only one person."""
    assert favorite_color({"Alice": "blue"}) == "blue"


def test_favorite_color_clear_winner():
    """Use case: one color more than others."""
    favs = {"Alice": "blue", "Bob": "red", "Charlie": "blue", "Dana": "green"}
    assert favorite_color(favs) == "blue"


def test_favorite_color_tie():
    """Use case: tie between two colors, return first"""
    favs = {"Alice": "blue", "Bob": "red", "Charlie": "red", "Dana": "blue"}
    assert favorite_color(favs) == "blue"


def test_bin_len_empty_list():
    """Edge case: empty list returns empty dict"""
    assert bin_len([]) == {}


def test_bin_len_various_lengths():
    """Use case: words of diff lengths grouped."""
    words = ["hi", "cat", "car", "elephant"]
    expected = {2: {"hi"}, 3: {"cat", "car"}, 8: {"elephant"}}
    assert bin_len(words) == expected


def test_bin_len_duplicates():
    """Use case: duplicate words"""
    words = ["the", "the", "fox"]
    expected = {3: {"the", "fox"}}
    assert bin_len(words) == expected
