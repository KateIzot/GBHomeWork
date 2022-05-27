def my_func_sum():
    sum = 0
    while True: 
        err = False
        list1 = input('enter a number separated by a space, enter "x" - exit').split()
        for n in list1:
            if n.lower() == 'x':
                return sum
            else:
                try:
                    sum += int(n)
                except ValueError:
                    err = True
        if err:
            print('Enter number incorrect')
        print(sum)


print(my_func_sum())

