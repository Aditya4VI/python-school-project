import random
while True:
    print("Hay here you can save your password.")
    print("And also you can encrypt your password.")
    print("Did you want to save password")
    print("or you want to delete")
    print("or you want to search password")
    print("")
    what_to_do=input("Tell me what to:-  ").lower()
    print("")
    if "save" in what_to_do:
        password=input("Enter your password (only password):-  ")
        print("")
        file_name=input("But befor \nI will save your password tell \nme the name which will halp\nyou to find your password (Only file name):-  ").lower()
        print("")
        print("Ok, now I am saving your password.")
        with open(f'{file_name}.txt','w')as save:
            save.write(f"{password}")
        print("Your password is saved.")
        print("")
    elif("delete"in what_to_do):
        which_password=input("Tell me the of file name which you used\nwhen you haved save the password:-  ").lower()
        print("")
        with open(f'{which_password}', 'w')as delete:
            pass
    elif("encrypt password" in what_to_do):
        which_type=random.choice(list(range(1,4)))
        password=input("Enter your password (Only password):-  ")
        print("")
        file_name=input("But befor \nI will save your password tell \nme the name which will halp\nyou to find your password (Only file name):-  ").lower()
        print("")
        if (which_type==1):
            password_to_bi=""
            for i in password: 
                password_to_bi1=format(ord(i),'08b')
                password_to_bi+=password_to_bi1
            e1_password=(password_to_bi)[::-1]
            e2_password=""
            for q in e1_password:
                if(q=="1"):
                    a="0"
                    e2_password+=(a)
                else:
                    a="1"
                    e2_password+=a
            e3_password=""
            for z in e2_password:
                if (z=="1"):
                    v="a"
                    e3_password+=v
                else:
                    v="A"
                    e3_password+=v
            with open(f"{file_name}", 'w')as encryptor:
                encryptor.write(f"{which_type} \n")
                encryptor.write(f"{e3_password}")
            print('Your password is saved.')    