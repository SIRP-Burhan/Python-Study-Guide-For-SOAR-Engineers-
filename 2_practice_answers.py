#2.5.1

A = [1, 2, 3]
B = [4, 5, 6]

cross_product = [(a, b) for a in A for b in B]
print(f"Answer for 2.5.1: {cross_product}")

#2.5.2

def is_palindrome(s):
    return s == s[::-1]

def palindromic_substrings(s):
    palindromes = []
    n = len(s)
    for i in range(n):
        for j in range(i+1, n+1):
            substring = s[i:j]
            if is_palindrome(substring):
                palindromes.append(substring)
    return palindromes

s = "madam"
result = palindromic_substrings(s)
result.sort()
print(f"Answer for 2.5.2: {result}")

#2.5.3

def word_frequency(text):
    # Remove punctuation by replacing each special character with a space
    punctuation = ".,!?;:'\"()[]{}<>-"
    for char in punctuation:
        text = text.replace(char, " ")
    
    # Convert to lowercase
    text = text.lower()
    
    # Split the text into words
    words = text.split()
    
    # Initialize an empty dictionary to count frequencies
    frequency = {}
    
    # Count the occurrences of each word
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    
    return frequency

# Example usage:
paragraph = "Hello world! Hello, Python. This is a test. Test, this is."
result = word_frequency(paragraph)
print(f"Answer for 2.5.3: {result}")


#2.5.4

def print_hexadecimal(file_path):
    with open(file_path, 'rb') as file:
        content = file.read()
        hex_output = content.hex()
        formatted_hex = ' '.join(hex_output[i:i+2] for i in range(0, len(hex_output), 2))
        print(formatted_hex)

# Example usage (make sure to replace 'example.bin' with your actual file path):
# print_hexadecimal('example.bin')
