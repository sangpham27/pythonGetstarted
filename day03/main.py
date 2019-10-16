# Read a full line of input from stdin and save it to our dynamically typed variable, input_string.

import sys
sys.stdin = open("input")

n = int(input())
if n%2 != 0:    print('Weird')
elif 2 < n < 5: print('Not Weird')
elif 6 < n <= 20: print('Weird')
elif n > 20 :   print('Not Weird')



