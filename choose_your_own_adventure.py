print("Welcome to my first game!")
name = input("What is our name: ")
age = int(input("What is your age: "))
health = 10

if age >= 18:
    print("You are old enough to play!")
    wants_to_play = input("Do you want to play?(Yes/No)").lower()

    if wants_to_play == "yes":
        print("You are starting with", health, "health")
        print("Lets's play!")
        left_or_right = input("First choice, pick left or right?(Left/Right)").lower()

        if left_or_right == "left":
            across_around = input("Nice, you follow the path and reach a lake. Do you want to swim across or go around?(across/around)?").lower()

            if across_around == "around":
                print("You went around, and got to the other side of the lake")

            else:
                print("You managed to get across but you got bitten by crocodile and lost 5 health")
                health -= 5

            house_cottage = input("You notice a house and a cottage, which do you go to?(House/Cottage)").lower()
            if house_cottage == "house":
                print("The owner hit you for trespassing, you lost 5 health")
                health -= 5

                if health <= 0:
                    print("Your health is now 0, you lost")

            else:
                print("You have survived, you won the game!")

        else:
            print("You fell down the lake and lost")

    else:
        print("Too bad, Cya!..")

else:
    print("You are not old enough to play")
