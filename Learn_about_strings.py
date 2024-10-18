name = "ganesh Malepati"
print(len(name))
print(name.endswith("pati"))
print(name.startswith("gane"))
print(name.startswith("hey"))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.find("e"))
print(name.count("a"))
s_1 = "Can i know how many times you can eat a day \nThree times in a day \nThat's Good "
print(s_1)
s_2 = "Ganesh  is working on  something"
index = -1
# i = 0
count = 0
for i in range(len(s_2)-1):
    if s_2[i] == ' ' and s_2[i+1] == ' ':
        count += 1
        index = i
    i += 1
print(index)
print(count)




# To reverse a string

def reverseString(s):
    reverse_s = ""
    for char in s:
        reverse_s = char + reverse_s
    return reverse_s
s = input("Enter a string: ")
print(reverseString(s))


def ReverseBySlice(s):
    return s[::-1]
s = input("Enter a string: ")
print(ReverseBySlice(s))


# To check whether its a Palindorme or not

def Palindrome(s):
    s = s.replace(" ", " ").lower()
    left = 0
    right = len(s)-1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
s = input("Enter a string: ")
print(Palindrome(s))



# To find the number of vowels and it's count in a provided string
def Vowels_in_String(s):
    vowels = ('aeiouAEIOU')
    count = 0
    found_vowels = set()
    for char in s:
        if char in vowels:
            count += 1
            found_vowels.add(char)
    return count, found_vowels

s = input("Enter a string: ")
print(Vowels_in_String(s))

# The find the occurence of each charater in a string

def Occurence_of_char(s):
    new_str = {}
    for char in s:
        if char in new_str:
            new_str[char] += 1
        else:
            new_str[char] = 1
    return new_str
s = input("Enter a string: ")
print(Occurence_of_char(s))


# The Frequency of each character

def Frequency_of_each_char(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    most_common_char = max(char_count, key=char_count.get)
    most_common_count = char_count[most_common_char]
    return most_common_char, most_common_count
    pass
s = input("Enter a string: ")
print(Frequency_of_each_char(s))

# To Remove the duplicate elements 

def Remove_Duplicate_result(s):
    seen = set()                  # Here a set is defined and set not allows duplicate values
    result = []                   # the final result is stored here
    for char in s:
        if char not in seen:
            seen.add(char)        # when a char is unique it will store in seen set()
            result.append(char)   # After removing the duplicate values each unique char are stored in result list
    return ''.join(result)        # This will Join all the values
s = input("Enter a string: ")
print(Remove_Duplicate_result(s))

