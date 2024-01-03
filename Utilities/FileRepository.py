import os

def read_file_lines(filename):
    # Validate that the file name is valid
    if not os.path.isfile(filename):
        raise Exception(f"{filename} does not exist")

    # Read each line of the file and add it to a collection of strings
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Return the collection of strings
    return lines