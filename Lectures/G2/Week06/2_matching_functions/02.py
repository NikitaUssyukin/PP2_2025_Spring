# What are regular expressions?

# Introduction to regex with easy exercises
# https://regexone.com/lesson/introduction_abcs

# Guide on python regex
# https://regexone.com/references/python

# Python regex HOWTO - tutorial for python regexes
# https://docs.python.org/3/howto/regex.html

# Online regex engine to test regexes, supports python flavour
# https://regex101.com/#python

# w3school tutorial on python regex
# https://www.w3schools.com/python/python_regex.asp

import re

text_to_match = "John's email is john.doe@example.com, and his backup is johndoe123@work.net."

pattern = 'john' # our regex

result = re.search(pattern, text_to_match)

print(result) # match object

print(result.group()) # print the match as a string