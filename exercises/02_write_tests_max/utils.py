from typing import Iterable, Optional, Union

Number = Union[int, float]

def find_max(values: Iterable[Number]) -> Optional[Number]:
    """
    Return the largest number in `values`.
    - If `values` is empty, return None.
    - Accept ints and floats. Raise TypeError if a non-number is present.

    Examples:
      find_max([1, 2, 3]) -> 3
      find_max([]) -> None
    """
    iterator = iter(values)
    try:
        first = next(iterator)
    except StopIteration:
        return None

    if not isinstance(first, (int, float)):
        raise TypeError("Non-numeric value detected")

    current_max: Number = first
    for v in iterator:
        if not isinstance(v, (int, float)):
            raise TypeError("Non-numeric value detected")
        if v > current_max:
            current_max = v
    return current_max
