from functools import cached_property

class frozendict:
    def __init__(self, d):
        self.d = dict(d)


    @cached_property
    def hash(self):
        return hash(frozenset(self.items()))


    def keys(self):
        return self.d.keys()

    
    def values(self):
        return self.d.values()


    def items(self):
        return self.d.items()


    def __repr__(self):
        return f"frozendict({repr(self.d)})"


    def __str__(self):
        return repr(self)


    def __eq__(self, other):
        if isinstance(other, frozendict):
            return self.d == other.d
        else:
            return self.d == other


    def __getitem__(self, key):
        return self.d[key]


    def __hash__(self):
        return self.hash
