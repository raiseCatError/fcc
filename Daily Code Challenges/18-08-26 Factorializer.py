# Factorializer
#
# Given an integer from zero to 20, return the factorial of that number. The factorial of a number is the product of all the numbers between 1 and the given number.
# 
# The factorial of zero is 1.
#

def factorial(n):
    
    if 0 <= n <= 20:
        result = 1
        
        for x in range(1, n + 1):
            result *= x
        
        print(result)

        return result
            
    
    


factorial(0)
factorial(5)
factorial(21)