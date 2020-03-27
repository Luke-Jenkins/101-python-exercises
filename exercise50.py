# Section Title: Accessing List Elements
# exercises 50-59
# This is the first exercise in the section
# Write a function definition named first that takes in sequence and returns the first value of that sequence.
def first(input):
    count = 0
    for x in input:
        count += 1
        if count == 1:
            return x

first(["python", "is", "awesome"])
