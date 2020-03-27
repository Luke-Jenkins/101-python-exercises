vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
def starts_with_vowel(input):
    for x in input:
        for v in vowels:
            if x == v:
                return True
        return False

def ends_with_vowel(input):
    input_length = len(input)
    input_slice = input[input_length::-1]
    for x in input_slice:
        for v in vowels:
            if x == v:
                return True
        return False

def starts_and_ends_with_vowel(input):
    if starts_with_vowel(input) == True and ends_with_vowel(input) == True:
        return True
    else:
        return False