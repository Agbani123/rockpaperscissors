import random
def rpc():
    while True:
        user=input("Enter R for rock, P for paper or S for scissors ").upper()
        CPU= random.choice(["R", "P", "S"])
        answer_dict= {"R":"P", "P":"S", "S":"R"}
        print("You: ", user, ", CPU: ", CPU)
        if answer_dict[user]==CPU:
            return "You've lost"
        elif answer_dict[CPU]==user:
            return "You've won."
        elif user==CPU:
            continue
        else:
            break
    
print(rpc())


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