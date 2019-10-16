# Read a full line of input from stdin and save it to our dynamically typed variable, input_string.

import sys
sys.stdin = open("input")

s1 = input()
s2 = input()
s3 = input()

i = 4
d = 4.0
s = "is the best place to learn and practice coding!"

print(f't1 = {i + int(s1)}')
print(f't2 = {d + float(s2)}')
print(f't2 = {s + s3}')

