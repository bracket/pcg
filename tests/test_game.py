from pcg import Game, Distribution
from pcg.common import zero, one


def test_game_instantiate():
    g = Game()


def test_game_le():
    assert zero() <= one()
    assert not one() <= zero()
    assert one() <= one()


def test_game_add():
    assert one() + zero() == one()


def test_game_repr():
    assert repr(Game()) == 'Game((), ())'


def test_distribution_instantiate():
    d = Distribution([(Game(), 1)])


def test_distribution_repr():
    d = Distribution([(Game(), 1)])
    assert repr(d) == 'Distribution([(Game((), ()), 1)])'
