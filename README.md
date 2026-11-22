# tonrader

Experiment with generating tone rows in Python, Boulez-style. Has support for standard Shoenberg-operations (R, I, RI, T), multiplication, and what I call splitting / merging (dividing a row into n parts, and then joining those parts according to a pattern).

The class `Row` must not represent a tone row. Simply change the `modulus` value to whatever amount of values it should be able to represent. For example, a value of 5 could represent rythm, using 0 as a whole note, 1 as a half and 4 as a sixteenth.

See `test.py` for an example, that recursively applies a given formula on an initial tone row, until it stumbles upon a row that has already been discovered.
