import random
balance= [10000, 20000, 5000, 50000, 10004, 23843, 74923, 75284, 35878, 45984, 88923, 84543, 58300, 458985, 9458948, 48945, 45809, 47948, 4980948, 94800948, 7854, 459, 23, 5984,75948, 859, 509, 9312, 18091, 89423, 9844]
bank= random.choice(balance)
print(f"Dear customer, your balance is:{bank}")
loop=0
while(loop<1):
    option= int(input("Press 1 to deposit" \
" 2 to Credit " \
" 3 to  exit:  "))
    if (option==1):
        deposi= int(input("How much did you want to Deposit:  "))
        if (deposi>=0):
            bank= bank+deposi
        print(f"Your money is deposited and now your new bank balance is {bank}")
        exit1=int(input("Press 1 to exit or 2 to continue:  "))
        if(exit1==1):
            break
    elif(2==option):
        credits= int(input("How much did you want to Credit:  "))
        if (credits<=bank):
            bank= bank-credits
            print(f"Your money is credited and now your bank balance is: {bank}")
        else:
            print("You dose not have suficeanyt bank balanc.")
        exit2=int(input("Press 1 to exit or 2 to continue:  "))
        if(exit2==1):
            break
    elif(option==3):
        break
    else:
        print("I am not able understand what you want to do.")
