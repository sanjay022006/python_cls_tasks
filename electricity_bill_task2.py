units=int(input("enter unit consumed:"))

if(units<0):
  print("invalid units")
else:
  if(units<=100):
    rate=2
  elif(units<=200):
    rate=3
  elif(units<=300):
    rate=5
  else:
    rate=7

  bill=units*rate
  if bill>1000:
   discount=bill*10/100
  else:
   discount=0

  final_bill =  bill-discount
  print("bill amount:",bill)
  print("discount:",discount)
  print("final bill:",final_bill)