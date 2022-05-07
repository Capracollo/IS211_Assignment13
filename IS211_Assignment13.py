# Part I - Fibonacci Sequence
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Part II - Euclid's GCD Algorithm

def gcd(a, b):
    if a == 0:
        return b
    else:
        return gcd(b % a, a)


# Part III - String Comparison

def compare_to(s1, s2):
    if s1 < s2:
        return -1
    elif s1 == s2:
        return 0
    elif s1 > s2:
        return 1
    else:
        return compare_to(s1[1:], s2[1:])


if __name__ == '__main__':
    print(fibonacci(27))
    print(gcd(17, 85))
    print(compare_to('string', 'string'))
