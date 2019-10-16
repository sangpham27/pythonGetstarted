# Read a full line of input from stdin and save it to our dynamically typed variable, input_string.

import sys
sys.stdin = open("input")

meal_cost = int(input())
tip_percent = int(input())
tax_percent = int(input())

tip = meal_cost * (tip_percent/100)
tax = meal_cost * (tax_percent/100)

totalCost = meal_cost + tip + tax

print(round(int(totalCost)))




