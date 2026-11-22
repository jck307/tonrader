from tonrader import *

def formula(row):
    # play around with this!
    row = row.cycle(1)
    row = row.part(2, 0).merge(row.part(2, 1), "ba")
    row = row.ri()
    return row

RESET = '\x1b[0m'
BG_RGB = '\x1b[48;2;{};{};{}m'
FG_BLACK = '\x1b[30m'
BOLD = '\x1b[1m'
TEXT_STYLE = FG_BLACK + BOLD
CONTRAST = 18
MAX_ROWS = 500

MODULUS = 12
INITIAL_ROW = Row(0, 8, 5, 1, 6, 3, 10, 2, 7, 9, 4, 11)

# MODULUS = 6
# INITIAL_ROW = Row(0, 1, 2, 3, 4, 5, modulus=MODULUS)

def print_row(row):
    missing = set(range(MODULUS)) ^ set(row)
    if len(missing) != 0:
        missing = f"(missing {len(missing)}: " + ", ".join(str(i) for i in missing) + ")"
    else:
        missing = ""
    print("".join([
        f"{BG_RGB}{TEXT_STYLE} {i:>2} ".format(
            255-CONTRAST*i*(12//MODULUS),
            255-CONTRAST*i*(12//MODULUS),
            255
        ) for i in row
    ]) + RESET, missing)

row = INITIAL_ROW
rows = [row]

while len(rows) < MAX_ROWS:
    print_row(row)
    row = formula(row)
    if row in rows:
        break
    rows.append(row)

print_row(row)
print("\nfound", len(rows), "rows.")

if 0:
    # extra info

    print("note frequencies:")
    for i in range(12):
        occurences = 0
        for row in rows:
            occurences += row.count(i)
        perc = occurences / (12 * len(rows)) * 100
        print(f"    {i:>2}: {occurences} ({perc:.0f}%)")

    print("\nvalid rows:")
    for row in rows:
        if row.valid():
            print(f"    {row}")

