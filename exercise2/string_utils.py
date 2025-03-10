# Exercise 2: String Utilities


def reverse_string(s: str) -> str:
    """
    Return the input string in reverse order.

    Args:
        s: Input string

    Returns:
        The reversed string
    """
    s_l=list(s)
    s_l.reverse()
    return "".join(s_l)



def count_vowels(s: str) -> int:
    """
    Return the number of vowels (a, e, i, o, u) in the input string.
    Case-insensitive: both uppercase and lowercase vowels should be counted.

    Args:
        s: Input string

    Returns:
        The number of vowels in the string
    """
    v=("a", "e", "i", "o", "u")
    count=0
    small_s=s.lower()
    for letter in list(small_s):
        if letter in v:
            count+=1
    return count


def is_palindrome(s: str) -> bool:
    """
    Check if the input string is a palindrome.
    A palindrome reads the same backward as forward.
    Spaces and case should be ignored.

    Args:
        s: Input string

    Returns:
        True if the string is a palindrome, False otherwise
    """
    clean_s="".join(s.split()).lower()
    if clean_s==reverse_string(clean_s):
        return True
    else:
        return False


def capitalize_words(s: str) -> str:
    """
    Capitalize the first letter of each word in the input string.

    Args:
        s: Input string

    Returns:
        The input string with the first letter of each word capitalized
    """
    return ' '.join(word.capitalize() for word in s.split(' '))
