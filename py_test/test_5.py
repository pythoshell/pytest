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
      for i in range(1, n+1):
         print("why n+1 in fact",i)
         result *= i
      return result


# Test cases
#print(factorial_iterative(5))  # 120
#print(factorial_iterative(0))  # 1
#print(factorial_iterative(-1))  # Factorial is not defined for negative numbers
"""
Python function to find the maximum element in an array of integers, using different approaches:


"""

def find_max(arr):
   if len(arr) == 0:
      return None  # Return None for empty arrays
   max_element = arr[0]
   for num in arr:
      if num > max_element:
         max_element = num
   return max_element

print(find_max([10,22,55,77,99,34,65,76]))

"""
You can write a Python function to remove duplicates from an array of integers while 
maintaining the order of appearance by using a for loop and a set to keep track of the seen elements. Here's a sample implementation:
"""
def remove_duplicates(arr):
   seen = set()
   result = []
   for num in arr:
      if num not in seen:
         seen.add(num)
         result.append(num)
   return result


# Example usage:
original_array = [3, 2, 1, 2, 4, 3, 5, 6, 5]
result_array = remove_duplicates(original_array)
print("Array with duplicates removed:", result_array)


"""
  Write a function to count the number of words in a given sentence.
  
"""

