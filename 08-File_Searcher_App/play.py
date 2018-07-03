
def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n-1)


print(f"5!={factorial(5)}, 3!={factorial(3)}, 11!={factorial(11):,}")


def fibonacci_co():
    current = 0
    next = 1

    while True:
        current, next = next, next + current
        yield current


for n in fibonacci_co():
    if n > 1000:
        break
    print(n, end=', ')
