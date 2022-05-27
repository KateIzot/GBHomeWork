my_str = input('enter a sentence without commas').split()

for x, i in enumerate(my_str, 1):
    print(f'{x}- {i:.10}')
