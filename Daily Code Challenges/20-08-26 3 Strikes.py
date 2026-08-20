# 3 Strikes
#
# Given an integer between 1 and 10,000, return a count of how many numbers from 1 up to that integer whose square contains at least one digit 3.
#

def squares_with_three(n):
    counter = 0

    for x in range(n + 1):
        y = str(x * x)
    
        if "3" in y:
            counter += 1

    return counter

squares_with_three(10) 
squares_with_three(100)
squares_with_three(1000)
squares_with_three(10000)