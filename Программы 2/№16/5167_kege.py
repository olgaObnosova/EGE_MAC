def f(n):
    if n >= 10_000:
        return n
    elif n % 2 == 0:
        return f(n + 2) + 3
    else:
        return f(n + 2) + 1


print(f(94) + f(80))
