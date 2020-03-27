def last(input):
    input_length = len(input)
    input_slice = input[input_length::-1]
    count = 0
    for x in input_slice:
        count += 1
        if count == 1:
            print(x)

last("banana")