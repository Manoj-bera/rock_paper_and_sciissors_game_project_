#Rock_paper_and_scissors_game
import random        #random module is a module which  allows us to choose random value

def check(comp, user):
    if(comp == user):
        return 0
    if(comp == 0 and user == 1):
        return -1
    if(comp == 1 and user == 2):
        return -1
    if(comp == 2 and user == 0):
        return -1
    
    return 1

while True:
    print("**************** Snake Water Game******************")
    comp = random.randint(0, 2)     #randint is a function inside random method which allows to choose rand int values
    user = int(input("0 is for snake, 1 is for water, 2 is for gun : "))

    print("you choosen : ",user)
    print("comp choosen : ",comp)
    
    score = check(comp, user)
    if score == 0:
        print("Draw!!")
        print("Play again")
    elif score == -1:
        print("You loose!!")
        print("Play again")
    elif score == 1:
        print("congratulations you won !!")
        print("Play again")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again == "yes":
        continue
    else:
        break