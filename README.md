# The Wakong Algorithm and Its Python Implementation

Wakong: An appropriate and robust masking algorithm for generating the training objective of text infilling

## Motivation

TODO

## Installation

Wakong supports Python 3.10 and above:

```sh
pip install wakong
```

## Usage

```python
from random import Random
from wakong import generate_mask_scheme, pretty_print_mask_scheme

seed = 42
rng = Random(seed)

for _ in range(5):
    seq_len = 60
    mask_scheme = generate_mask_scheme(rng, seq_len)
    pretty_print_mask_scheme(seq_len, mask_scheme)
```

Output:

```
..(xx)..(xxx)....(xx).........(x)...................................
..............(xxxx)...............(xxxxx)......................
..........().....(xxx)....................................(xxxxxx)
........(xx)..................(xxxxxx)...........(xx).............
............(xxxxx).........................(xxxxx).............
```

`.` stands for non-masked tokens, while `(xxx)` stands for substituting 3 tokens to a single mask token.
