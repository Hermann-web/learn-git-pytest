# Exercise 2: String Utilities


def reverse_string(s: str) -> str:
    return s[::-1]
    # TODO: Implement this function
    pass


def count_vowels(s: str) -> int:
    vowels = "aeiou"
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count
    # TODO: Implement this function
    pass


def is_palindrome(s: str) -> bool:
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]
    # TODO: Implement this function
    pass


def capitalize_words(s: str) -> str:
    words = s.split()
    capitalized_words = [word.capitalize() for word in words]
    return " ".join(capitalized_words)
    # TODO: Implement this function
    pass
