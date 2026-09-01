#Convert the time entered in hh,min and sec into seconds.

h = int(input("Enter hours: "))
m = int(input("Enter minutes: "))
s = int(input("Enter seconds: "))

total_seconds = (h * 3600) + (m * 60) + s

print(f'Total seconds in given time is {total_seconds}')