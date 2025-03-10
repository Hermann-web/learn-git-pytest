# Exercise 2: String Utilities


def reverse_string(s: str) -> str:
    
    return s[::-1]


def count_vowels(s: str) -> int:
    return sum(1 for c in s.lower() if c in "aeiou")


def is_palindrome(s: str) -> bool:
  s = s.lower().replace(" ", "")  # Convertir en minuscule et enlever les espaces
  return s == s[::-1]


def capitalize_words(s: str) -> str:
    words = s.split()  # Sépare les mots
    capitalized_words = [word.capitalize() for word in words]  # Met la première lettre en majuscule
    return " ".join(capitalized_words)