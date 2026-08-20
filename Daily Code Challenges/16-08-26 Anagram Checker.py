# Anagram Checker
#
# Given two strings, determine if they are anagrams of each other (contain the same characters in any order).
#
# Ignore casing and white space.
#

def are_anagrams(str1, str2):

    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")

    l1 = len(str1)

    check_count = 0

    for x in str1.lower():
        if x in str2.lower():
            check_count += 1

    return check_count == l1

are_anagrams("listen", "silent")
are_anagrams("School master", "The classroom")
are_anagrams("A gentleman", "Elegant man")
are_anagrams("Hello", "World")
are_anagrams("apple", "banana")
are_anagrams("cat", "dog")