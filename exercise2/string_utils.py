import re

def reverse_string(s: str) -> str:
    return s[::-1]

def count_vowels(s: str) -> int:
    vowels = "aeiou"
    return sum(1 for char in s.lower() if char in vowels)

def is_palindrome(s: str) -> bool:
    cleaned = ''.join(s.split()).lower()
    return cleaned == cleaned[::-1]

def capitalize_words(s: str) -> str:
    # On utilise une expression régulière pour conserver les espaces multiples.
    return re.sub(r'\S+', lambda m: m.group(0)[0].upper() + m.group(0)[1:], s)
