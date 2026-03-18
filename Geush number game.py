import random
print("There are 3 level.")
print("In each level you will get 5 attempt.")
while True:
    level= int(input("Which level do you want to play enter:-  "))
    if (level==1):
        print("Ok you want to play level 1.")
        print("In this level you have to geush number between 1 to 10.")
        print("This is so easy level.")
        num_1= random.choice(list(range(1, 11)))
        for time in range (1, 6):
            print(f"Its your {time}th attempt.")
            user_number= int (input("Geush the number:-  "))
            win=False
            if (user_number==num_1):
                win=True
                print ("Your geush is correct.")
                print ("You win the game. ")
                print(f"In only {time} attempt. ")
                break
            elif(user_number<1 or user_number>10):
                print("Attempt waste.")
            elif(user_number>num_1):
                print("Number is smaller.")
            elif(user_number<num_1):
                print ("Number is greater.")
        if (win==False):
            print("You lose the game.")
    elif(level==2):
        print("Ok you want to play level 2.")
        print("In this level you have to geush number between 1 to 50.")
        print("This is so meadium level.")
        num_1= random.choice(list(range(1, 51)))
        for time in range (1, 6):
            print(f"Its your {time}th attempt.")
            user_number= int (input("Geush the number:-  "))
            win=False
            if (user_number==num_1):
                win=True
                print ("Your geush is correct.")
                print ("You win the game. ")
                print(f"In only {time} attempt. ")
                break
            elif(user_number<1 or user_number>50):
                print("Attempt waste.")
            elif(user_number>num_1):
                print("Number is smaller.")
            elif(user_number<num_1):
                print ("Number is greater.")
        if (win==False):
            print("You lose the game.")
    elif(level==3):
        print("Ok you want to play level 3.")
        print("In this level you have to geush number between 1 to 100.")
        print("This is so hard level.")
        num_1= random.choice(list(range(1, 101)))
        for time in range (1, 6):
            print(f"Its your {time}th attempt.")
            user_number= int (input("Geush the number:-  "))
            win=False
            if (user_number==num_1):
                win=True
                print ("Your geush is correct.")
                print ("You win the game. ")
                print(f"In only {time} attempt. ")
                break
            elif(user_number<1 or user_number>100):
                print("Attempt waste.")
            elif(user_number>num_1):
                print("Number is smaller.")
            elif(user_number<num_1):
                print ("Number is greater.")
        if (win==False):
            print("You lose the game.")
    else:
        print("Your level is invalid.")
    play_again=input("Did you want to play a gain.  ").lower()
    if (play_again=="no"):
        break
