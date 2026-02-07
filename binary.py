print("If you want to change the text into binary press 1 ")
chose=int(input("and if you want to change binary into text press 2:-   "))
binary=""
text="" 
if (chose==1):
    sentence= input("Enter your sentence:-  ")
    for character in sentence:
        binary2= ord(character)
        binary3= format(binary2, '08b')
        binary+=binary3
    print(binary)
elif(chose==2):
    code = input("Enter binary code: ")
    for i in range(0, len(code), 8):
        byte = code[i:i+8]             
        code1 = int(byte, 2)            
        code2 = chr(code1)  
        text+= code2           
    print(text)         
exit= input("Press Enter to exit.")