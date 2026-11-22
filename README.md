# tonrader

Experiment with generating tone rows in Python, Boulez-style. Has support for standard Shoenberg-operations (R, I, RI, T), multiplication, and what I call splitting / merging (dividing a row into n parts, and then joining those parts according to a pattern).

See `test.py` for an example, that recursively applies a given formula on an initial tone row, until it stumbles upon a row that has already been discovered.
