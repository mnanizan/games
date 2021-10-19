"""
This is random number guessing game.
The computer will generate a random number.
The computer will give a hint either the user guesses is above or below the correct random number.
The computer will track how many times the user guesses to get to the correct random number.
"""
import random                         #import random module, which is preinstalled with python

top_of_range = input("Type a number: ")

if top_of_range.isdigit():           #.isdiggit is to check if the input a digit, if its a digit it will return as true
    top_of_range = int(top_of_range)

    if top_of_range <= 0:            #if the number keyed in is 0 or less
        print("Please key in a number greater than 0 next time")
        quit()
else:
    print("Please key in a number next time") #if user keyed in something other than number
    quit()

random_number = random.randint(0, top_of_range) #the range of number to guess from 0-10
                                                #another way to do this is print(random.randrange())
                                                #another way to do this is print(random.randint()) , this function will include last index
guesses = 0

while True:                                     #only if its true
    guesses += 1
    user_guess = input("Make a guess: ")        #the guessing input
    if user_guess.isdigit():                    # .isdiggit is to check if the input a digit, if its a digit it will return as true
        user_guess = int(user_guess)
    else:
        print("Please key in a number next time.")  # if user keyed in something other than number
        continue                                    #to continue looping it back at while function again

    if user_guess == random_number:                 #if user guessed it right
        print("You guessed it right!")
        break                                       #to stop the loop once user got it right
    elif user_guess > random_number:
        print("Your guess is above the number!")#if user guess is above the correct @ random number
    else:
        print("Your guess is below the number!")#if user guess is below the correct number

print("You got it in ", guesses, "guesses")