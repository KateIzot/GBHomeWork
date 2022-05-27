my_list = input('Enter a number').split()
print('your list:', my_list)
idx = len(my_list) if len(my_list) % 2 == 0 else len(my_list) - 1
my_list[:idx:2], my_list[1:idx:2] = my_list[1:idx:2], my_list[:idx:2]
print('new list', my_list)
