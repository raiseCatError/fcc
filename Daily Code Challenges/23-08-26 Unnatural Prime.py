# Unnatural Prime

# Given an integer, determine if that number is a prime number or a negative prime number.

# A prime number is a positive integer greater than 1 that is only divisible by 1 and itself.

# A negative prime number is the negative version of a positive prime number.

# 1 and 0 are not considered prime numbers.


def is_unnatural_prime(n):

    if n < 0:
        n = n * (-1)

    counter = 0
    
    for x in range(n):
        if x > 0:
                if n % x == 0:
                    counter += 1

    if counter == 1:
        print(True)
        return True
    else:
        print(False)
        return False

is_unnatural_prime(-1)
is_unnatural_prime(1)
is_unnatural_prime(-19)
is_unnatural_prime(-23)
is_unnatural_prime(0)
is_unnatural_prime(-61)