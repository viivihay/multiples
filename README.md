# Multiples

## Multiples of A and B

A program that takes a file as the first command line argument. The file content has to be list of
numbers, with 3 numbers per row separated by space and number of rows is undefined (can
be something between 1 - infinite). First number in a row is A and the second is B, third one is
the goal number. The program searches all multiples of A and B which
are below the third number, prints them out to screen and also writes results to file which was given
as the second command line argument.
Program sorts out output file by ascending order how many multiples certain row has.

---

### Example usage:

Input file (input.txt):

> 1 8 31  
> 4 7 20  
> 3 9 15

Command line command:  
`python multiples.py "input.txt" "output.txt"`

Command line output and output file:

> 15:3, 6, 9, 12, 15  
> 20:4, 7, 8, 12, 14, 16, 20  
> 31:1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31
