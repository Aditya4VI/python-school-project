print("Here you can check strength of your password.")
password= input("Enter your password:-  ")
#things which can be present in password
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
alphabeT = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
symbol = ["~","!","@","#","$","%","^","&","*","-","_","+","=","/","?",">","<"]
number= list(str(range(1,10)))
#to find length of pass word
length= len(password)
#old point of password
length_d=0
alphabet_d=0
alphabeT_d=0
symbol_d=0
number_d=0
#point get by length test
if (length<=5):
    length_d+=0
elif(length>=6 and length<=8):
    length_d+=1
elif(length<=10):
    length_d+=2
elif(length>10):
    length_d+=3
#point get by alphabet test
for word in alphabet:
    if word in password:
        alphabet_d+=0.5
#point get by alphabeT test
for words in alphabeT:
    if words in password:
        alphabeT_d+=0.5
#point get by symbols
for sym in symbol:
    if sym in password:
        symbol_d+=1.5
#point get by number
for num in number:
    if num in password:
        number_d+=1
#total point get by password
point= alphabeT_d+alphabet_d+length_d+symbol_d+number_d
#now print password deficulty
if (point<=3):
    print("Your password is very weak.")
    print(f"Your password get very low point, only {point}.")
elif(point>=4 and point<=6):
    print("Your password is weak.")
    print(f"Your password get only {point} points.")
elif(point>=7 and point<=9):
    print("Your password is of meadium.")
    print(f"Your password get {point} points.")
elif(point>=10 and point<=12):
    print("Your password is strong.")
    print(f"Your password get total {point} points.")
elif(point>12):
    print("Your password is very strong.")
    print(f"Your password get a larg amount of points, it is {point}.")
u=input("Press Enter to exit.")