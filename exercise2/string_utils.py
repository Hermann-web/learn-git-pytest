# Exercise 2: String Utilities


def reverse_string(s: str) -> str:
    n=len (s)
    L=[]
    for i in rang(n):
        L.append(s[n-1-i])
    return str(L)


    # TODO: Implement this function
    pass

from collections import Counter
def count_vowels(s: str) -> int:
    vowels= set("aeuioyAEUIOY")
    counter= Counter(s)
    return sum(counter[v] for v in counter.keys() & vowels)    
    # TODO: Implement this function
    pass


def is_palindrome(s: str) -> bool:
    n=len(s)
    L=[]
    for i in range(n):
        if not L[i]!=" ":
            L.append(s[i])
    for j in range(n):
        if L[i]!=L[n-1-i]:
            return False 
        else:
            return True 

    # TODO: Implement this function
    pass


def capitalize_words(s: str) -> str:
    n=len(s)
    L=[]
    for i in range(n):
        L.append(s[i])
    for j in range(n):
        if L[j]==" ":
            L[j+1]= upper(L[j+1])
    L[0]=upper(L[0])
    return str(L)
    # TODO: Implement this function
    pass
