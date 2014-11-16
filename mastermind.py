import math

primes = {}


def is_prime(n):
    global primes
    if primes.get(n, False) == True:
        return True

    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


t = int(raw_input())

while t > 0:
    input_range = raw_input()
    start = int(input_range.split(' ')[0])
    end = int(input_range.split(' ')[1])
    count = end - start + 1
    while start <= end:
        if is_prime(start) == True:
            primes.update({start: True})
            count = count - 1

        start = start + 1
    print count

    t = t - 1