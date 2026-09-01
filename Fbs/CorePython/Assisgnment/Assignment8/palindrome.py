#WAP to check whether entered number is palindrome or not
def palindrome(n):
    rev=0
    temp=n
    while(n>0):
        d=n%10
        n=n//10
        rev=rev*10+d
    if(temp==rev):
        print('The number is palindrome')
    else:
        print('The number is not palindrome')

n=int(input('Enter the number to check palindrome:'))
palindrome(n)


