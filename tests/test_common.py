from pcg.common import *

def test_zero():
    z = zero()
    assert not z.left_options
    assert not z.right_options


def test_one():
    o = one()

    [ z ] = o.left_options
    assert z == zero()
