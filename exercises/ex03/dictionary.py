"""Dictionary utility functions for EX03 - COMP110."""

__author__ = "730830842"


def invert(d: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of the input dictionary."""
    result: dict[str, str] = {}
    for key in d:
        value = d[key]
        if value in result:
            raise KeyError(f"Duplicate key found when inverting: {value}")
        result[value] = key
    return result


def count(items: list[str]) -> dict[str, int]:
    """Returns dictionary where each key is a unique with # of times it appears."""
    result: dict[str, int] = {}

    for item in items:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


def favorite_color(favs: dict[str, str]) -> str:
    """Returns the color that appears the most"""
    color_counts: dict[str, int] = count(list(favs.values()))
    max_count = 0
    most_common = ""

    for name in favs:
        color = favs[name]
        if color_counts[color] > max_count:
            max_count = color_counts[color]
            most_common = color
    return most_common


def bin_len(words: list[str]) -> dict[int, set[str]]:
    """Bins a list of strings by length, grouped in sets"""
    result: dict[int, set[str]] = {}

    for word in words:
        length = len(word)
        if length in result:
            result[length].add(word)
        else:
            result[length] = {word}

    return result
