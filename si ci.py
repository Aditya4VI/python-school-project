print("In this you can find Simple Interest")
print("Compound Interest and Amount")
print("Press 1 for Simple Interest")
c= int(input("and 2 for Compound Interest: "))

if c == 1:
    p = float(input("Enter Principal: "))
    t = float(input("Enter Time: "))
    r = float(input("Enter Rate per annum: "))
    
    si = (p * r * t) / 100
    amount = p + si
    
    print(si, "is Simple Interest and", amount, "is Amount")

else:
    p = float(input("Enter Principal: "))
    t = float(input("Enter Time: "))
    r = float(input("Enter Rate: "))
    
    amount = p * (1 + r/100) ** t
    ci = amount - p
    
    print(ci, "is Compound Interest and", amount, "is Amount")

input("Press Enter key to close window")
