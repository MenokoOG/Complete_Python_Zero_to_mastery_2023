"""Error lesson, L. Jefferson II, Menoko OG, 11/2023"""

# error handling, allows python to run even if there are errors in program. There are a lot of built in exceptions in python, syntax, type, name, index, ie.....
while True: #this makes code run again after exception
    try:
        age = int(input("what is your age? ")) #should be number right?
        # print(age)
        10/age #here it would normallly return zerodivsion error without the except statement.
    except ValueError:
        print("Please enter a number.")
    except ZeroDivisionError:
        print("Please enter age hihger than 0.")
    else: #this stops program once try is accepted and coditions of program for correct input met.
        print(f"Thank You, {age} year old person!")
        break
    print("*" * 40)
    
def sumy(num1, num2):
    try:
        return num1 + num2
    except (TypeError, ZeroDivisionError) as err:
        print(err)
    
print(sumy( "1" + 2)) 
    