def second_largest(nums):
    if len(nums) < 2:
        return "Need at least two numbers"

    max_num = max(nums) 
    filtered = [n for n in nums if n != max_num]  

    return max(filtered) 

num = [12, 35, 1, 10, 34, 1]
print("Second largest number is:", second_largest(num))
