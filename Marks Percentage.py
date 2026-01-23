print ("In this you can calculate your marks. And I can only calculate marks of max 12 subject and minum 8 suject.")
name=input("Can you tell me your name first, your name can help me in this work.")
subject=int(input(f"So, {name}, how much subject dose you have."))
if(subject<13 and subject>7):
   if(subject<12):
      if(subject<11):
         if(subject<10):
            if(subject<9):
               if(subject==8):
                  eight1=float(input(f"{name}, how much dose you score in 1st subject."))
                  eight2=float(input(f"Now {name} tell me marks of 2nd subject."))
                  eight3=float(input("Bro tell me marks of 3rd subject."))
                  eight4=float(input(f"{name} what was your score in 4th subject."))
                  eight5=float(input(f"{name} how much dose you score in 5th subject."))
                  eight6=float(input(f"{name}, how much dose you score in 6th subject."))
                  eight7=float(input("So, tell how much dose you score in 7th subject."))
                  eight8=float(input("So, tell how much dose you score in last subject."))
                  total8=float(input("Now tell, what is total marks of each subjct"))
                  score8=eight1+eight2+eight3+eight4+eight5+eight6+eight7+eight8
                  scorepercent8=(score8/(total8*8))*100
                  print (f"So {name}, you have score {scorepercent8}%, and I believe you can do much better.")
            else:
               nine1=float(input(f"{name}, how much dose you score in 1st subject."))
               nine2=float(input(f"Now {name} tell me marks of 2nd subject."))
               nine3=float(input("Bro tell me marks of 3rd subject."))
               nine4=float(input(f"{name} what was your score in 4th subject."))
               nine5=float(input(f"{name} how much dose you score in 5th subject.")) 
               nine6=float(input(f"{name} ,how much dose you score in 6th subject."))
               nine7=float(input("So, tell how much dose you score in 7th subject."))
               nine8=float(input(f"Hey {name} now tell score of 8th subject"))
               nine9=float(input("Now tell, what is the score in last subjct"))
               total9=float(input("Now tell, what is total marks of each subjct"))
               score9=nine1+nine2+nine3+nine4+nine5+nine6+nine7+nine8+nine9
               scorepercent9=(score9/(total9*9))*100
               print (f"So {name}, you have score {scorepercent9}%, and I believe you can do much better.")
         else:
            ten1=float(input(f"{name}, how much dose you score in 1st subject."))
            ten2=float(input(f"Now {name} tell me marks of 2nd subject."))
            ten3=float(input("Bro tell me marks of 3rd subject."))
            ten4=float(input(f"{name} what was your score in 4th subject."))
            ten5=float(input(f"{name} how much dose you score in 5th subject."))
            ten6=float(input(f"{name} ,how much dose you score in 6th subject."))
            ten7=float(input("So, tell how much dose you score in 7th subject."))
            ten8=float(input(f"Hey {name} now tell score of 8th subject"))
            ten9=float(input("Now tell, how much did you score in 9th subjct"))
            ten10=float(input("Now tell, what is the score in last subjct"))
            total10=float(input("Now tell, what is total marks of each subjct"))
            score10=ten1+ten2+ten3+ten4+ten5+ten6+ten7+ten8+ten9+ten10
            scorepercent10=(score10/(total10*10))*100
            print (f"So {name}, you have score {scorepercent10}%, and I believe you can do much better.")
      else:
         ele1=float(input(f"{name}, how much dose you score in 1st subject."))
         ele2=float(input(f"Now {name} tell me marks of 2nd subject."))
         ele3=float(input("Bro tell me marks of 3rd subject."))
         ele4=float(input(f"{name} what was your score in 4th subject."))
         ele5=float(input(f"{name} how much dose you score in 5th subject."))
         ele6=float(input(f"{name} ,how much dose you score in 6th subject."))
         ele7=float(input("So, tell how much dose you score in 7th subject."))
         ele8=float(input(f"Hey {name} now tell score of 8th subject"))
         ele9=float(input("Now tell, how much did you score in 9th subjct"))
         ele10=float(input("Now tell, what is the score in 10th subjct"))
         ele11=float(input("Now tell, what is the score in last subjct"))
         total11=float(input("Now tell, what is total marks of each subjct"))
         score11=ele1+ele2+ele3+ele4+ele5+ele6+ele7+ele8+ele9+ele10+ele11
         scorepercent11=(score11/(total11*11))*100
         print (f"So {name}, you have score {scorepercent11}%, and I believe you can do much better.")
   else:
      two1=float(input(f"{name}, how much dose you score in 1st subject."))
      two2=float(input(f"Now {name} tell me marks of 2nd subject."))
      two3=float(input("Bro tell me marks of 3rd subject."))
      two4=float(input(f"{name} what was your score in 4th subject."))
      two5=float(input(f"{name} how much dose you score in 5th subject."))
      two6=float(input(f"{name} ,how much dose you score in 6th subject."))
      two7=float(input("So, tell how much dose you score in 7th subject."))
      two8=float(input(f"Hey {name} now tell score of 8th subject"))
      two9=float(input("Now tell, how much did you score in 9th subjct"))
      two10=float(input("Now tell, what is the score in 10th subjct"))
      two11=float(input("Hey tell me marks of 11th subject"))      
      two12=float(input("Now tell, what is the score in last subjct"))
      total12=float(input("Now tell, what is total marks of each subjct"))
      score12=two1+two2+two3+two4+two5+two6+two7+two8+two9+two10+two11+two12
      scorepercent12=(score12/(total12*12))*100
      print (f"So {name}, you have score {scorepercent12}%, and I believe you can do much better.")
else:
   print(f"{name}, I am only able to calculate marks of minum 8 subject an max 12 subject only, sorry for that I can only calculate between 12 and 7 subject")
y=input("Press enter to exit")