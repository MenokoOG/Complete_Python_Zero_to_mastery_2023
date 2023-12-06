"""Walrus lesson, L. Jefferson II, Menoko OG, 11/2023"""
a= "helloooooooooooooooooooo"

# print(len(a))
if ( (n := len(a))  > 10):
    print(f"too long {n} elements.")
    
while ((n := len(a)) > 5):
    print(n)
    a = a[:-1]

print(a)