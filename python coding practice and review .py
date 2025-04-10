
#Lesson 2 on Numbers and Variables
    #integer = whole nunmber 4
    #float = number with decimal point 4.5
    #floor division = counting the quotient using // symbol 9//2=4
    #remainder= remaining number after dividing: 6%4=2
    #exponentiation **, 6**2 = 36

    #Variables
        #Stores information that can be retrieved later on
        #can be reassigned values
        #cannot be a keyword
        #cannot start with a number
        #cannot contain spaces
        #CAN have an underscore
        #CAN have numbers within, just not to begin with
        #are case sensitive
    #Data Types
        #Boolean= True or False values
        #Dictionaries --> store multiple items of data as a list-- key:value pairs, values are referenced by key {'name':'Bob}
        #Set--> restrictive python list w unique values separated by commas inside curly braces set = {'Alpha',"Bear'}
        #string= type of text data type enclosed by quotes, string = 'Number of kids'
        #List = allows us to store info in a specific order. We can add, remove, or modify elements after creating the list
            #example, list = [1,2,3,4,5]
        #Tuple--> a collection of elements which cannot be changed or reversed, represented by parenthesis
            #tuple=(1,2,3,4,5)

#Lesson 3: Strings
    #enclosed within single '' or double "" quotes
    #can contain letters, numbers, symbols, and even empty spaces
    #triple quotes will break down string into multiple lines
    #\n breaks code into a separate line

    #concatenation
        #uses a + symbol to concatenate or join variables and text together
        #Example:
Book ='Coding for Python'
copyright_year = 2002
print("The book"+Book +"was written in" + str(copyright_year))

#.format() method
print('Hi there, {}'.format('Pooja'))
print("{0} and {1}".format('Pooja','Patel'))

#F-strings
    #Do not need to use + symbol or conversions
Age = 31
Name= 'Pooja'
print(f'{Name} is {Age} years old.')
print(len(Name))
print(str.upper(Name))
print(str.lower(Name))
print(str.count(Name,'oo'))
#str.replace('old','new')--> replacing variables
#str.count('letter')--> counts number of times something appears in a string


text = input('Enter the text to be formatted: ')
print("UPPERCASE:" + text.upper())
print(text.lower())
print(text.title())
print(len(text))

sentence = input("Enter a sentence: ")
new_word = input("Enter the word to replace: ")
letter = input("Enter the letter to count: ")
print(sentence.replace(new_word, sentence))
print(sentence.count(letter))


#Slicing
    #index--> refers to numerical position of an element within a string, uses square brackets [] to indicate index position
    # indices can be positive or negative, starts with 0 from the left side and -1 on the right side
string = "Python"
print(string[0:3]) #--> regular string
print(string[-1:-3:-1]) #--> reversing a string

sliced_sentence = 'Python programming is fun!'
print(sliced_sentence[7:18])
print(sliced_sentence[0:25:3])
print(sliced_sentence[::-1])


#Lesson 4: Boolean
    #data type that has only 2 possible values, True or False
    #conditional operators
        # < less than
        # < = less than or equal to
        # > greater than
        # > = greater than or equal to
        # == equal
        # != does not equal
    #If Statement = evaluates a given condition and if the condition is true, it executes a specific block of code
    #Else Statement = executes other code when all other possibilities are false
    # Elif Statement = another option to consider
    #AND, OR, NOT = Boolean operators

age = int(input('Enter your age:'))

if age >= 18:
    print('You are eligible to vote')
else:
    print('You are not eligible to vote')


grade = int(input("Enter student’s grade: "))

if grade >= 90:
    print('You\'ve got an A')
elif grade >= 80:
    print('You\'ve got an B')
elif grade >= 70:
    print('You\'ve got an C')
elif grade >= 60:
    print('You\'ve got an D')
else:
    print('You\'ve got an F')

#Lesson on Lists:
 # iterate means to walk over each
 # first element of a list has an index of 0
 # lists are always declared using square brackets