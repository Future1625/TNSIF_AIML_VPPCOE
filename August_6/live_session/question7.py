# Set - write a python program to remove all duplicates from a list using a set and return the unique elements as a list

def remove_duplicates(my_list):
    unique_list = list(set(my_list))
    return unique_list

my_list = [1, 2, 2, 3, 4, 4, 5]
result = remove_duplicates(my_list)
print(result)