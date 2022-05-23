ent_month = int(input('Enter the month of the year (in numbers)'))
my_dict_month = {1:'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
my_list_month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

if ent_month in my_dict_month:
    print(f'{ent_month} - {my_dict_month[ent_month]}')
    print(f'{ent_month} - {my_list_month[ent_month -1]}')
else:
    print('enter the correct number')