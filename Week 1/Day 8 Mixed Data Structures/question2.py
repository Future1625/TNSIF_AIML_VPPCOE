# 2.Given a dictionary with values as lists, write a program to flatten all values into a single list.

data = {
    "a": [1, 2],
    "b": [3, 4],
    "c": [5, 6]
}

flattened = []
for value_list in data.values():
    flattened.extend(value_list)

print("Flattened list:", flattened)