import random

random_number = random.randint(1,100)
while True:
    try:
        guess = int(input("guess a number between 1-100: "))

        if guess > 100 or guess < 1:
            print("enter a number between 1-100 only pls")

        elif guess > random_number:
            print("too high")

        elif guess <  random_number:
            print("too low") 
        
        else:
            print(f"congo u gave guessesd the correct number which is {random_number}")
            break
        
    except ValueError:
        print("please enter a proper number")