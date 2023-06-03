print('---pricing---') 
print('1-9   | 3 Baht')
print('10-99 | 2 Baht')
print('>99   | 1 Baht')
print('--------------')

quntity = int(input("Amount of copy:"))
print(f'Amount = {str(quntity)} sheet of paper')

if quntity>=1 and quntity<=9:
  cost = quntity*3
elif quntity>=10 and quntity<=99:
  cost = ((quntity-9)*2)+27
else:
  cost = (quntity-99)+178+27 #(9)*3 + (99-10)*2 + (count-99)*1

print(f'Cost : {str(cost)}')

money = int(input("How much you will pay : "))
balance = money-cost
if money >= cost:
    print(f'Your change : {str(balance )} Baht')
    changes = {100: 0,50: 0,20: 0,10: 0,5: 0,1: 0,}
    for change in changes:
        surplus = max(0,balance //change)
        balance =surplus*change
        changes[change] = int(surplus)
    print(changes)
elif money < cost:
    print(f"Please put more money, another {abs(balance )} bath is missing")
else:
    print('Error: InsufficientFunds')