# write a python function to check whether a given number is a prime number or not

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

is_prime_number = is_prime(29) 
print(f"Is num a prime number? {is_prime_number}")