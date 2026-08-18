# S P A C E J A M
#
# Given a string, remove all spaces from the string, insert two spaces between every character, convert all alphabetical letters to uppercase, and return the result.
# Non-alphabetical characters should remain unchanged (except for spaces).
#

def space_jam(s):
    sol = []
    for x in s:
        if x != ' ':
            sol.append(x.upper())
            
    sol = "  ".join(sol)

    return sol


space_jam("   free   Code   Camp   ")


        

