import os
import re

def filter_directories(base_path, pattern):
    # Compile the regex pattern for efficiency
    regex = re.compile(pattern)

    # Iterate over directories
    for root, dirs, files in os.walk(base_path):
        for directory in dirs:
            print(directory)
            # Check if the directory name matches the regex pattern
            if regex.match(directory):
                yield os.path.join(root, directory)
            print(directory)


# Usage example
if __name__ == "__main__":
    base_path = r"C:\PowerShell_Tests\engine"  # Change this to your base folder path
    pattern = r""  # Change this to your regex pattern

    matching_directories = filter_directories(base_path, pattern)
    count = 0
    for dir_path in matching_directories:

        print(dir_path)
        print(matching_directories)
        count = count + 1
        print(count)
