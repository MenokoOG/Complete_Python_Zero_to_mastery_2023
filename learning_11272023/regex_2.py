"""Regex lesson, Menoko OG, 11-2023"""
# password validation exercise
# at least 8 characters long
# contain any sort letters, numbers, and special characters
# must end with a number
import re
pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
string = "Lawrence"
pattern2 = re.compile(r"[A-Za-z0-9$%#@]{8,}\d")
password = "hdjkahskdha5534%$9"
password2 = "jkjjdhJJ##@847hj" # does not end in a number so returns None

a = pattern.search(string)
check = pattern2.fullmatch(password)
check2 = pattern2.fullmatch(password2)
print(check)
print(check2)
