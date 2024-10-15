from pcg import Game, Distribution

def test_game():
    g = Game()
    print(g)


def test_game_repr():
    assert repr(Game()) == 'Game((), ())'
