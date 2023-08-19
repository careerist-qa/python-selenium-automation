"""
HW 5
4** Amazon interview question:
Create a function that will take a string as an input
and print the 1st unique letter of a string.
"google" => l
How would you test it? How would you handle edge cases?

"""
def unique(string: str):
    # Google => google
    string = string.lower()  # google

    d = {}
    for letter in string: # O(n)
        if letter not in d:
            d[letter] = 1
        else:
            d[letter] += 1

    # print(d) # d = {'g': 2, 'o': 2, 'l': 1, 'e': 1}

    for k, v in d.items(): # O(n)
        if v == 1:
            return k
    return ''
    # O(n)

print(unique('google'))
print(unique('Google'))
print(unique(''))
print(unique('gogo'))









