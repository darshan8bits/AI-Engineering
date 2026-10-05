# Getting / Checking / Converting variable types

a = 10
b = 10.5
c = "Darshan"

print(type(a))
print(type(b))
print(type(c))

#Invalid:
newint = int(c)
print(newint)

#Valid:
newstr = str(a)
print(newstr * 2) #Prints 1010, not 20

newbool = bool(40)
print(newbool)    #Anything other than 0 prints true!


# logical operators: and, or, not, is -> (Compares objects of same instance)

age = 20

if age > 18 and age < 60:
    print('Can drive')
else:
    print('Cannot drive')

# fstrings

name = "Darshan"
sentence = f"Hi my name is {name} "

print(sentence)

# String methods: Mostly look them up, since there are a lot of them

s2 = sentence.upper()
s3 = sentence.lower()
s4 = sentence.title()

print(s2, s3, s4)

# Loops

for i in range(1, 7):  # 1 to 6, 7 is exclusive
    print(i)

# while loops work similar to c++ syntax: while(condition) is used

# Data Structures

# 1. LISTS: Equivalent to Arrays

list1 = ["Apple", 10, True, ["Hello", "Second List"]]
print(list1[0])
for item in list1:
    if isinstance(item, list):
        print(item[0])
list1.append("Last Element")
print(list1[-2])                  # Second Last Element
print(len(list1))

list1.sort()       
print(list1)                      # Throws error since comparison b/w str and int is not supported

print(list1.count("Apple"))       # Counts Frequency
print(list1[1:5])                 # Extracts Subarray or SubList from index 1 to 4!   
