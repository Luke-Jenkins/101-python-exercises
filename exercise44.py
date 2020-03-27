vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
def has_vowels(l):
    for x in l:
        for v in vowels:
            if x == v:
                return True
    return False

assert has_vowels("banana") == True
assert has_vowels("ubuntu") == True
assert has_vowels("QQQQ") == False
assert has_vowels("wyrd") == False
print("Exercise 44 is correct.")