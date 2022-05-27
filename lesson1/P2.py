sec = int(input('Enter time in seconds'))

second = sec % 3600 % 60
hour = sec / 3600
minute = sec % 3600 / 60

print("%02d:%02d:%02d" % (hour, minute, second))
