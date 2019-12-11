def karatsuba(x, y):
    len_x = len(str(x))
    len_y = len(str(y))
    if len_x == 1 or len_y == 1:
        return x * y
    else:
        n = max(len_x, len_y)
        nby2 = n // 2

        a = x // 10 ** nby2
        b = x % 10 ** nby2
        c = y // 10 ** nby2
        d = y % 10 ** nby2

        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        mid = karatsuba(a + b, c + d)

        return (ac * 10 ** (2 * nby2)) + ((mid - ac - bd) * 10 ** nby2) + bd


print(int(karatsuba(3141592653589793238462643383279502884197169399375105820974944592, 2718281828459045235360287471352662497757247093699959574966967627)))
print(int(karatsuba(123, 456)))
print(123 * 456)