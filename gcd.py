# find the greatest common divisor
# using euclid algorithm

# GCD is definded as the greatest common divisor
# which divides both the number with the zero reminder

# this algorithms works by dividing the first number
# by second number and checks for the zero remainder
# else it replaces the number a with b and b with
# remainder and keep on dividing unless we get a zero
# remainder


def gcd(a, b):
    result = 0
    while (1):
        result = a % b
        if result == 0:
            return b
        a = b
        b = result


# testing the algorithm
print(gcd(60, 96))  # should be 12
print(gcd(20, 8))  # should be 8
