
def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n-1)


print(f"5!={factorial(5)}, 3!={factorial(3)}, 11!={factorial(11):,}")