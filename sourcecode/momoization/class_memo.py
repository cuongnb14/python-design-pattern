def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n - 1)


class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]


fac = Memoize(factorial)
print(fac(1))
print(fac(2))


@Memoize
def factorial_d(n):
    if n < 2:
        return 1
    return n * factorial(n - 1)


print(factorial_d(1))
print(factorial_d(2))
