# Sum of Squares
#
# Given a positive integer up to 1,000, return the sum of all the integers squared from 1 up to the number.
#

def sum_of_squares(n):

    if n < 0:
        print("Input a Positive Integer")

    sol = 0

    for x in range(n + 1):
        sol += x * x

    return sol


sum_of_squares(5)
sum_of_squares(10)
