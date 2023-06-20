#Compute the sum of digits in all numbers from 1 to n. When a function gets a number n, find the sum of digits in all numbers from 1 to n.

n = int(input("enter the n value: "))

sum = 0
for i in range(1,n):
    sum = sum+i
print("sum of n numbers:",sum)

#Find the max number from 3 values.
#Example: 124, 21, 32. Result = 124.

firstnumber=124
secondnumber = 21
thirdnumber = 32
if firstnumber>secondnumber and firstnumber>thirdnumber:
    print ("maximum number is firstnumber:",firstnumber)
elif secondnumber>thirdnumber :
   print(secondnumber)
else: print(thirdnumber)

#Count odd and even numbers of the wholenumbers.

wholenumber = input ("enter the wholenumber;")
wholenumber = int (wholenumber)


evensum = 0
oddsum = 0

while wholenumber > 0:
    lastdigit = wholenumber%10
    if lastdigit% 2 == 0:
        evensum += lastdigit
    else:
        oddsum += lastdigit
    wholenumber = wholenumber // 10

print ("Evensum:% d, oddsum:% d"% (evensum, oddsum))


