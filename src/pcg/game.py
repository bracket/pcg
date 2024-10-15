from .errors import PCGError
from .frozendict import frozendict
from .groupby import sum_groupby
from functools import cached_property
from itertools import chain


class Game:
    def __init__(self, left_options=(), right_options=()):
        if not isinstance(left_options, tuple):
            left_options = tuple(left_options)

        if not isinstance(right_options, tuple):
            right_options = tuple(right_options)

        self.left_options = left_options
        self.right_options = right_options


    @cached_property
    def game(self):
        return self


    @cached_property
    def distribution(self):
        return Distribution(((self, 1)))


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
    def ccg(self):
        left_options = tuple(d.ccg for d in self.left_options)

        if any(o is None for o in left_options):
            return None

        right_options = tuple(d.ccg for d in self.right_options)

        if any(o is None for o in right_options):
            return None

        return self


    @cached_property
    def hash(self):
        return hash((Game, self.left_options, self.right_options))


    @cached_property
    def negative(self):
        return Game(
            (-r for r in self.right_options),
            (-l for l in self.left_options)
        )


    def __hash__(self):
        return self.hash


    def __repr__(self):
        return f"Game({repr(self.left_options)}, {repr(self.right_options)})"


    def __add__(self, other):
        if isinstance(other, Distribution):
            return self.distribution + other
        elif isinstance(other, Game):
            return Game(
                chain(
                    (l + other for l in self.left_options),
                    (self + l for l in other.left_options)
                ),
                chain(
                    (r + other for r in self.right_options),
                    (other + r for r in other.right_options)
                )
            )

        raise PCGError(f"Cannot add Game and {type(other)}")


    def __sub__(self, other):
        return self + (-other)


    def __neg__(self):
        return self.negative


    def __le__(self, other):
        if isinstance(other, Game):
            if any(other <= l for l in self.left_options):
                return False

            if any(r <= self for r in other.right_options):
                return False

            return True
        elif isinstance(other, Distribution):
            o = other.ccg

            if o is None:
                return False

            return self <= o

        raise PCGError(f"Cannot compare Game and {type(other)}")


    def __eq__(self, other):
        return self <= other and other <= self


class Distribution:
    def __init__(self, options):
        if not isinstance(options, frozendict):
            options = frozendict(options)

        if not options:
            raise PCGError("Distribution must have at least one option")

        if sum(options.values()) != 1:
            raise PCGError("Distribution options must sum to 1")

        self.options = options


    @cached_property
    def game(self):
        try:
            [ (o, p) ] = self.options.items()
            return o.game
        except ValueError:
            return None


    @cached_property
    def distribution(self):
        return self


    @cached_property
    def left_probability(self):
        return sum(p * o.left_probablity for o, p in self.options.items())


    @cached_property
    def right_probability(self):
        return sum(p * o.right_probability for o, p in self.options.items())


    @cached_property
    def ccg(self):
        game = self.game

        if game is None:
            return None

        return game.ccg


    @cached_property
    def negative(self):
        return Distribution((-o, p) for o, p in self.options.items())


    def items(self):
        return self.options.items()


    @cached_property
    def hash(self):
        return hash((Distribution, self.options))


    def __hash__(self):
        return self.hash


    def __repr__(self):
        return f"Distribution({repr(list(self.options.items()))})"


    def __add__(self, other):
        return Distribution(
            sum_groupby(
                (s + o, p * q)
                for s, p in self.distribution.items()
                for o, q in other.distribution.items()
            )
        )


    def __sub__(self, other):
        return self + (-other)

    
    def __neg__(self):
        return self.negative


    def __le__(self, other):
        if isinstance(other, Game):
            pass


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
