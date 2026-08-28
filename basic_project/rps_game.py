import random

emojis = {"r": "🪨", "p":"📃", "s":"✂️"}
choose = ("r","p","s")

computer_choose = random.choice(choose)

while True:
    user_input =input("choose rock,paper,scisor(r/p/s): ").lower()
    if user_input not in choose:
        print("invalid choice")
        continue

    print(f"you choosed {emojis[user_input]}")
    print(f"computer choosed {emojis[computer_choose]}")

    if user_input == computer_choose:
        print("tie")

    elif (
        (user_input == "r" and computer_choose == "s") or
        (user_input == "p" and computer_choose == "r") or
        (user_input == "s" and computer_choose == "p")):
        print("you win")

    else:
        print("you lost")

    continue_play = input("do you want to continue(y/n): ").lower()
    if continue_play == "n":
        break


    