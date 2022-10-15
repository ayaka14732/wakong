def apply_mask_scheme(words: list[str], mask_scheme: list[tuple[int, int]], mask_token: str='<mask>') -> list[str]:
    '''
    ```python
    >>> words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    >>> mask_scheme = [(0, 0), (1, 3), (6, 1), (8, 0)]
    >>> apply_mask_scheme(words, mask_scheme)
    ['<mask>', 'a', '<mask>', 'e', 'f', '<mask>', 'h', '<mask>']
    ```
    '''

    if not mask_scheme:
        return words

    res = []

    next_word_pos = 0
    it = iter(mask_scheme)
    insert_pos, span = next(it)

    while next_word_pos < len(words):
        if next_word_pos == insert_pos:
            res.append(mask_token)
            next_word_pos += span
            try:
                insert_pos, span = next(it)
            except StopIteration:
                insert_pos = -1
        else:
            res.append(words[next_word_pos])
            next_word_pos += 1

    # final check
    if next_word_pos == insert_pos:
        res.append(mask_token)

    return res
