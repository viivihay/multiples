import sys

"""Multiples of A and B

This script allows the user to read an input file containing sets of A, B and C where C is the limit of multiples of A and B. 
Finally the script creates an output file containing sets of all the natural numbers below C that are multiples of A and B.
"""

def main(input_file, output_file):
    input_text = read_input_file(input_file)
    rows = input_to_list(input_text, "\n")
    output_list = create_output_list_with_multiples(rows)
    formatted_output = form_output(output_list)
    sorted_output = sort_output_lines(formatted_output)
    print(sorted_output)
    write_output_file(sorted_output, output_file)

def read_input_file(input_file):
    """Read given input file contents and return it."""
    with open(input_file) as f:
        contents = f.read()
        return contents
    
def input_to_list(input, separator=" "):
    """Parse given input string into a list using given separator and return the list."""
    input_list = input.split(separator)
    return input_list

def create_output_list_with_multiples(rows):
    """Loop through given rows and count the multiples of each row. Append results into an output list and return that."""
    output_list = []
    for row in rows:
        row = input_to_list(row)
        output_list.append(f"{row[2]}:")
        row_multiples_list = create_multiple_list(row[0], row[1], row[2])
        row_multiples_list = remove_duplicates_and_sort(row_multiples_list)
        output_list.append(row_multiples_list)
    return output_list

def create_multiple_list(A, B, C):
    """Create and return a list of multiples using given parameters."""
    multiple_list = []
    multiple_list = count_multiples(A, C, multiple_list)
    multiple_list = count_multiples(B, C, multiple_list)
    return multiple_list

def count_multiples(multiple, limit, multiple_list):
    """Count the multiples with given limit and multiple and add those to given list that is returned when done."""
    multiple = int(multiple)
    limit = int(limit)
    multiple_times = limit // multiple +1
    for i in range(1, multiple_times):
        multiple_list.append(i*multiple)
    return multiple_list

def remove_duplicates_and_sort(numbers):
    """Convert list to set and back to list again to remove duplicates and sort the list ascending."""
    return list(set(numbers))

def form_output(output_list):
    """Form given output list into a string following spesific formatting style desired and return the outcome."""
    output_text = ""
    for i in output_list:
        output_text += str(i)
        output_text = output_text.replace("]", "\n")
        output_text = output_text.replace("[", "")
    return output_text

def sort_output_lines(output):
    """Sort given output ascending by the number of multiples found the line and return the sorted outcome."""
    lines = output.split("\n")
    sorted_lines = sorted(lines, key=number_of_separators)
    sorted_output = "\n".join(sorted_lines)
    return sorted_output

def number_of_separators(line):
    """Count and return the number of multiples on given line."""
    parts = line.split(":")
    numbers = parts[1].split(",") if len(parts) > 1 else []
    return len(numbers)

def write_output_file(output_text, output_file):
    """Write given text into a file."""
    with open(output_file, "w") as f:
        f.write(output_text)
    
if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)