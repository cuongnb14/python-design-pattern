def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n - 1)


def memoize(fn, arg):
    memo = {}
    if arg not in memo:
        memo[arg] = fn(arg)
    return memo[arg]


def fac_m_f(n):
    return memoize(factorial, n)
