import jax; jax.config.update('jax_platforms', 'cpu')
import jax.numpy as np
import random

from wakong import generate_mask_scheme, pretty_print_mask_scheme

# internal functions for testing
from wakong.generate_mask_scheme import *
from wakong._generate_probs_list import normalise_probs

seed = r'''
                  _oo0oo_
                 o8888888o
                 88" . "88
                 (| -_- |)
                 0\  =  /0
               ___/`---'\___
             .' \\|     | '.
            / \\|||  :  ||| \
           / _||||| -:- |||||- \
          |   | \\\  -  / |   |
          | \_|  ''\---/''  |_/ |
          \  .-\__  '-'  ___/-. /
        ___'. .'  /--.--\  `. .'___
     ."" '<  `.___\_<|>_/___.' >' "".
    | | :  `- \`.;`\ _ /`;.`/ - ` : | |
    \  \ `_.   \_ __\ /__ _/   .-` /  /
=====`-.____`.___ \_____/___.-`___.-'=====
                  `=---='
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
         佛祖保佑         永無 BUG
'''

def pretty_print_array(a: np.ndarray) -> str:
    return f'[{", ".join(map(lambda x: f"{x:.4f}", a))}]'

def undo_cumsum(a: np.ndarray) -> np.ndarray:
    return np.diff(a, prepend=0.)

def test():
    rng = random.Random(seed)
    rng_ = random.Random(42)

    total_seq_len = 0
    total_mask_len = 0
    span_lens = [0] * (max_span_len + 1)

    for _ in range(200000):
        seq_len = rng_.randrange(2, 256)
        mask_scheme = generate_mask_scheme(rng, seq_len)

        print(mask_scheme)
        pretty_print_mask_scheme(seq_len, mask_scheme)

        mask_len = sum(span for _, span in mask_scheme)
        total_seq_len += seq_len
        total_mask_len += mask_len
        for _, span in mask_scheme:
            span_lens[span] += 1

    print(f'Proposed mask rate: {proposed_mask_rate:.2%}')
    print(f'Resulting mask rate: {total_mask_len / total_seq_len:.2%}')
    print(f'Proposed span length distribution: {pretty_print_array(undo_cumsum(np.array(probs_list[-1])))}')
    print(f'Resulting span length distribution: {pretty_print_array(normalise_probs(np.array(span_lens)))}')

if __name__ == '__main__':
    test()
