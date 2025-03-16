import sys

"""Multiples of A and B

This script allows the user to read an input file containing sets of A, B and C where C is the limit of multiples of A and B. 
Finally the script creates an output file containing sets of all the natural numbers below C that are multiples of A and B.
"""

def main(input_file, output_file):
    """ Main logic for counting multiples of a text file and writing the result into another text file.
    
    Args:
        input_file (str/path): text file containing at least one row with three numbers.
        output_file (str/path): text file to input the outcome into

    Outcome:
        output_file (str/path): text file to input the outcome into
        results printed out on command line
    """
    input_text = read_input_file(input_file)
    rows = convert_str_to_list(input_text, "\n")
    output_list = create_output_list_with_multiples(rows)
    formatted_output = format_output(output_list)
    sorted_output = sort_output_lines(formatted_output)
    print(sorted_output)
    write_output_file(sorted_output, output_file)

def read_input_file(input_file):
    """Read given input file contents and return it.

    Args:
        input_file (str/path): text file containing at least one row with three numbers.

    Return:
        contents (str): contents of text file
    """
    with open(input_file) as f:
        contents = f.read()
        return contents
    
def convert_str_to_list(input, separator=" "):
    """Parse given input string into a list using given separator and return the list.
    
    Args:
        input (str): a string to be converted
        separator (str): separator to use when splitting the string, defaulted as space

    Return:
        input_list (list): result list of the splitted string
    """
    input_list = input.split(separator)
    return input_list

def create_output_list_with_multiples(rows):
    """Loop through given rows and count the multiples of each row. Append results into an output list and return that.
    
    Args:
        rows (list): list of rows with three numbers
        
    Return:
        output_list: list of numbers that counted as multiples
    """
    output_list = []
    for row in rows:
        row = convert_str_to_list(row)
        output_list.append(f"{row[2]}:")
        row_multiples_list = create_list_of_multiples(row[0], row[1], row[2])
        row_multiples_list = remove_duplicates_and_sort(row_multiples_list)
        output_list.append(row_multiples_list)
    return output_list

def create_list_of_multiples(A, B, C):
    """Create and return a list of multiples using given parameters.
    
    Args:
        A, B, C (str): numbers to use in counting multiples

    Return:
        multiple_list (list): list containing counted multiples for two number pairs
    """
    multiple_list = []
    multiple_list = count_multiples(A, C, multiple_list)
    multiple_list = count_multiples(B, C, multiple_list)
    return multiple_list

def count_multiples(multiple, limit, multiple_list):
    """Count the multiples with given limit and multiple and add those to given list that is returned when done.
    
    Args:
        multiple (str): the multiple number
        limit (str): the limit of multiples
        multiple_list (list): list of multiples

    Return:
        multiple_list (list): list of multiples with new multiples found
    """
    multiple = int(multiple)
    limit = int(limit)
    multiple_times = limit // multiple +1
    for i in range(1, multiple_times):
        multiple_list.append(i*multiple)
    return multiple_list

def remove_duplicates_and_sort(numbers):
    """Convert list to set and back to list again to remove duplicates and sort the list in ascending order.
    
    Args:
        numbers (list): list to be sorted
    
    Return: 
        list(set(numbers)) (list): sorted list without duplicates
    """
    return list(set(numbers))

def format_output(output_list):
    """Form given output list into a string following spesific formatting style desired and return the outcome.
    
    Args:
        output_list (list): list of multiple rows to be formatted

    Return:
        output_text (str): formatted output
    """
    output_text = ""
    for i in output_list:
        output_text += str(i)
        output_text = output_text.replace("]", "\n")
        output_text = output_text.replace("[", "")
    return output_text

def sort_output_lines(output):
    """Sort given output in ascending order by the number of multiples found the line and return the sorted outcome.
    
    Args:
        output (str): str containing rows to be sorted

    Return:
        sorted_output (str): sorted str output of multiples rows
    """
    lines = output.split("\n")
    sorted_lines = sorted(lines, key=number_of_separators)
    sorted_output = "\n".join(sorted_lines)
    return sorted_output

def number_of_separators(line):
    """Count and return the number of multiples on given line.
    
    Args:
        line (str): row of multiples

    Return:
        len(numbers) (int): length of the numbers on certain row
    """
    parts = line.split(":")
    numbers = parts[1].split(",") if len(parts) > 1 else []
    return len(numbers)

def write_output_file(output_text, output_file):
    """Write given text into a file.
    
    Args:
        output_text (str): text to be inputted into a file
        output_file (str/path): text file to input the outcome into
    """
    with open(output_file, "w") as f:
        f.write(output_text)
    
if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)