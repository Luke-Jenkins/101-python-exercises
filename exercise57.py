def first(input):
    count = 0
    for x in input:
        count += 1
        if count == 1:
            return x

def second(input):
    count = 0
    for x in input:
        count += 1
        if count == 2:
            return x

def first_and_second(input):
    x = [first(input), second(input)]
    return x

assert first_and_second([1, 2, 3, 4]) == [1, 2]
assert first_and_second(["python", "is", "awesome"]) == ["python", "is"]
assert first_and_second(["strawberry", "kiwi", "mango", "guava"]) == ["strawberry", "kiwi"]
print("Exercise 57 is correct.")