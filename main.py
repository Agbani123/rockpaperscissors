import random
def rockpaperscissors(a,b):
    while a=="R":
        if b=="S":
            print("You win")
        elif b=="P":
            print("CPU wins")
        break
    while a== "P":
        if b=="R":
            print("You win")
        elif b=="S":
            print("CPU wins")
        break
    while a=="S":
        if b=="P":
            print("You win") 
        elif b=="R":
            print("CPU wins")
        break

Done=True
while Done:
    game_list=["R","P","S"]
    user=input("Please pick either 'R' for rock, 'P' for paper or 'S' for scissors\n").title() 
    while user not in "RPS":
        user=input("Put in a valid choice\n").title()
    CPU= random.choice(game_list)
    print(f"Player({user}):CPU({CPU})")
    if user ==CPU:
        print("It's a tie.")
        continue
    else:
        rockpaperscissors(user, CPU) 
    Done=False


