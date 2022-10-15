# Wakong

Wakong: An appropriate and robust masking algorithm for generating the training objective of text infilling

This project is the Python library of ARP 1: [_The Wakong Algorithm and Its Python Implementation_](https://arp.shn.hk/1/).

This project is supported by Cloud TPUs from Google's [TPU Research Cloud](https://sites.research.google/trc/about/) (TRC) as a part of my project on large-scale language model pre-training.

## Installation

Wakong supports Python 3.10 and above:

```sh
pip install wakong
```

You can also install from source:

```sh
flit install
```

## Usage

```python
from wakong import Wakong
wakong = Wakong(seed=42)
sentence = 'I can eat glass , it does not hurt me .'.split(' ')
print(wakong(sentence))
```

Output:

```
['I', '<mask>', 'eat', 'glass', '<mask>', ',', 'it', 'does', 'not', 'hurt', 'me', '.']
```
