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