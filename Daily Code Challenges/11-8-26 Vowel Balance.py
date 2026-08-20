# Vowel Balance
#
# Given a string, determine whether the number of vowels in the first half of the string is equal to the number of vowels in the second half.
#
# The string can contain any characters.
#
# The letters a, e, i, o, and u, in either uppercase or lowercase, are considered vowels.
#
# If there's an odd number of characters in the string, ignore the center character.
#

def is_balanced(s):

    s = s.lower()

    split_point = len(s) // 2

    left_s = s[:split_point]

    if len(s) % 2 != 0:
        right_s = s[split_point + 1:]
    else:
        right_s = s[split_point:]

    left_count = 0
    right_count = 0

    for x in left_s: 
        if x in "aeiou":
            left_count += 1
        
    for x in right_s: 
        if x in "aeiou":
            right_count += 1

    if left_count == right_count:
        return True
    else:
        return False

is_balanced("123A#b!E&*456-o.U")
is_balanced("abcdefghijklmnopqrstuvwxyz")
is_balanced(" ")
is_balanced("string")
is_balanced("Kitty Ipsum")
is_balanced("Lorem Ipsum")
is_balanced("racecar")