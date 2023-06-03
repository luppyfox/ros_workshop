print('---pricing---') 
print('1-9   | 3 Baht')
print('10-99 | 2 Baht')
print('>99   | 1 Baht')
print('--------------')

count = int(input("Amount of copy:"))
print(f'Amount = {str(count)} sheet of paper')

if count>=1 and count<=9:
  cost = count*3
elif count>=10 and count<=99:
  cost = ((count-9)*2)+27
else:
  cost = (count-99)+178+27 #(9)*3 + (99-10)*2 + (count-99)*1

print(f'Cost : {str(cost)}')

money = int(input("How much you will pay : "))
sum = money-cost
if money >= cost:
    print(f'Your change : {str(sum)} Baht')
    changes = {100: 0,50: 0,20: 0,10: 0,5: 0,1: 0,}
    for change in changes:
        surplus = max(0,sum//change)
        sum-=surplus*change
        changes[change] = int(surplus)
    print(changes)
elif money < cost:
    print(f"it's don't have enough money, another {abs(sum)} bath is missing")
else:
    print('Error: InsufficientFunds')
