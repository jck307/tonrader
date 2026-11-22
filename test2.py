from tonrader import *
from run_formula import run_formula

modulus = 6
row = Row(0, 1, 2, 3, 4, 5, modulus=modulus)

def formula(row):
    row *= 2
    row = row.part(2, 0).merge(row.part(2, 1) + 1, "ba")
    return row

for _ in range(3):
    print("running...")
    row = run_formula(formula, row, extra_info=True)
    row = row.i().normalize()

