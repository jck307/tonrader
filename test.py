from tonrader import *
from run_formula import run_formula

modulus = 12
initial_row = Row(0, 8, 5, 1, 6, 3, 10, 2, 7, 9, 4, 11)

# modulus = 6
# initial_row = Row(0, 1, 2, 3, 4, 5, modulus=modulus)

def formula(row):
    # play around with this!
    row = row.rotate(1) * 2
    row = row.part(2, 0).merge(row.part(2, 1) + 1, "ba")
    row = row.i()
    return row

run_formula(formula, initial_row, extra_info=True)

