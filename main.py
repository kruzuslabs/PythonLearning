# Practice for problem solving
from typing import List


def is_palindrome(word: str) -> bool:
    """
    Check if a word is a palindrome.

    A palindrome is a word that reads the same forwards and backwards.

    Args:
        word (str): The word to check.

    Returns:
        bool: True if the word is a palindrome, False otherwise.
    """
    word = word.replace(" ", "").lower()
    return word == word[::-1]


def reverse_string(word: str) -> str:
    """
    Reverse a given string.

    Args:
        word (str): The string to reverse.

    Returns:
        str: The reversed string.
    """
    return word[::-1]


def invert_list(items: List[int]) -> List[int]:
    """
    Invert the sign of each item in a list.

    Args:
        items (List[int]): The list of integers.

    Returns:
        List[int]: A new list with the sign of each item inverted.
    """
    inverted = []
    for x in items:
        inverted.append(-x)
    return inverted
