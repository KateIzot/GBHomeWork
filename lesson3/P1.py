def division_num(num_1, num_2):
    try:
        num_1, num_2 = float(num_1), float(num_2)
        div_num = num_1 / num_2
    except ZeroDivisionError:
        return "can't divide by zero"
    return (div_num)

print(division_num(float(input('Enter first number')), float(input('Enter second number'))))
