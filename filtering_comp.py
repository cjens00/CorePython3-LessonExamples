# Filtering Comprehensions
# All three comprehensions allow for a filtering clause
from math import sqrt


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


# Prime Square Divisors
# Maps numbers with exactly three divisors to tuple of divisors
psd = {x*x: (1, x, x*x) for x in range(2000) if is_prime(x)}
[print(x) for x in psd.items()]
