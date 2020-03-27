vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
def count_vowels(input):
    count = 0
    for v in vowels:
        count += input.count(v)
    print(count)
count_vowels("banana")