# camelCase

# Given a string, return its camel case version using the following rules:

# Words in the string argument are separated by one or more characters from the following set: space ( ), dash (-), or underscore (_). Treat any sequence of these as a word break.

# The first word should be all lowercase.

# Each subsequent word should start with an uppercase letter, with the rest of it lowercase.

# All spaces and separators should be removed.

def to_camel_case(s):

    s = s.replace("_", " ").replace("-", " ")
    words = s.split()
    
    for i, x in enumerate(words):
        if i == 0:
            s = x.lower()
        
        if i > 0:
            s = s + x.capitalize()

    return s



to_camel_case("FREE cODE cAMP")
