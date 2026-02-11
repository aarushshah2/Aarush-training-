from functools import reduce, lru_cache, partial

# reduce - Aggregate a list
print(reduce(lambda x, y: x + y, [1, 2, 3, 4])) # 10

# lru_cache - Memoization for performance
@lru_cache(maxsize=None)
def fib(n):
    return n if n < 2 else fib(n-1) + fib(n-2)

# partial - Pre-fill function arguments
int2 = partial(int, base=2)
print(int2('101')) # 5