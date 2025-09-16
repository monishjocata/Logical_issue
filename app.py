##I dont know-->is this branch?
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return True   # ❌ wrong, should return False
    return False           # ❌ wrong, should return True for prime

print(is_prime(7))  # Should be True, will give False

def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    # Logical bug: dividing by fixed 100 instead of length
    return total / 100  

print(calculate_average([10, 20, 30, 40, 50]))


def factorial(n):
    result = 0  # ❌ should start with 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))  # Expected 120, but gives 0


numbers = [1, 2, 3]
print(numbers[5])  # ❌ Index out of range

x = 10
y = 0
print(x / y)  # ❌ Division by zero

x = 10
y = 0
print(x / y)  # ❌ Division by zero

with open("not_exist.txt", "r") as f:
    data = f.read()  # ❌ File doesn’t exist
