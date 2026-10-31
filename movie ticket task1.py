age=int(input("Enter your age:"))
show_type=input("enter show type: normal or premium:")

if(age<0):
   print("invaild")
elif(show_type not in("normal","premium")):
     print("invaild")
else:
  if(age<5):
    print("ticket is free")
  elif(age<=17 and show_type=="premium"):
    print("premium show ticket price is 200")
  elif(age>=18 and show_type=="premium"):
    print("premium show ticket price is 300")
  else:
    if(age<5):
      print("ticket is free")
    elif(age<=17 and show_type=="normal"):
      print("normal show ticket price is 100")
    elif(age>=18 and show_type=="normal"):
      print("normal show ticket price is 200")

