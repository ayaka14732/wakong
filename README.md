# Python Implementation of the Wakong Algorithm

Wakong: An appropriate and robust masking algorithm for generating the training objective of text infilling

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
    mask_scheme = generate_mask_scheme(rng, seq_len=60)
    pretty_print_mask_scheme(mask_scheme)
```
