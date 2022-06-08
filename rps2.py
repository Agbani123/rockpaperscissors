import random
def rockpaperscissors():
    #asking for input
    user=input("Take a pick: R, S or P for rock, scissors, paper respectively.\n").upper()
    #when the user gives a wrong input
    while user not in "RPS":
        user=input("I don't have that kind of time. Abeg pick a valid choice\n").upper()
    #getting the computers choice using the random module
    CPU= random.choice(["R", "S", "P"])
    # if the user and Cpu gives the same hand signal
    while user==CPU:
        print("Player: ", user, " and CPU: ", CPU, ".It's a tie")
        user=input("Take a pick: R, S or P for rock, scissors, paper respectively.\n").upper()
        CPU= random.choice(["R", "S", "P"])
    print("Player: ", user, " and CPU: ", CPU)
    if user=="R":
        if CPU=="P":
            return "CPU wins"
        else:
            return "You win"
    elif user=="P":
        if CPU=="S":
            return "CPU wins"
        else:
            return "You win"
    elif user=="S":
        if CPU=="P":
            return "CPU wins"
        else:
            return "You win"
print(rockpaperscissors())
