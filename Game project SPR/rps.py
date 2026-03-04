import random
item_list=["Rock","Paper","Scissor"]
user_choice=input("enter your move - rock , paper , scissor = ")
comp_choice=random.choice(item_list)

print(f"user choice is = {user_choice} , computer choice is ={comp_choice}")
if user_choice == comp_choice:
    print("Both choice is Match : Match Tie")

elif user_choice=="Rock":
    if comp_choice=="Paper":
        print("paper cover the rock : Computer Win ")
    else:
        print("Rock Smash Scissor : you win")
        
elif user_choice=="Paper":
    if comp_choice=="Scissor":
        print("Scissor cuts the paper , computer Wins")
    else:
        print("paper cover the rock,You win")
elif user_choice=="Scissor":
    if comp_choice=="Rock":
        print("Rock samash Scissor : Computer Win")
    else :
        print("Scissor cut the paper: you win")
    