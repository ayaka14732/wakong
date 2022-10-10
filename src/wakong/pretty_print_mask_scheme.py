from .generate_mask_scheme import MaskScheme

def pretty_print_mask_scheme(seq_len: int, mask_scheme: MaskScheme) -> None:
    x = ['.'] * seq_len

    for insert_pos, span in mask_scheme:
        for i in range(insert_pos, insert_pos + span):
            x[i] = 'x'

    offset = 0
    for insert_pos, span in mask_scheme:
        x.insert(insert_pos + offset, '(')
        offset += 1
        x.insert(insert_pos + span + offset, ')')
        offset += 1

    print(''.join(x))
