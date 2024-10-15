__all__ = [
    'flip_distribution',
    'flip_game',
    'half',
    'one',
    'zero',
]

from .game import Game, Distribution

def zero():
    return Game()


def one():
    return Game((zero(),))


def half():
    return Game((zero(),), (one(),))


def flip_distribution(p, G):
    return Distribution([(G, p), (-G, 1 - p)])


def flip_game(p, G):
    d = flip_distribution(p, G)
    return Game((d,), (-d,))
