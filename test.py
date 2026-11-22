from tonrader import *
from run_formula import run_formula

modulus = 12
row = Row(0, 8, 5, 1, 6, 3, 10, 2, 7, 9, 4, 11)

def formula(row):
    # play around with this!

    row = row.rotate(1)
    row = row.part(2, 0).merge(row.part(2, 1), "ba")
    row = row.ri()

    return row

row = run_formula(formula, row, extra_info=False)

