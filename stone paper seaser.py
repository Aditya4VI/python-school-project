import random
print ("Stone, Paper, Saesar")
s_p_c= {"stone":1, "paper":2, "saesar":3}
loop= int(input("How much match you want to play."))
for i in range(1, loop+1):
    computer1= random.choice(list(range(1,4)))
    user_choice= input("Enter your choice (in small and in one word):-  ")
    user_choice_convet= s_p_c[user_choice]
    if (computer1==1 and user_choice_convet==1):
        print(f"I geush stone.")
        print ("Match drow.")
    elif(computer1==2 and user_choice_convet==2):
        print(f"I geush paper.")
        print("Match drow.")
    elif(computer1==3 and user_choice_convet==3):
        print(f"I geush saesar.")
        print("Match drow.")
    elif(computer1==1 and user_choice_convet==2):
        print(f"I geush stone.")
        print("You win.")
    elif(computer1==1 and user_choice_convet==3):
        print(f"I geush stone.")
        print("I win.")
    elif(computer1==2 and user_choice_convet==1):
        print(f"I geush paper.")
        print("I win.")
    elif(computer1==2 and user_choice_convet==3):
        print(f"I geush paper.")
        print("You win.")
    elif(computer1==3 and user_choice_convet==1):
        print(f"I geush saesar.")
        print("You win.")
    elif(computer1==3 and user_choice_convet==2):
        print(f"I geush saesar.")
        print("I win.")
p=input("Press Enter to exit.")