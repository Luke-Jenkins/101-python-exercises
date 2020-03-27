vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
def ends_with_vowel(input):
    input_length = len(input)
    input_slice = input[input_length::-1]
    for x in input_slice:
        for v in vowels:
            if x == v:
                return True
        return False

assert ends_with_vowel("banana") == True