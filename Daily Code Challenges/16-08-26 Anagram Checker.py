# Anagram Checker
#
# Given two strings, determine if they are anagrams of each other (contain the same characters in any order).
#
# Ignore casing and white space.
#

def are_anagrams(str1, str2):

    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    l1 = len(str1)

    check_count = 0

    for x in str1:
        if str1.count(x) == str2.count(x):
            check_count += 1

    return check_count == l1

are_anagrams("listen", "silent")
are_anagrams("School master", "The classroom")
are_anagrams("A gentleman", "Elegant man")
are_anagrams("Hello", "World")
are_anagrams("apple", "banana")
are_anagrams("cat", "dog")