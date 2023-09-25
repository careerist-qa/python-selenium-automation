def reverse_negative_number(n: int):
    string = str(n)
    if string[0] == '-':
        return int('-' + string[:0:-1])
    else:
        return int(string[::-1])

print(reverse_negative_number(-456))


def is_anagram(s1: str, s2: str):
    s1 = s1.lower()
    s2 = s2.lower()

    if len(s1) != len(s2):
        return False
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False

print(is_anagram(s1= "race",s2= "care"))
print(is_anagram(s1= "hEart",s2= "earth"))
print(is_anagram(s1= "rattle",s2= "battle"))

# level one done



def reverse_words(sentence: str):
    # Split the sentence into individual words using the .split() method
    words = sentence.split()

    # Create an empty list to store the reversed versions of words
    reversed_words = []

    # Iterate through each word in the list of words
    for word in words:
        # Reverse each word using string slicing with a step of -1
        reversed_word = word[::-1]

        # Append the reversed word to the list of reversed words
        reversed_words.append(reversed_word)

    # Join (.join) the reversed words back together into a single string, separated by spaces
    reversed_sentence = " ".join(reversed_words)

    # Return the final reversed sentence
    return reversed_sentence

# level 3 done

sentence = "The brown fox jumped over the fence"
result = reverse_words(sentence)
print(result)


def repeat_digits(s: str):
    # Initialize an empty string to store the result
    result = ""
    # Iterate through each character in the input string
    for char in s:
        # Convert the character to an integer
        current_num = int(char)
        # Repeat the character based on its integer value
        repeated_char = char * current_num
        # Append the repeated character to the result string
        result += repeated_char
        # Return the final result string
    return result

# Example usage:
input_str = "216"
result = repeat_digits(input_str)
print(result)



def shortcut(s: str):
    result = ""

    for char in s:
        if char not in "aeiou":
            result += char

    return result


input_str1 = "jacob"
result1 = shortcut(input_str1)
print(result1)


input_str2 = "grable"
result2 = shortcut(input_str2)
print(result2)


