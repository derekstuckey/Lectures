def fib_memoization(n: int, lookup: dict) -> int:
    if n < 1:
        return -1
    # base case
    if n == 1 or n == 2:
        lookup[n] = 1

    if lookup.get(n, None) is None:
        lookup[n] = fib_memoization(n - 1, lookup) + fib_memoization(n - 2, lookup)
        return lookup


def main():
    my_dictionary = {}
    f = fib_memoization(6, my_dictionary)
    print(f)


if __name__ == '__main__':
    main()
