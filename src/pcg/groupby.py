def sum_groupby(seq, key=None):
    '''Iterate over sequence of pairs and sum second elements grouped by first elements

        Parameters:
            seq:
                Iterable[Tuple[Hashable, Any] | Any]

                Sequence of pairs to iterate over, or any sequence at all
                provided the key function is supplied.

            key:
                None | Callable

                If provided, seq may be an arbitrary sequence.  key will be
                applied to each element to determine the key to group on.

        Returns:
            Dict[Hashable, Any]

            Sums of elements grouped by key.
    '''

    seq = iter(seq)

    if key is not None:
        seq = ((key(x), x) for x in seq)

    out = { }

    for k, v in seq:
        accumulator = out.get(k)
        if accumulator is None:
            out[k] = v
        else:
            out[k] += v

    return out
