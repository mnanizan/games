"""
Typical rock, paper, scissor game
The computer vs user
Once user choose to quit the game, the score will be shown
"""
import random

user_wins = 0          #tracking scores by creating this two variables
computer_wins = 0

options = ["rock", "paper", "scissor"]
options[0]

while True:            #while loop
    user_input = input("Type Rock/Paper/Scissor or Q to quit: ").lower()
    if user_input == 'q':
        break

    if user_input not in ["rock", "paper", "scissor"]: #if user didn't key in either of these three input
        continue                                       #keep looping again at the while statement

    random_number =random.randint(0, 2)                #rock:0, paper:1, scissor: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissor":
        print("You won!")
        user_wins += 1
        continue

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
        continue

    elif user_input == "scissor" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
        continue

    elif user_input == "rock" and computer_pick == "rock":
        print("Deuce!")
        continue

    elif user_input == "paper" and computer_pick == "paper":
        print("Deuce!")
        continue

    elif user_input == "scissor" and computer_pick == "scissor":
        print("Deuce!")
        continue

    else:
        print("You lose!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye")