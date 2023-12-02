Grocery_List = ['Milk','Eggs','Jam']
print('Item List: ', end ='\n')
for i in Grocery_List:
    print(i, end='\n')
print()
Grocery_List = [['Milk', 1], ['Eggs', 12], ['Jam', 1]]
print('Item List: ')
for i in Grocery_List:
    for j in i:
        print(j, end= '  ')
    print()
