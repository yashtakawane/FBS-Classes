###1. Numeric
#1. int

#int var
var = 10

#2.float
var = 3.14

#3. complex
var = 10 + 5j #real & imaginary 

print(type(var))

###2. Text

#1.str

var = "Firstbit's"
var = '"first"bit'
var = '''This is first line.
this is sec.
this is third.''' ##here different uppre quama are use as per the content inside


###note: here we can see only new value of var is available as python has overwrite and dynamic

print(type(var))

###3. Sequential
#1. List
var = [10, 20, 30, 40]

#2. tuple
var = (10, 20, 30, 40)

#3. range
var = range(1,11)

print(type(var))

###4. Ser type
#1. set
var = {10, 20, 10}

#2. frozenset
var = frozenset({10, 20, 30})

print(type(var))

###5. Mapping
#1. dictonary
var = {'id':101, 'name':'YASH'}
print(type(var))

###6. Others
#1. boolean
var = True

#2. none
var = None
print(type(var))