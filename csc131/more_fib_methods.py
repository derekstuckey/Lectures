def fib_memoization(n: int, lookup: dict) -> int:               # top bottom momoization
    if n < 1:
        return -1
    # base case
    elif n == 1 or n == 2:
        lookup[n] = 1

    elif lookup.get(n, None) is None:
        lookup[n] = fib_memoization(n - 1, lookup) + fib_memoization(n - 2, lookup)
        return lookup


def fib_tab(n: int) -> int:                                     # bottom up tabulation
    f = [0] * (n+1)

    # basecase
    f[1] = 1

    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]
        return f[n]
        print(f[n])


def main():
    my_dictionary = {}
    f = fib_memoization(6, my_dictionary)
    print(f)


if __name__ == '__main__':
    main()
