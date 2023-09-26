"""
**Reverse a String:**
Write a function to reverse a given string. For example,
if the input is "hello," the output should be "olleh."

"""


# Using String Slicing:

def reverse_string_slice_method(reversed_string):
   reversed_string = original_string[::-1]
   print(reversed_string)

original_string = "Hello, World!"
#reverse_string_slice_method(original_string)

#Reversed string using append from backside
def reverse_string_loopmethod():
   original_string = "Hello, World!"
   reversed_string = ""
   for char in original_string:
      print("character",char)
      reversed_string = char + reversed_string
      print("added values",reversed_string)
   print(reversed_string)

#reverse_string_loopmethod()

def reverse_string_function():
   original_string = "Hello, World!"
   reversed_string = list(reversed(original_string))
   print(reversed_string)

#reverse_string_function()



"""
2. **Check Palindrome:**
   Write a function to determine whether a given string is a palindrome (reads the same forwards and backwards).
      


"""


def is_palindrome_loop(s):
   s = s.lower()  # Convert to lowercase for case-insensitive comparison
   left, right = 0, len(s) - 1

   while left < right:
      if s[left] != s[right]:
         print("left",s[left])
         print("left", s[right])
         return False

      left += 1
      right -= 1
      print('left pass',left)
      print('Right pass', right)
   return True


# Test cases
print(is_palindrome_loop("racecar"))  # True
print(is_palindrome_loop("hello"))  # False




"""
Calculating the factorial of a non-negative integer is a common mathematical operation. 
The factorial of a non-negative integer n is denoted as n! and is the product of all positive integers from 1 to n. 
Here's how you can calculate the factorial of a number in Python using both iterative and recursive approaches:

1. Iterative Approach:
"""


def factorial_iterative(n):
   if n < 0:
      return "Factorial is not defined for negative numbers"
   elif n == 0:
      return 1
   else:
      result = 1
      for i in range(1, n + 1):
         result *= i
      return result


# Test cases
print(factorial_iterative(5))  # 120
print(factorial_iterative(0))  # 1
print(factorial_iterative(-1))  # Factorial is not defined for negative numbers
