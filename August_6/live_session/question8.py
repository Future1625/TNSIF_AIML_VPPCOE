# Dictionary - write a python function that takes a dictionary and returns the key with the maximum value

def max_value_key(dict1):
    return max(dict1, key=dict1.get)    

dict1 = {'a': 1, 'b': 3, 'c': 2}
result = max_value_key(dict1)
print("Key with maximum value:", result)