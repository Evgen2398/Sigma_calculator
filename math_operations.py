

def calculate_sum(numbers):
    return sum(numbers)

def calculate_difference(a, b):
    return a - b

def calculate_product(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def calculate_division(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

