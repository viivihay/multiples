"""Multiples of A and B

This script allows the user to read an input file containing of A, B and C where C is the limit of multiples of A and B. 
Finally the script creates an output file containing all the natural numbers below C that are multiples of A and B.
"""

def main():
    input = read_input_file("input.txt")
    output_list = []
    case_list = input_to_list(input, "\n")
    for case in case_list:
        case = input_to_list(case)
        output_list.append(f"{case[2]}:")
        case_multiples_list = multiples(case[0], case[1], case[2])
        output_list.append(case_multiples_list)
    formatted_output = form_output(output_list)
    sorted_output = sort_output(formatted_output)
    print(sorted_output)
    write_output_file(sorted_output, "output.txt")

def multiples(A, B, C):
    factor_list = []
    factor_list = count_multiples(A, C, factor_list)
    factor_list = count_multiples(B, C, factor_list)
    return factor_list

def count_multiples(factor, limit, factor_list):
    """Count the multiples with given limit and factor and add those to given list that is returned when done."""
    factor = int(factor)
    limit = int(limit)
    multiple_times = limit // factor +1
    for i in range(1, multiple_times):
        factor_list.append(i*factor)
    return factor_list

def read_input_file(input_file):
    """Read given input file contents and return it."""
    with open(input_file) as f:
        contents = f.read()
        return contents
    
def input_to_list(input, separator=" "):
    """Parse given input string into a list using given separator and return the list."""
    input_list = input.split(separator)
    return input_list

def sort_output(output):
    lines = output.split("\n")
    sorted_lines = sorted(lines, key=number_of_separators)
    sorted_output = "\n".join(sorted_lines)
    return sorted_output

def number_of_separators(line):
    parts = line.split(":")
    numbers = parts[1].split(",") if len(parts) > 1 else []
    return len(numbers)

def form_output(output_list):
    output_text = ""
    for i in output_list:
        output_text += str(i)
        output_text = output_text.replace("]", "\n")
        output_text = output_text.replace("[", "")
    return output_text

def write_output_file(output_text, output_file):
    with open(output_file, "w") as f:
        f.write(output_text)
    
if __name__ == "__main__":
    main()