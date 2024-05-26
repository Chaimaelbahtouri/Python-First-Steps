import random

while True:
    suggestions = ["rock","paper","scissors"]
    player = None
    computer = random.choice(suggestions)
    if True:
        while player not in suggestions:
            player = input("rock , paper or scissors ?").lower()
            if player == computer:
                print("computer :",computer)
                print("player : ",player)
                print("Tie,Tie")
            elif player == "paper":
                if computer == "scissors":
                    print("computer : ",computer)
                    print("player : ",player)
                    print("you lose")
                if computer == "rock":
                    print("computer : ",computer)
                    print("player : ",player)
                    print("you win")
            elif player == "scissors":
                if computer == "paper":
                    print("computer : ",computer)
                    print("player : ",player)
                    print("you win")
                if computer == "rock":
                    print("computer : ",computer)
                    print("player : ",player)
                    print("you lose")
            elif player == "rock":
                if computer == "scissors":
                    print("computer : ",computer)
                    print("player : ",player)
                    print("you win")
                if computer == "paper":
                    print("computer : ",computer)
                    print("player : ",player)
                    print("you lose")
            else :
                print("please enter the correct choice ")
    ask = input("do you want play again ? yes / no : ").lower()
    if ask != "yes":
        print("ook by!")
        break