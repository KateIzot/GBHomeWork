my_list = [12, 'kate', True, 13.5, 777, False, 'kot']
my_list1 = my_list.copy()
print(my_list1)

while True:
    print(type(my_list1.pop()))
    print(my_list1)
    if my_list1 == []:
        print('no more items in the list')
        break

print(my_list)

