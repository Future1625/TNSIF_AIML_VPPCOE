#  check if two sets have common elements

def common_elements(set1, set2):
    return len(set1 & set2) > 0

a = {1, 2, 3}
b = {3, 4, 5}

print("Do they have common elements?", common_elements(a, b))
