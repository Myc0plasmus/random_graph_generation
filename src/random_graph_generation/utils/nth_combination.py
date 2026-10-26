import math


from math import comb

def nth_combination(values, k, i):
    n = len(values)

    if not 0 <= k <= n:
        raise ValueError("k must be between 0 and len(values)")

    total = comb(n, k)

    if not 0 <= i < total:
        raise IndexError("combination index out of range")

    result = []

    start = 0

    for pos in range(k):
        remaining = k - pos - 1

        # Number of combinations available from this position onward.

        total_here = comb(n - start, remaining + 1)

        lo = start

        hi = n - remaining - 1

        # Find the first x such that i belongs to x's block.

        while lo < hi:
            mid = (lo + hi) // 2

            # Number of combinations before those beginning with `mid`.

            before = total_here - comb(n - mid, remaining + 1)

            # Number beginning with `mid`.

            block = comb(n - mid - 1, remaining)

            if i < before:
                hi = mid - 1

            elif i < before + block:
                hi = mid

            else:
                lo = mid + 1

        x = lo

        # Remove combinations belonging to earlier choices.

        before = total_here - comb(n - x, remaining + 1)

        i -= before

        result.append(values[x])

        start = x + 1

    return tuple(result)

