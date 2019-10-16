# Read a full line of input from stdin and save it to our dynamically typed variable, input_string.

import sys

old_stdin = sys.stdin
sys.stdin = open("input")

input_string = input()

print(input_string)
# Print a string literal saying "Hello, World." to stdout.
print('Hello, World.')

# TODO: Write a line of code here that prints the contents of input_string to stdout.

