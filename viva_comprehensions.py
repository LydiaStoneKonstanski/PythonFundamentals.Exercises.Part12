from typing import List, Dict, Set, Callable
import enum


class Parity(enum.Enum):
    # Integers based on modulus
    ODD = 1
    EVEN = 0


def gen_list(start: int, stop: int, parity: Parity) -> List[int]:
    return [i for i in range(start, stop) if i % 2 == parity.value]


def gen_dict(start: int, stop: int, strategy: Callable) -> Dict:
    return {i : strategy(i) for i in range(start, stop)}


def gen_set(val_in: str) -> Set:
    # This is the longform logic
    # krisYouDirtyDog = set()
    # for letter in val_in:
    #     if letter.islower():
    #         krisYouDirtyDog.add(letter.upper())

    # This is same logic using comprehension
    krisYouDirtyDog = set([letter.upper() for letter in val_in if letter.islower()])
    return krisYouDirtyDog

