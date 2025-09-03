# list- given the list of integers, write a function to return a new list containing only the even numbers from the original list 

def even_numbers(list1):
    even_list = []
    for num in list1:
        if num % 2 ==0:
            even_list.append(num)
    return even_list

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = even_numbers(list1)
print(even_list)