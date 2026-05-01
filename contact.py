while True:
     option=int(input("Enter 1 to find phone number or 2 to save phone number:-  "))
     if (option==1):
          user=input("Enter person name:-   ").lower()
          with open('write.txt','r')as contact:
               allcontact=contact.readlines()
               
          contact_num1={}
          for i in allcontact:
               y=i.split(":")
               c={y[0]:y[1]}
               contact_num1.update(c)
          phone=False
          for k in contact_num1:
               if k in user:
                    phone=True
                    print(f"Phone number of {user.capitalize()} is {contact_num1[k]}")
                    break
          if(phone==False):
               print("Phone dose not found.")
          continue1=input("Did you want to continue.(Yes or No):-  ").lower()
          if (continue1=="no"):
               break
     elif(option==2):
          name=input("Enter the name of persion:-  ").lower()
          number=input("Enter the number of persion:-  ")
          with open('write.txt', 'a')as save:
               save.write(f"{name}:{number} \n")
               print("Your number is saved.")
               save.close
          continue1=input("Did you want to continue.(Yes or No):-  ").lower()
          if (continue1=="no"):
               break
