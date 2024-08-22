#1.5.1

# Taking two numbers as input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Performing arithmetic operations
sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2 if num2 != 0 else "undefined (division by zero)"

# Printing the results
print(f"Sum: {sum_result}")
print(f"Difference: {difference}")
print(f"Product: {product}")
print(f"Quotient: {quotient}")

print("\n")
#################################################################################################

#1.5.2

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
# Printing prime numbers between 1 and 100
print("Prime numbers between 1 and 100:")
for num in range(1, 101):
    if is_prime(num):
        print(num, end=" ")

print("\n")

#################################################################################################

#1.5.3

def find_highest_with_index(int_list):
    if not int_list:  # Check if the list is empty
        return None
    highest = int_list[0]
    highest_index = 0
    for index, value in enumerate(int_list):
        if value > highest:
            highest = value
            highest_index = index
    return highest, highest_index
# Example usage:
numbers = [3, 5, 7, 2, 8, 6]
result = find_highest_with_index(numbers)
print(f"The highest number is {result[0]} at index {result[1]}")

print("\n")

#################################################################################################

#1.5.4

def print_student_grades(student_grades):
    for student, grade in student_grades.items():
        print(f"Student: {student}, Grade: {grade}")

# Creating a dictionary with student names and their grades
students = {
    "Alice": "A",
    "Bob": "B+",
    "Charlie": "A-",
    "David": "B",
}

# Printing the students and their grades
print_student_grades(students)

#################################################################################################