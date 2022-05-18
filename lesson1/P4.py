num = int(input('Enter numb'))
num_max = -1
while num > 10:
    d = num % 10
    num //= 10
    if d > num_max:
        num_max = d
print(num_max)