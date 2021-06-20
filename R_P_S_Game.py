import random

user_action = input("Enter a choice(rock, paper, scissor): ")

# user input

possible_actions=["rock","paper","scissor"]
computer_actions=random.choice(possible_actions)

# make the computer choose

print(f"\n You chose {user_action}, computer chose {computer_actions}.\n")

# how to determine a winner

if user_action==computer_actions:
    print(f"Both palyers selected {user_action}. It's a tie!")

elif user_action=="rock":
    if computer_actions=="scissor":
        print("You win!")
    else:
        print("You lose!")

elif user_action=="paper":
    if computer_actions=="rock":
        print("You win!")
    else:
        print("You lose!")

elif user_action=="scissor":
    if computer_actions=="paper":
        print("You win!")
    else:
        print("You lose!")

