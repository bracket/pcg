from .errors import PCError
from .frozendict import frozendict
from functools import cached_property


class Game:
    def __init__(self, left_options=(), right_options=()):
        self.left_options = left_options
        self.right_options = right_options
    

    @cached_property
    def left_probability(self):
        if self.left_options:
            return max(d.right_probability for d in self.left_options)
        else:
            return 0


    @cached_property
    def right_probability(self):
        if self.right_options:
            return min(d.left_probability for d in self.right_options)
        else:
            return 1


    @cached_property
    def hash(self):
        return hash((Game, self.left_options, self.right_options))


    def __hash__(self):
        return self.hash


    def __repr__(self):
        return f"Game({repr(self.left_options)}, {repr(self.right_options)})"


class Distribution:
    def __init__(self, options):
        if not options:
            raise PCGError("Distribution must have at least one option")

        self.options = frozendict(options)


    @cached_property
    def left_probability(self):
        return sum(p * o.left_probablity for o, p in self.options.items())


    @cached_property
    def right_probability(self):
        return sum(p * o.right_probability for o, p in self.options.items())


    @cached_property
    def hash(self):
        return hash((Distribution, self.options))


    def __hash__(self):
        return self.hash


class Dyadic(Game):
    def __init__(self, m, n):
        self.m = m
        self.n = n


    @property
    def left_options(self):
        return ()


    @property
    def right_options(self):
        return ()
