"""Regulae Expression Lesson, Menoko OG, L. Jefferson II, 11-2023"""
import re

pattern = re.compile("this")
pattern2 = re.compile("Search inside this of this string of text please!")
string = "Search inside this of this string of text please! LJ"

# a = (re.search("this", string)) # returns object with index information and the match in string
a = pattern.search(string)
b = pattern.findall(string)
c = pattern2.fullmatch(string) # has to be exact match of pattern and string, if LJ removed from string variable then a match would return, as is it returns = None
d = pattern2.match(string) # will rerun match because it contains
# print(a.span()) # returns the index span
# print(a.start()) # returns the start of index
# print(a.end()) # returns end of index position
# print(a.group()) # returns the object of the search = this
print(a)
print(b)
print(c)
print(d)