import jax.numpy as np
import numpyro.distributions as dist

from .constants import max_span_len, poisson_rate

def normalise_probs(a: np.ndarray) -> np.ndarray:
    return a / a.sum()

def generate_probs_list() -> list[list[float]]:
    probs_list = []

    poisson = dist.Poisson(rate=poisson_rate)
    probs = np.exp(poisson.log_prob(np.arange(max_span_len + 1)))

    probs_ = normalise_probs(probs)
    probs_list.append(probs_.cumsum().tolist())

    for i in range(max_span_len - 1):
        probs_ = normalise_probs(probs[:-i-1])
        probs_list.append(probs_.cumsum().tolist())

    return probs_list[::-1]
