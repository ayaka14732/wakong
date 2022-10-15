from random import Random

from .generate_mask_scheme import generate_mask_scheme
from .apply_mask_scheme import apply_mask_scheme

class Wakong:
    def __init__(self, seed) -> None:
        self.rng = Random(seed)

    def __call__(self, words: list[str], mask_token: str='<mask>') -> list[str]:
        seq_len = len(words)
        mask_scheme = generate_mask_scheme(self.rng, seq_len)
        res = apply_mask_scheme(words, mask_scheme, mask_token=mask_token)
        return res
