#Reverse a Statement
#Build an algorithm that will print the given statement in reverse.
# input string
string = "I will become a tester"
# reversing words in a given string
s = string.split()[::-1]
l = []
for i in s:
    # appending reversed words to l
    l.append(i)
# printing reverse words
print(" ".join(l))




#Permutations
#Write a solution that will print all permutations of a string.




def permute(s, answer):
    if (len(s) == 0):
        print(answer, end="  ")
        return

    for i in range(len(s)):
        ch = s[i]
        left_substr = s[0:i]
        right_substr = s[i + 1:]
        rest = left_substr + right_substr
        permute(rest, answer + ch)


# Driver Code
answer = ""
s = input("Enter the string : ")
print("All possible strings are : ")
permute(s, answer)



#Count Characters
#Create a program that will count vowels and consonants in a string.
str1 = input("Please Enter Your Own String : ")
vowels = 0
consonants = 0
str1.lower()

for i in str1:
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
        vowels = vowels + 1
    else:
        consonants = consonants + 1

print("Total Number of Vowels in this String = ", vowels)
print("Total Number of Consonants in this String = ", consonants)
