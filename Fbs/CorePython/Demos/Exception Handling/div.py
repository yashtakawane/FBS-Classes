# num1=int(input('Enter the number 1:'))
# num2=int(input('Enter the number 2:'))
try:#try needs atleast one except or final statement
   num1=int(input('Enter the number 1:'))
   num2=int(input('Enter the number 2:')) 
   print(num1//num2)
except ZeroDivisionError as a: #it is specialized exception
   print(f"I am in ZeroDiv",a)
except ValueError as v:
   print(f'Value err={v}')
except Exception as e:#this is genralized which always comes after specialized expection
   print(e)

else:#it execute when there is no exception in application
   print('I am in else block')

finally:#it executes in any situation
   print('I am in finally block')
