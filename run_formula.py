from tonrader import *

RESET = '\x1b[0m'
BG_RGB = '\x1b[48;2;{};{};{}m'
FG_BLACK = '\x1b[30m'
BOLD = '\x1b[1m'
TEXT_STYLE = FG_BLACK + BOLD
CONTRAST = 18
MAX_ROWS = 500

def print_row(row):
    missing = set(range(row.modulus)) ^ set(row)
    if len(missing) != 0:
        missing = f"(missing {len(missing)}: " + ", ".join(str(i) for i in missing) + ")"
    else:
        missing = ""
    print("".join([
        f"{BG_RGB}{TEXT_STYLE} {i:>2} ".format(
            255-CONTRAST*i*(12//row.modulus),
            255-CONTRAST*i*(12//row.modulus),
            255
        ) for i in row
    ]) + RESET, missing)

def run_formula(formula, initial_row, extra_info=False):
    row = initial_row
    rows = [row]

    while len(rows) < MAX_ROWS:
        print_row(row)
        row = formula(row)
        if row in rows:
            break
        rows.append(row)

    print_row(row)
    print("found", len(rows), "rows.")

    repeated_row = row

    if extra_info:
        print("note frequencies:")
        for i in range(row.modulus):
            occurences = 0
            for row in rows:
                occurences += row.count(i)
            perc = occurences / (row.modulus * len(rows)) * 100
            print(f"    {i:>2}: {occurences} ({perc:.0f}%)")

        # print("\nvalid rows:")
        # for row in rows:
        #     if row.valid():
        #         print(f"    {row}")

    return repeated_row

