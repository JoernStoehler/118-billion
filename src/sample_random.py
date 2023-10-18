from human import Human
from typing import Dict
import random
import logging

def sample_random(human, var: str, dist: Dict[str, float]):
    if human.vars_stat.get(var) is not None:
        logging.info(f"Variable {var} already sampled.")
        return

    vals = list(dist.keys())
    odds = list(dist.values())
    value = random.choices(vals, weights=odds)[0]
    logging.info(f"Sampled value: {var}={value}")

    human.vars_stat[var] = value
    human.save()