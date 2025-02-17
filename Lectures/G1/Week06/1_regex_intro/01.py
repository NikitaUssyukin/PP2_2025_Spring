# What are regular expressions?

# Introduction to regex with easy exercises
# https://regexone.com/lesson/introduction_abcs

# Python regex HOWTO - tutorial for python regexes
# https://docs.python.org/3/howto/regex.html

# Online regex engine to test regexes, supports python flavour
# https://regex101.com/#python

# w3school tutorial on python regex
# https://www.w3schools.com/python/python_regex.asp

import re

text = "Hello KBTU"

pattern = "Hello"

result = re.match(pattern, text)

print(result) # match object

print(result.group(0)) # group(0) returns the entire match
