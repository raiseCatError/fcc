# Targeted Sum
#
# Given an array of numbers and an integer target, find two unique numbers in the array that add up to the target value. Return an array with the indices of those two numbers, or "Target not found" if no two numbers sum up to the target.
#
# The returned array should have the indices in ascending order.
#

def find_target(arr, target):

    for i, x in enumerate(arr):
        
        for ii, y in enumerate(arr):

                if i < ii and x + y == target:        
                    return [i, ii]
            
    return "Target not found"
            


find_target([2, 7, 11, 15], 9)
find_target([3, 2, 4, 5], 6)
find_target([1, 3, 5, 6, 7, 8], 15)
find_target([1, 3, 5, 7], 14)