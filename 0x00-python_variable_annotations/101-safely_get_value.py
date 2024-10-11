#!/usr/bin/env python3
from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any, default: Union[T, None]
                     = None) -> Union[Any, T]:
    """Returns the value for a key in a dictionary or a default value."""
    return dct.get(key, default)
