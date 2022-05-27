from bisect import insort_right


my_list = [8, 7, 7, 6, 6, 6, 5, 4, 4, 3, 2, 2, 1]

while True:
    new_el = input('enter a new rating element')
    if new_el.isdigit():
        my_list.append(int(new_el))
        my_list.sort(reverse=True)
        print(my_list)
    elif new_el == 'x':
        break 
