vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
def count_vowels(input):
    count = 0
    for x in input:
        for v in vowels:
            if x == v:
                count += 1
    return count

count_vowels("banana")