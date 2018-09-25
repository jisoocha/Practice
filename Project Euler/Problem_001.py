# https://projecteuler.net/problem=1

# Multiples of 3 and 5
# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


def sum_multiples(num, ths):
    mx = (ths - 1) // num
    return num * sum(range(1, mx + 1))


def solution():
    num1 = 3
    num2 = 5
    ths = 1000

    print(sum_multiples(num1, ths) + sum_multiples(num2, ths) - sum_multiples(num1 * num2, ths))


solution()