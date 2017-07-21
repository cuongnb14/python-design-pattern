def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n - 1)


memo = {}


def factorial_memo(n):
    if n < 2:
        return 1
    if n not in memo:
        memo[n] = n * factorial(n - 1)
    return memo[n]


print(factorial(3))
print(factorial(4))