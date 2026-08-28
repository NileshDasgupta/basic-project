import random

emojis = {"r": "🪨", "p":"📃", "s":"✂️"}
choose = ("r","p","s")

computer_choose = random.choice(choose)

def get_the_user_input():
    while True:
        user_input =input("choose rock,paper,scisor(r/p/s): ").lower()
        if user_input not in choose:
            print("invalid choice")
            continue
        else:
            break
    return user_input

def display_of_choice(user_input):
    print(f"you choosed {emojis[user_input]}")
    print(f"computer choosed {emojis[computer_choose]}")
 
def game_logic(user_input):
      if user_input == computer_choose:
            print("tie")
    
      elif (
        (user_input == "r" and computer_choose == "s") or
        (user_input == "p" and computer_choose == "r") or
        (user_input == "s" and computer_choose == "p")):
        print("you win")
    
      else:
         print("you lost")

def play_game():
    while True:
        user_input = get_the_user_input()
        display_of_choice(user_input)
        game_logic(user_input)
        continue_play = input("do you want to continue(y/n): ").lower()
        if continue_play == "n":
            break

play_game()




    