#read mode
f=None
try:
    f=open('abc.txt','r')
    data=f.read()
    if not data:
        raise Exception("File is empty")
except Exception as e:
    print(e)
else:
    print(data)
finally:
    if f is not None:
        print("File is close")
        f.close()

print('I am outside abc')