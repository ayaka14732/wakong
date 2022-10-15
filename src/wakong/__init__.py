'''Wakong: An appropriate and robust masking algorithm for generating the training objective of text infilling.'''

__version__ = '1.1.0'

from .generate_mask_scheme import MaskScheme, generate_mask_scheme
from .pretty_print_mask_scheme import pretty_print_mask_scheme
from .apply_mask_scheme import apply_mask_scheme
from .Wakong import Wakong
