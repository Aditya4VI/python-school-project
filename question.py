name=input("Hey can you tell me your name.  ")
choice=int(input("Hay first press 1 to give exame of maths and 2 to give exam of G.K.  "))
if(choice==1):
    print ("Answer in one word.")
    score=0
    maths1=float(input("So, tell the product of 12.3 and 9.4? "))
    if(maths1==115.62):
        score+=1
        print (f"Hay {name}, your first answer is correct.  ")
    else:
        print (f"{name}, your answer is wrong. Correct answer is 115.62 .  ")
    maths2=float(input(f"{name}, what is the difference of 9 and 6.1 ?  "))
    if(maths2==2.9):
        score+=1
        print (f"{name}, you are correct.  ")
    else:
        print (f"{name}, you are wrong. Correct answer is 2.9 .  ")
    maths3=float(input("Now what is the value of x if 2x-3=1?  "))
    if(maths3==2):
        score+=1
        print (f"{name}, you are absolutely correct.  ")
    else:
        print (f"{name}, your answer is wrong. x=2 is correct answer.  ")
    print (f"{name}, got {score} marks out of 3 marks.  ")
else:
    point=0
    gk1=input(f"{name}, Which city is the capital of India?   ")
    ga1="delhi"
    if ga1 in gk1.lower():
        point+=1
        print (f"{name}, your answer is correct.  ")
    else:
        print (f"{name}, your answer is not correct. The correct answer is Delhi")
    gk2=input("What is the National Flower of India?  ")
    ga2="lotus"
    if ga2 in gk2.lower():
        point+=1
        print (f"{name}, your answer is correct.  ")
    else:
        print (f"{name}, your answer is not correct. The correct answer is Lotus")
    gk3=input(f"Which gas is prodused during Photosynthesis by green plant? Write the full name of gas.  ")
    ga3="oxygen"
    if ga3 in gk3.lower():
        point+=1
        print (f"{name}, your answer is correct.  ")
    else:
        print (f"{name}, Oxygen is produce by plant. Your answer was wrong.")
    print(f"So, {name} you have score {point} marks out of 3 marks.")
y=input("Press Enter to exit.")