import random

number = list(range(1, 10))
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
alphabeT = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
symbol = ["~","!","@","#","$","%","^","&","*","-","_","+","=","/","?",">","<"]

digit = int(input("Of how much digit password should be: "))
loop_run = 0
which_digit = [1, 2, 3, 4]
password = []

while (loop_run < digit):
    loop_run += 1   # FIXED increment
    which_digit_find = random.choice([1, 2, 3, 4])  # FIXED: don't remove items
    if which_digit_find == 1:
        number_which = random.choice(number)
        password.append(str(number_which))  # convert to string
    elif which_digit_find == 2:
        alphabet_which = random.choice(alphabet)
        password.append(alphabet_which)
    elif which_digit_find == 3:
        alphabeT_which = random.choice(alphabeT)
        password.append(alphabeT_which)
    elif which_digit_find == 4:
        symbol_which = random.choice(symbol)
        password.append(symbol_which)
print(f"Here is the password of {digit} ")
print("".join(password))  # join into one string
input= input("Press Enter to exit")