import jax; jax.config.update('jax_platforms', 'cpu')

from wakong._generate_probs_list import generate_probs_list

probs_list = generate_probs_list()

with open('src/wakong/probs_list.py', 'w', encoding='utf-8') as f:
    f.write(f'probs_list = {probs_list}\n')
