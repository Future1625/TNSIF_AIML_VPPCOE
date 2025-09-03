def double_even_number(nums):
    return [num*2 for num in nums if num % 2 ==0]

print(double_even_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))