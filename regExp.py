# Python RegEx
# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

# RegEx can be used to check if a string contains the specified search pattern.

import re

# Search the string to see if it starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
""" ^ is use to checkfor starting word .* means vache game te hoy and
spain$ hear $ is use for veirfy the last word """

print(x)

y = re.search("^.*rain.*$", txt)
print(y)
#      01234567890123456
str = "The rain in Spain"
x = re.findall("ai", str)
print(x)

tr = "The rain in Spain"
x = re.search( "\s", str)
print("The first white-space character is located in position:", x.start())
x = re.search("rain", str)
print(x)
# split()
str = "The rain in Spain"
x = re.split("\s", str)
print(x)
x = re.split("\s", str, 1)
print(x)
# The sub() Function

# The sub() function replaces the matches with the text of your choice:
# Example
# Replace every white-space character with the number 9:

str = "The rain in Spain"
x = re.sub("\s", "9", str)
print(x)
x = re.sub("\s", "9", str, 2)
print(x)

# The Match object has properties and methods used to retrieve information about the search, and the result:

# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match
# Example
# Print the position (start- and end-position) of the first match occurrence.

# The regular expression looks for any words that starts with an upper case "S":

str = "The rain in Spain"
x = re.search(r"\bS\w+", str)
print(x.span())

# Print the string passed into the function:
x = re.search(r"\bS\w+", str)
print(x.string)

# Print the part of the string where there was a match.

# The regular expression looks for any words that starts with an upper case "S":

x = re.search(r"\bS\w+", str)
print(x.group())

# Note: If there is no match, the value None will be returned, instead of the Match Object.
