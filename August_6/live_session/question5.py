# Tuple - write a python function that takes a tuple of numbers and returns the sum of all elements

def tuple_sum(tuple1):
    return sum(tuple1)

tuple1 = (1, 2, 3, 4, 5)
result = tuple_sum(tuple1)
print("Sum of tuple elements: ", result)