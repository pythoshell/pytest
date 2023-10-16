"""
Try-Except Blocks:
Use try and except to catch and handle exceptions.

"""

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Test1 Error: {e}")

"""
Handling Multiple Exceptions:
You can handle multiple exceptions in a single try-except block.
"""

try:
    value = int("abc")
except (ValueError, TypeError) as e:
    print(f"Test2 Error: {e}")

"""
Using else and finally:
The else block is executed if no exception occurs, and the finally block is executed regardless of whether an exception occurred.
"""

try:
    value = int("123")
except ValueError as e:
    print(f"Test 3 Error: {e}")
else:
    print("Test 3 No error occurred.")
finally:
    print("Test 3 This will always be executed.")

"""
Raising Exceptions:
You can raise your own exceptions using the raise statement.
"""


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b


try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    print(f" Test4 Error: {e}")

"""
Custom Exception Classes:
You can create custom exception classes by inheriting from Exception or a more specific exception class.
"""


class NegativeNumberError(Exception):
    pass

def process_positive_number(number):
    if number < 0:
        raise NegativeNumberError("Test5 Negative numbers are not allowed")
    # Perform some processing

try:
    value = -5
    process_positive_number(value)

except NegativeNumberError as e:
    print(f"Error: {e}")



"""
Handling File I/O Errors:
When working with files, you should handle file I/O exceptions.
"""

try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"Error: {e}")

"""
Assertion Error:
Use assert for debugging and checking conditions. An AssertionError is raised if the condition is False.
"""
age = 17
try:
    assert age >= 18, "Age must be 18 or older"

except AssertionError as er:
    print("Test6 error for assert ")

"""
Handling Unknown Exceptions:
You can use a generic except block to catch unknown exceptions.
"""

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Unknown Error: {e}")

"""
Using except with as for detailed error information:
You can catch exceptions and access detailed information about the exception using as.
"""
try:
    value = int("abc")
except ValueError as e:
    print(f"Error Type: {type(e)}")
    print(f"Error Message: {e}")
