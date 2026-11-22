class Row:
    def __init__(self, *indexes, modulus=12):
        for i in indexes:
            assert type(i) is int
        self.indexes = indexes
        self.modulus = modulus

    def derive(self, indexes):
        return __class__(*indexes, modulus=self.modulus)

    def __len__(self):
        return len(self.indexes)

    def __mul__(self, factor):
        return self.derive([(i * factor) % self.modulus for i in self.indexes])

    def __add__(self, rhs):
        if type(rhs) is int:
            return self.derive([(i + rhs) % self.modulus for i in self.indexes])
        elif type(rhs) is __class__:
            return self.join(rhs)
        else:
            raise TypeError

    def __repr__(self):
        return "ToneRow(" + ", ".join([str(i) for i in self.indexes]) + ")"

    def __getitem__(self, i):
        return self.indexes[i]

    def __eq__(self, other):
        return self.indexes == other.indexes

    def count(self, n):
        return self.indexes.count(n)

    def valid(self):
        for i in range(self.modulus):
            if i not in self.indexes:
                return False
        return len(self) == self.modulus

    def r(self):
        # retrograde
        return self.derive(reversed(self.indexes))

    def i(self):
        # inversion
        return self.derive([self.modulus-1-i for i in self.indexes])

    def ri(self):
        # retrograde inversion
        return self.r().i()

    def cycle(self, count):
        count = count % len(self)
        return self.derive((self.indexes[len(self)-count:] + self.indexes[:len(self)-count]))

    def normalize(self):
        return self + (-self[0])

    def join(self, other):
        return self.derive((self.indexes + other.indexes))

    def merge(self, other, mode):
        assert len(self) == len(other)
        assert (len(self) * 2) % len(mode) == 0
        assert set(list(mode)) == {"a", "b"}
        assert mode.count("a") == mode.count("b")
        result = []
        self_i = 0
        other_i = 0
        for i in range(len(self)*2):
            match mode[i%len(mode)]:
                case "a":
                    result.append(self[self_i])
                    self_i += 1
                case "b":
                    result.append(other[other_i])
                    other_i += 1
        return self.derive(result)

    def split(self, divisions):
        parts = []
        for i in range(divisions):
            parts.append(self.part(divisions, i))
        return parts

    def part(self, divisions, n):
        assert len(self) % divisions == 0
        part_len = int(len(self) / divisions)
        start = n*part_len
        return self.derive(self.indexes[start:start+part_len])

