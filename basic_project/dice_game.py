import random 

while True:
    start = input("do you want to play(y/n): ").lower()

    if start == "y":
        first_roll = random.randint(1,6)
        print(f"You have rolled {first_roll}")

    elif start == "n":
        print("thanks for playing")
        break

    else:
        print("invalid input")