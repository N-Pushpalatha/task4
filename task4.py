mark1=int(input("Enter the tamil mark:"))
mark2=int(input("Enter the english mark:"))
mark3=int(input("Enter the maths mark:"))
mark4=int(input("Enter the computer mark:"))
mark5=int(input("Enter the phy mark:"))
mark6=int(input("Enter the ac mark:"))
if(mark1>mark2 and mark1>mark3 and mark1>mark4 and mark1>mark5 and mark1>mark6):
  print("maximum mark =",mark1)
elif(mark2>mark3 and mark2>mark4 and mark2>mark5 and mark2>mark6):
  print("maximum mark =",mark2)
elif(mark3>mark4 and mark3>mark5 and mark3>mark6):
  print("maximum mark =",mark3)
elif(mark4>mark5 and mark4>mark6):
  print("maximum mark =",mark4)
elif(mark5>mark6):
 print("maximum mark =",mark5)
else:
 print("maximum mark=",mark6)

mark1=int(input("Enter the tamil mark:"))
mark2=int(input("Enter the english mark:"))
mark3=int(input("Enter the maths mark:"))
mark4=int(input("Enter the computer mark:"))
mark5=int(input("Enter the phy mark:"))
mark6=int(input("Enter the ac mark:"))
if(mark1<mark2 and mark1<mark3 and mark1<mark4 and mark1<mark5 and mark1<mark6):
  print("Minimum mark =",mark1)
elif(mark2<mark3 and mark2<mark4 and mark2<mark5 and mark2<mark6):
  print("Minimum mark =",mark2)
elif(mark3<mark4 and mark3<mark5 and mark3<mark6):
  print("Minimum mark =",mark3)
elif(mark4<mark5 and mark4<mark6):
  print("Minimum mark =",mark4)
elif(mark5<mark6):
 print("Minimum mark =",mark5)
else:
 print("Minimum mark=",mark6)