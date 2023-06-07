#Split in Half
#Given a string. Split it into two equal parts. Swap these parts and return the result.
#If the string has odd characters, the first part should be one character greater than the second part.
# initializing string
import math

name = "bharathirajaram"

# printing original string
print("The original string is : " + name)
#find name length
name_length = len(name)
#find highest mid point so we are using ceil function
mid_point = math.ceil(name_length/2)

#get first part of name using mid_point

first_name = name[:mid_point]
print("first part greater than second part;",first_name)
#get last part of name using mid_point
last_name = name[mid_point:]
print("second half of the name:",last_name)

#first_name,last_name = name[:mid_point],name[mid_point:]

full_name=last_name+first_name
print ("name in reverse order   ",full_name)







#Given a string, determine if it consists of all unique characters.

def isUniqueChar(name) :
    #loop through the all chars from given name string
    for i in name:
        #find that char how many times occuring in that string
        charscount = name.count(i)
        #if its occuring more than once,return false
        if charscount > 1:
            print(f'No unique chars in the name. Charactor {i} is occuring {charscount} times')
            return False
    #if all chars occurs only once, function returns true
    print(f'Name {name} has ONLY unique chars')
    return True


name = "moohaan"
Isvalid=isUniqueChar(name)
print("Is Unique chars in String",Isvalid)
