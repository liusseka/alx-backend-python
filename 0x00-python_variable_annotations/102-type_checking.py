#!/usr/bin/env python3
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Returns a zoomed version of the array."""
    zoomed_in: List = [item for item in lst for _ in range(factor)]
    return zoomed_in
