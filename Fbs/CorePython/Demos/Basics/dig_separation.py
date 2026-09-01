num = 457

d1 = num % 10 #sep digit 7
num = num // 10 #gives 45 & overwrite 457

d2 = num % 10  #gives digit 5
num = num // 10 #repeats same overwrite 4 over 45

d3 = num % 10  #gives digit 4
num = num // 10

print(f'd1:{d1}, d2:{d2}, d3:{d3}')