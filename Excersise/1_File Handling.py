
"""
Exercise 1: Read a Text File
Create a text file called "sample.txt" with some text in it.
Write a Python program to open and read the
contents of the file and print them to the console.

"""

# Open and read a text file
with open("sample.txt", "r") as file:
    contents = file.read()
    print(contents)



"""
Exercise 2: Write to a Text File
Create a Python program that prompts the 
user to enter text and then write that text to a new text file called "output.txt."
"""

# Get user input and write to a text file
user_input = input("Enter text: ")
with open("output.txt", "w") as file:
    file.write(user_input)


"""
Exercise 3: Append to a Text File
Modify the program from Exercise 2 to append the user's input to an existing text file, rather than overwriting it.

"""
# Get user input and append to a text file
user_input = input("Enter text: ")
with open("output.txt", "a") as file:
    file.write(user_input)


"""
Exercise 4: Count Lines in a Text File
Write a program to count the number of lines in a text file and print the count.

"""

# Count lines in a text file
with open("sample.txt", "r") as file:
    line_count = len(file.readlines())
    print(f"Line count: {line_count}")


"""
Exercise 5: Word Frequency Counter
Create a program that reads a text file, 
counts the frequency of each word, and prints the word frequencies. 
You can use a dictionary to store the word frequencies.

"""

# Word frequency counter
word_freq = {}
with open("sample.txt", "r") as file:
    text = file.read()
    words = text.split()
    for word in words:
        word = word.strip(".,!?").lower()
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

for word, freq in word_freq.items():
    print(f"{word}: {freq}")


"""
Exercise 6: CSV File Operations
Read data from a CSV file, perform some operations 
(e.g., calculate the sum or average of a column), 
and write the results to another CSV file.

Exercise 7: JSON File Operations
Read data from a JSON file, manipulate the data 
(e.g., filter or modify it), and save the updated data to a new JSON file.

Exercise 8: Error Handling
Add error handling to your file handling programs. 
For example, handle file not found errors and permission errors gracefully.

"""