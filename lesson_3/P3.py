def numbers(num1, num2,num3):
    my_list = [num1, num2, num3]
    try:
        my_list.remove(min(my_list))
        return sum(my_list)
    except TypeError:
        print('Enter a numbers!!!')

print(numbers(1,2,3))