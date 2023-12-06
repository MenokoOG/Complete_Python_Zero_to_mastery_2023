from random import randint
# generate number 1-10
answer = randint(1, 10)
# input from user.

# Check that input is a number 1-10
while True:
    try:
        print(answer)  # this is for programmer test for program. comment back out once test is complete.
        guess = int(input("guess a number 1-10 "))
        if 0 < guess < 11:
            if guess == answer:
                print("You are AWESOME!!!")
                break
        else:
            print("hey bozo i said 1-10, not 0-10")
    except ValueError:
        print("please enter a number")
        continue

# check if number is the right guess. otherwise ask again.