import random, math
def play():
    user= input("What's your choice: R, P or S...i.e rock, paper or scissors\n").lower()
    computer= random.choice(["r", "p", "s"])

    if user==computer:
        return (0, user,computer)
    
    #we introduce a helper function, is_win that tells us who won
    if is_win(user, computer):
        return (1, user, computer)
    return (-1, user, computer) 

#we now define the function
def is_win(player, opponent):
    #return true means the player won opponent
    if (player=="s" and opponent=="p") or (player=="p" and opponent=="r") or (player=="r" and opponent=="s"):
        return True
    else:
        return False

#winnning best out of n games, we use math.ceil for this
def best_out_of(n):
    player_wins=0
    computer_wins=0
    wins_necessary= math.ceil(n/2)
    while player_wins< wins_necessary or computer_wins< wins_necessary:
        result, user, computer=play()
        if result==0:
            print("Its a tie")
        elif result==1:
            player_wins+=1
            print("You played {} and the computer played {}. you won".format(user,computer))
        else:
            computer_wins+=1
            print("You played {} and the computer played {}. you lost".format(user,computer))
    if player_wins>computer_wins:
        print("You have won the best out of", n)
    else:
        print("the computer has won best out of", n)

if __name__=="__main__":
    print(best_out_of(9))