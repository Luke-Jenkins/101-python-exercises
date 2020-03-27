# Section Title: Accessing List Elements
# exercises 50-59
# This is the last exercise in the section
# Goal: Write a function definition named first_to_last that takes in sequence and returns the sequence 
# with the first value moved to the end of the sequence.
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
