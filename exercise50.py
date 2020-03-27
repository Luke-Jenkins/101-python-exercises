def first(input):
    count = 0
    for x in input:
        count += 1
        if count == 1:
            return x

first(["python", "is", "awesome"])