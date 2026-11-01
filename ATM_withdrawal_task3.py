account_balance=int(input("enter account balance:"))
withdrawal_amount=int(input("enter withdrawal amount:"))

if(account_balance<0):
  print("invalid")
elif(withdrawal_amount==0):
  print("Enter a valid withdrawal amount")
elif(withdrawal_amount>account_balance):
  print("insufficient balance")
else:
  if(withdrawal_amount%100==0):
    remaining_balance=account_balance-withdrawal_amount
    print("withdrawl successful!")
    print("remaining amount",remaining_balance)

  else:
    print("Enter an amount in multiples of 100")

