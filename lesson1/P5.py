vyr = int(input('Enter revenue'))
izd = int(input('Enter costs'))
rez = vyr - izd
if rez > 0:
    rent = rez / vyr
    people = int(input('enter the number of employees'))
    retn_people = rez / people 
    print('Everything is fine. Рrofitability is {:.2f}, profit per person is {:.2f}'.format((rent), (retn_people)))
else:
    print('bad. need to work harder')
