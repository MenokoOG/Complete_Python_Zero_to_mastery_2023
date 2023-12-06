"""conditional logic lesson, L. Jefferson II, Menoko OG"""
is_old = True
is_licensed = True

if is_old and is_licensed:
    print("You are old enough to drive and you have a license!")   
else:
    print("You are not olde enough to drive!")
print("*" * 40)
#truthy and Falsy
#ternary operator or conditional expressions
is_friend = False
can_message = "message allowed" if is_friend else "not allowed to message"

print(can_message)
print("*" * 40)
#short circuiting
is_friend = False
is_user = True

if is_friend or is_user: #here it will print becasue of of the variables is true, if and was used then it would not print becasue and needs both values to be true.
    print("best friends forever!")
print("*" * 40)
