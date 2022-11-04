# This file is public domain, it can be freely copied without restrictions.
# SPDX-License-Identifier: CC0-1.0


def voter_model(a: int, b: int, c: int) -> int:
    """model of voter 2 of 3"""
    r = 0
    if a == b:
        r = a
    elif a == c:
        r = a
    else:
        r = b
    return r
