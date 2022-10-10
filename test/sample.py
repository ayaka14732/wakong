from random import Random
from wakong import generate_mask_scheme, pretty_print_mask_scheme

seed = 42
rng = Random(seed)

for _ in range(5):
    mask_scheme = generate_mask_scheme(rng, seq_len=60)
    pretty_print_mask_scheme(mask_scheme)
