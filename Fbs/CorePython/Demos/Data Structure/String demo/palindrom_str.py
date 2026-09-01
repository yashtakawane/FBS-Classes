def chkPalindromString(str):
    rev_str=''
    for char in str:
        rev_str=char+rev_str

    if(str==rev_str):
        print('String is palindrome')
    else:
        print('String is not palindrome')

str=input('Enter the string:')
chkPalindromString(str)
