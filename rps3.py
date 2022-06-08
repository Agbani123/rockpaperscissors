import random
def play():
    user= input("What's your choice: R, P or S...i.e rock, paper or scissors\n").lower()
    computer= random.choice(["r", "p", "s"])

    if user==computer:
        return "You have chosen the same stuff {}. It's a tie".format(user)
    
    #we introduce a helper function, is_win that tells us who won
    if is_win(user, computer):
        return "You have chosen {} and the computer has chosen {}. You won".format(user, computer)
    return "You have chosen {} and the computer has chosen {}. You lost".format(user, computer) 

#we now define the function
def is_win(player, opponent):
    #return true means the player won opponent
    if (player=="s" and opponent=="p") or (player=="p" and opponent=="r") or (player=="r" and opponent=="s"):
        return True
    else:
        return False
if __name__=="__main__":
    print(play())