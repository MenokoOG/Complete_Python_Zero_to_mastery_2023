"""Error handling exercise lesson, L. Jefferson II, Menoko OG, 11/2023"""
while True: #this makes code run again after exception
    try:
        age = int(input("what is your age? ")) 
        # print(age)
        10/age 
    except ValueError:
        print("Please enter a number.")
    except ZeroDivisionError:
        print("Please enter age hihger than 0.")
    else: 
        print(f"Thank You, {age} year old person!")
        break
    finally:
        print("This is the end end of program, have a nice day!")