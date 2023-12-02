import re

def CheckInput(tmpamt):
   pattern = pattern = r"^[-+]?[0-9]*\.?[0-9]+$"
   match = re.match(pattern, tmpamt)
   if bool(match) == False:
      tmpamt = input('Please enter correct value: ')
      CheckInput(tmpamt)
   return float(tmpamt)
    
amount = CheckInput(input('Enter Total amount of food purchased: '))
tip = (amount/100)*18
salesTax =  (amount/100)*7
total = amount+tip+salesTax

print('\n\n*********************** RECEIPT *****************************')
print('\nPrice of Food Purchased :', end =' $')
print('{:.2f}'.format(amount))
print('Tip :', end='                     $')
if tip < 10:
   print('0',end='')
print('{:.2f}'.format(tip))
print('Sales Tax :', end='               $')
if salesTax < 10:
   print('0',end='')
print('{:.2f}'.format(salesTax))
print('\ntotal :', end='                   $')
print('{:.2f}'.format(total))
print('\n*********************** End *********************************')