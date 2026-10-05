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


# logical operators: and, or, not, is -> (Compares object identity)

age = 20

if age > 18 and age < 60:
    print('Can drive')
else:
    print('Cannot drive')


# Object Identity

a = [1, 2]
b = [1, 2]

print(a is b)       # Returns False
print(a == b)       # Returns True


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
list1.append("Another")
list1.remove("Another")
list1.pop()                       # Remove and Return Last Index
popped = list1.pop(1)             # Remove and Return by index!
print(popped)
print(list1)                      
print(list1[-2])                  # Second Last Element
print(len(list1))

list1.sort()       
print(list1)                      # Throws error since comparison b/w str and int is not supported

print(list1.count("Apple"))       # Counts Frequency
print(list1[1:5])                 # Extracts Subarray or SubList from index 1 to 4!   

# 2. TUPLES: Immutable Lists, cannot be modified

tup1 = (220, 255, 34)             # Constant Values, for example can store an rgb value
tup1[0] = 230                     # INVALID!

# 3. Dictionaries: Equivalent to hash-maps

person = {
    "name" : "Darshan",
    "age" : 20,
    "job" : "Software Engineer",
    "isGraduated" : False
}

print(person["age"])

# iteration format:

for key, value in person.items():
    print(key, " -> ", value)

# Separate:

print(type(person.keys()))      # <class 'dict_keys'>
print(type(person.values()))    # <class 'dict_values'>
print(type(person.items()))     # <class 'dict_items'>

# Special Use:

print(person["cgpa"])           # Returns Error
print(person.get("cgpa"))       # Returns None
print(person.get("cgpa", "not available"))  # Returns not available string


# 4. SETS: Equivalent to unordered_set in C++

s1 = set()                      # Initializing an empty set, not {}, because thats a dictionary

array = [1, 2, 3, 4, 4, 5, 6, 7, 8, 8, 9, 10]
s1 = set(array)
print(s1)                       # Removes duplicate
print(type(s1))                 # <class 'set'>

# Sets are exclusively used for membership testing and set operations
# and do not support indexing

print(s1[1])                    # Invalid

# Iteration

for i in s1:
    print(i)

# Membership test

flag = False

if 100 in s1:
    flag = False
else:
    flag = True

print(flag)

# Set Operations

A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}

print(A | B)                # Union
print(A & B)                # Intersection
print(A - B)                # Difference
print(A ^ B)                # Symmetric Difference, kind of like XOR

# A ^ B = (A | B) - (A & B)

# Functions:

def speak():
    print("hello")
    return

def power(base, power = 2):     #power can be passed, else its assumed to be 2
    return base ** power

print(power(5, 3))              # 125
print(power(5))                 # 25

# Using functions like this:

print(power(base = 10, power = 2)) # Used when writing complex fns, like model.fit(), etc

# Type Hinting:

def bin_search(array: list[int], target: int) -> int:    # Python does not enforce them during the runtime
    l = 0
    r = len(array) - 1
    while l <= r:
        m = l + (r - l) // 2                # In Python / results in float division
        num = array[m]                      # Resulting in type incompatibility, we must 
                                            # use // for integer division
        if num == target:
            return m
        elif num > target:
            r = m - 1
        else:
            l = m + 1
    return -1

array = [2, 4, 6, 10, 12, 20, 22]
target = 10

found_index = bin_search(array, target)
print(found_index)

target2 = 11
found_index = bin_search(array, target2)
print(found_index)