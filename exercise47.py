vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
def starts_with_vowel(input):
    for x in input:
        for v in vowels:
            if x == v:
                return True
        return False

assert starts_with_vowel("banana") == True