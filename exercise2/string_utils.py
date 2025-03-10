# Exercise 2: String Utilities


def reverse_string(s: str) -> str:
    """
    Return the input string in reverse order.

    Args:
        s: Input string

    Returns:
        The reversed string
    """
    # TODO: Implement this function
    return s[::-1] # méthode le slicing


def count_vowels(s: str) -> int:
    """
    Return the number of vowels (a, e, i, o, u) in the input string.
    Case-insensitive: both uppercase and lowercase vowels should be counted.

    Args:
        s: Input string

    Returns:
        The number of vowels in the string
    """
    # TODO: Implement this function
    vowels = {'a', 'e', 'i', 'o', 'u'} # Définir l'ensemble des voyelles
    s = s.lower() # Convertir la chaîne en minuscules
    total_vowels = 0
    for char in s:
        if char in vowels:
            total_vowels += 1  # Incrémenter si le caractère est une voyelle
            
    return total_vowels


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
    # TODO: Implement this function

     # Convertir la chaîne en minuscules et supprimer les espaces
    
    s_no_spaces = s.replace(" ", "")
    cleaned_s = s_no_spaces.lower()
    return cleaned_s == cleaned_s[::-1]


def capitalize_words(s: str) -> str:
    """
    Capitalize the first letter of each word in the input string.

    Args:
        s: Input string

    Returns:
        The input string with the first letter of each word capitalized
    """
    # TODO: Implement this function
    return s.title()

