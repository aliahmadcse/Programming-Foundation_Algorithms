# using the recursion to implement the power and factorial function


def power(num, pow):
    if pow == 0:
        return 1
    return num*power(num, pow-1)


def factorial(num):
    if num == 0:
        return 1
    return num*factorial(num-1)


print("{} to the power of {} is {}".format(5,3,power(5,3)))
print("{} factorial is {}".format(5,factorial(5)))
print("{} factorial is {}".format(10,factorial(10)))