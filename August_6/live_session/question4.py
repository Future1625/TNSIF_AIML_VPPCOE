# Tuple - given a list of tuples, write a function that return a list of tuples sorted based on the second element in each tuple

def sorted_tuples(tuples_list):
    return sorted(tuples_list, key=lambda x: x[1])

tuples_list = [(1, 3), (3, 2), (2, 1)]
sorted_list = sorted_tuples(tuples_list)
print(sorted_list)