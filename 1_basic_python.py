"""
1_basic_python.py

What to cover:
1.1	Variables and Data Types
1.2	Control Flow
1.3	Functions
1.4	Basic Data Structures
1.5	Practice Questions 
1.6	Test Your Might!

_Words_of_wisdom_:

Kindly read from start till the end without nit picking what interests you most. Follow the flow of this guide. 
It is designed to improve your understanding step by step in the most optimal manner.
Make sure to solve all practice questions before trying Test Your Might! section of each chapter.  

The answers provided arent the only solution and there might be better solutions out there for the problem at hand.
However, the solutions I provide will give you a holistic idea on problem solving. 

"""

#1.1 Variable and Date Types
print("1.1 Variables and Data Types\n")

x = 10          # Integer
y = 3.14       # Float
name = "Alice" # String
is_valid = True  # Boolean	

#1.2 Control Flow
print("1.2 Control Flow\n")
    #conditionals:

if x > 10:
    print("x is greater than 10")
elif x == 10:
    print("x is 10")
else:
    print("x is less than 10")

    #loops:

for i in range(5): #For loop iterates over any iterable (string, list, tuple, etc.)
    print(i)

###################################################################################

count=0
while count<5: #While loop works until the contidion is true
    print(count)
    count+=1

###################################################################################

    #break and continue statement

for i in range(10):
    if i==5:
        break #Loop exits when i equals 5
    if i % 2==0:
        continue #Skips the current iteration if i is even
    print(i) #Output 1,3,7,9

print("\n")

#1.3 Functions
print("1.3 Functions\n")

def greet(name): #defining a function
    return f"Hello {name}!"

greeting = greet("SIRP Engineer") #calling a function and storing its output

print(greeting) #Output Hello SIRP Engineer!

def greet_default(name="Guest"): #defining a function with a default value
    return f"Hello {name}!"

print(greet_default()) #Output Hello Guest!

print("\n")

#1.4 Basic Data Structures
print("1.4 Basic Data Structures\n")
    
    #Lists

fruits = ['apple','banana','cherry'] #list is declared

fruits.append('orange') #adds orange to the end of the list
print(f"{fruits}\n") #Output ['apple', 'banana', 'cherry', 'orange']

fruits.extend(['mango','grape','melon'])
print(f"{fruits}\n")#Output ['apple', 'banana', 'cherry', 'orange', 'mango', 'grape', 'melon']

fruits.insert(2, "avacado") #adding an item at a specific index in the list
print(f"{fruits}\n") #Output ['apple', 'banana', 'avacado', 'cherry', 'orange', 'mango', 'grape', 'melon']

fruits.remove('cherry') #Removing an element by passing its index
print(f"{fruits}\n") #Output ['apple', 'banana', 'avacado', 'orange', 'mango', 'grape', 'melon']

###################################################################################

    #Tuples (Ordered, immutable, collections of items)

my_tuple = (1,2,3,3,4,5)
count = my_tuple.count(3) #Returns the number of times ‘3’ appears in the tuple
print(f"{count}\n") #Output 1, as 3 only appeared once in the tuple

###################################################################################

    #Dictionaries (Unordered collection of key-value pairs, equivalent to a Hash Table)

my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
		
name_dic = my_dict['name']
print(f"{name}\n") #prints value stored in dictionary under ‘name’ (key)

key = my_dict.keys() #returns a list
print(f"{key}\n") #output [‘name’, ‘age’, ‘city’]

key_2 = my_dict.values() #returns a list
print(f"{key_2}\n") #output [‘name’, ‘age’, ‘city’]

#1.5 Practice Problem

"""
1.5.1	Write a Python program that takes two numbers as input and prints their sum, difference, product, and quotient.
1.5.2	Write a program that prints all prime numbers between 1 and 100.
1.5.3	Write a function that takes a list of integers and returns the highest integer along with its index position as a tuple. 
1.5.4	Create a dictionary that stores student names and their grades. Write a function to print out each student's name and grade.

"""

#1.6 Test Your Might!

"""
1.6.1	Write a program that simulates a basic calculator. The program should take two numbers and an operator (+, -, *, /) as input and print the result.
1.6.2	Implement a function that takes a string and returns it reversed.
1.6.3	Write a function that counts the frequency of each character in a given string using a dictionary. Return the character with highest frequency along with its value from the dictionary. 

"""




