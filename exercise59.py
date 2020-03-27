def first(input):
    count = 0
    for x in input:
        count += 1
        if count == 1:
            return x

def first_to_last(input):
    count = 0
    for x in input:
        count += 1
        if count == 1:
            input = input.remove(first(input))
    input = input.append(first(input))
    print(input)

first_to_last(["python", "is", "awesome"])