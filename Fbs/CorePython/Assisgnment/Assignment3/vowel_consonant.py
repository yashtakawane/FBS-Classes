#Write a program to input any alphabet and check whether it is vowel or consonant.
alpha = input('Enter the Alphabet:')
vowel = ['a','e','i','o','u']
if(alpha in vowel):
    print(f'The alphabet is Vowel')
else:
    print('The alphabet is a consonent')