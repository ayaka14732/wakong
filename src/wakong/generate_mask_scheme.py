from random import Random

from .constants import proposed_mask_rate, max_span_len
from .probs_list import probs_list

MaskScheme = list[tuple[int, int]]

def determine_should_mask_len(rng: Random, seq_len: int) -> int:
    x = seq_len * proposed_mask_rate
    integer_part = int(x)
    fractional_part = x - float(integer_part)
    should_add = rng.random() < fractional_part
    should_mask_len = integer_part + should_add
    return should_mask_len

def generate_spans(rng: Random, should_mask_len: int) -> list[int]:
    spans = []
    while should_mask_len > 0:
        current_max_span_len = min(max_span_len, should_mask_len)
        probs = probs_list[current_max_span_len - 1]
        span_len = rng.choices(range(current_max_span_len + 1), cum_weights=probs)[0]
        spans.append(span_len)
        should_mask_len -= span_len + 1
    rng.shuffle(spans)
    return spans

def distribute_insert_poses(abs_insert_poses: list[int], spans: list[int]) -> MaskScheme:
    offset = 0
    mask_scheme = []
    for abs_insert_pos, span in zip(abs_insert_poses, spans):
        insert_pos = abs_insert_pos + offset
        mask_scheme.append((insert_pos, span))
        offset += span + 1
    return mask_scheme

def random_add_one(rng: Random, mask_scheme: MaskScheme) -> MaskScheme:
    should_add_one = rng.random() < 0.5
    if should_add_one:
        mask_scheme = [(insert_pos + 1, span) for insert_pos, span in mask_scheme]
    return mask_scheme

def generate_mask_scheme(rng: Random, seq_len: int) -> MaskScheme:
    should_mask_len = determine_should_mask_len(rng, seq_len)
    spans = generate_spans(rng, should_mask_len)

    n_spans = len(spans)
    n_possible_insert_poses = seq_len - sum(spans) - n_spans + 1
    abs_insert_poses = sorted(rng.sample(range(n_possible_insert_poses), n_spans))

    mask_scheme = distribute_insert_poses(abs_insert_poses, spans)
    mask_scheme = random_add_one(rng, mask_scheme)
    return mask_scheme
