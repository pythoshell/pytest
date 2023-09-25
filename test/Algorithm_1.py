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

reverse_string_function()