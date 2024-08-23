"""
2_intermediate_python.py

What to cover:
2.1 List Comprehension & Slicing
2.2 String Manipulation
2.3 File Handling
2.4 Exception handling
2.5 Practice Questions
2.6 Test Your Might!

"""
######################################################################################################################################################################

#2.1 List Comprehension and Slicing
print(f"List Comprehension and Slicing\n")

# Present list
int_list = [1,2,3,4,5,6,7,8,9,10]

#Lets generate a new list that stores squares of all even numbers from int_list
#2 ways to do this; loop and list comprehension

#using for loop

evenSquares_1=[]
for num in int_list:
    if num%2==0:
        evenSquares_1.append(num**2)
print(f"Using For Loop: {evenSquares_1}")

#using list comprehension
evenSquares_2=[num**2 for num in int_list if num%2==0]
print(f"Using List Comprehension: {evenSquares_2}\n")

#Syntax for list comprehension
#new_list = [item for item in items if *some condition*]

#Now Lets move on to Slicing
#Slicing is a way to manipulate traversing of strings and elemnts of list

str1 = "Hello Worlds!"
print("First Slice example: "+str1[2:5]) #Output First Slice example: llo
print("Second Slice example: "+str1[::2]) #Output Second Slice example: HloWrd!
                                          #From index 0, traverse over every other element

print("Third Slice example: "+str1[3::3]) #Output Third Slice example: lWl!
                                          #From index 3, traverse skipping every 2 elements

print("Fourth Slice example: "+str1[::-1]) #Output Fourth Slice example: !sdlroW olleH
                                          #traverse in reverse
                    
print(f"Print Multiples of 4 from int_list: {int_list[3::4]}\n") #Output Print Multiples of 4 from int_list: [4, 8]

######################################################################################################################################################################

#2.2 String Manipulation
print("2.2 String Manipulation\n")

#https://www.w3schools.com/python/python_ref_string.asp contains all string related 
#functions but lets go over the most important of them

#capitalize and un-capitalize
capital_str = str1.upper()
un_capital_str = str1.lower()

print(f"Capital: {capital_str}, All Lower Case: {un_capital_str}") #Output Capital: HELLO WORLDS!, All Lower Case: hello worlds!

#Capitalize only the first character of each word
print(f"Capitalizing only the first character of each word: {un_capital_str.title()}\n") #Output Capitalizing only the first character of each word: Hello Worlds!

#Spliting the strings at line breaks and storing each word in a list, by deafault it breaks strings at white spaces
string_list = "Just some meaningless string for demo"
print(f"Here is the list of words: {string_list.split()}") #Output Here is the list of words: ['Just', 'some', 'meaningless', 'string', 'for', 'demo']

#Finding the index of some character in the string
print(f"The character 'd' is at index: {string_list.find('d')}\n") #Output The character 'd' is at index: 33

#finding ascii value of a string and vice versa
print(f"the ascii value of {string_list[3]} is {ord(string_list[4])}")
print(f"the character at ascii value {69} is {chr(69)}\n")

#Remember one thing, these manipulation methods don't chamge the original string. In order to 
#implement the changes, we have to store them. Explaination:
string_list.upper()
print(string_list+"\n") #Expected Output: JUST SOME MEANINGLESS STRING FOR DEMO
                   #Output: Just some meaningless string for demo

######################################################################################################################################################################

#2.3 File Handling
print("2.3 File Handling\n")

#open(): opens a file and returns a file object.
file = open("example.txt", "r")  # Open a file for reading 
file.close()  # Always close the file after use

#read(): Reads the entire file content.
with open("example.txt", "r") as file: #using with keyword allows automatic closing of file
    content = file.read()
    print(content)

#readline(): Reads a single line from the file
with open("example.txt", "r") as file:
    first_line = file.readline()
    print(first_line)

#readlines(): reads all lines into a list
with open("example.txt", "r") as file:
    lines = file.readlines()
    print(lines)

#write(): Write a string to the file
with open("example.txt", "w") as file:
    file.write("Hello, World!")

#writelines(): Writes a list of strings to the file.
lines = ["Hello, World!", "Python is awesome!"]
with open("example.txt", "w") as file:
    file.writelines(lines)

# "r": Read mode (default)
# "w": Write mode (truncates the file if it exists)
# "a": Append mode (adds content to the end of the file)
# "b": Binary mode (used for binary files like images)
# "r+": Read and write mode
print("\n")

######################################################################################################################################################################

#2.4 Exception Handling
print("2.4 Exception Handling\n")

#try and except: To handle exceptions.
try:
    x = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

#finally block will execite no matter what
try:
    file = open("example.txt", "r")
except FileNotFoundError:
    print("File not found!")
finally:
    file.close()

print("\n")

######################################################################################################################################################################

#2.5 Practice Questions
print("Practice Questions\n")

#2.5.1
#Create a list comprehension that computes the cross product of two lists A and B, where A = [1, 2, 3] and B = [4, 5, 6].
#Expected Output: [(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]

#2.5.2
#Write a function that takes a string and returns all palindromic substrings within it.
#s = "madam"
# Expected Output: ["m", "a", "d", "a", "m", "ada", "madam"]

#2.5.3
#Given a paragraph of text, count the frequency of each word (case-insensitive) using a dictionary.
#Ignore punctuation and special characters.

#2.5.4
#Write a program that reads a binary file and prints its contents in hexadecimal format.

######################################################################################################################################################################

#2.6 Test Your Might!
print("Test Your Might!\n")

#2.6.1
#Given a list of text files, write a program that merges them into a single file. 
#Ensure that the contents are merged in alphabetical order based on the filename.

#2.6.2
#Implement a function that compresses a string by replacing sequences of the same 
#character with that character followed by the number of repetitions.
#For example, "aabcccccaaa" should become "a2b1c5a3". If the compressed string is not
#shorter than the original, return the original string.

#2.6.3
#Given a string, write a list comprehension to generate all possible permutations of its characters.
