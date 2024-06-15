
def add_numbers(x, y):
    """This function adds two numbers."""
    result = x + y
    return x

# Call the function
#sum_result = add_numbers(3, 5)
#print("Sum:", sum_result)  # Output: Sum: 8


from Library import windows_file_handle

base_path = r"C:\PowerShell_Tests\engine"  # Change this to your base folder path
pattern = r""  # Change this to your regex pattern
#filter_directories(base_path,pattern)
resuk = windows_file_handle.filter_directories(base_path,pattern)
print(resuk)
count = 0

for dir_path in resuk:
    print(dir_path)
    count = count + 1
    print(count)