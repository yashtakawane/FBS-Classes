#Write a program to check if user has entered correct userid and password.
userid = input('Enter the userid:')
password = input('Enter thr password:')

if((password == 123) and (userid == 1234)):
    print('Password and userid is valid')
else:
    print('Password and userid is not valid')