vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
def remove_vowels(input):
    for x in input:
        for v in vowels:
            if x == v:
                input = input.replace(v,"")
    print(input)

remove_vowels("banana")