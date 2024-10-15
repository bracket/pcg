from pcg.frozendict import frozendict

def test_frozendict():
    a = frozendict({'a': 1, 'b': 2})
    b = frozendict(a)
    c = frozendict({'b': 1, 'a': 2})

    assert a['a'] == 1
    assert a['b'] == 2
    assert a == {'a': 1, 'b': 2}

    assert a is not b
    assert a == b
    assert a != c


def test_frozendict_repr():
    a = frozendict({'a': 1, 'b': 2})
    assert repr(a) == "frozendict({'a': 1, 'b': 2})"
