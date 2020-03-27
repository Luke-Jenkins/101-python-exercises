vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
def is_vowel(l):
    for v in vowels:
        if v == l:
            return True
    return False

assert is_vowel("a") == True
assert is_vowel("U") == True
assert is_vowel("banana") == False
assert is_vowel("Q") == False
assert is_vowel("y") == False
print("Exercise 43 is correct.")