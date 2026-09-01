#Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)
gender = input('Enter gender(M/F):')
age = int(input('Enter age:'))

if(gender == 'F'):
    if(age >= 18):
        print('Girl is eligible for marraige')
    else:
        print('Girl is not eligible for marraige')
else:
    if(age >= 21):
        print('Boy is eligilble for marraige')
    else:
        print('Boy is not eligible for marraige')
