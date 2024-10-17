def count_vowels(input_string):
    vowels = 'AEIOUaeiou'  # Define vowels (both uppercase and lowercase)
    vowel_count = {'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U': 0}  # Initialize count for each vowel
    total_vowels = 0

    for char in input_string:
        if char.upper() in vowel_count:
            vowel_count[char.upper()] += 1  # Increase count for the specific vowel
            total_vowels += 1  # Increase total count of vowels

    return total_vowels, vowel_count


# Input string
input_string = "guvi geeks network private limited"

# Get total vowel count and individual vowel counts
total_vowels, vowel_count = count_vowels(input_string)

# Output results
print(f"Total number of vowels: {total_vowels}")
print(f"Count of each vowel: {vowel_count}")




def number_pyramid(n):
    num = 1  # Starting number
    for i in range(1, n+1):  # Number of rows
        for j in range(i):  # Number of elements per row
            print(num, end=' ')  # Print number with a space
            num += 1  # Increment number
            if num > 20:  # Stop when number exceeds 20
                break
        print()  # Move to the next line
        if num > 20:  # Stop printing rows if number exceeds 20
            break

# Generate pyramid with numbers from 1 to 20
number_pyramid(20)




def remove_vowels(input_string):
    vowels = 'AEIOUaeiou'  # Define vowels (both uppercase and lowercase)
    result = ''.join([char for char in input_string if char not in vowels])  # Remove vowels
    return result

# Input string
input_string = "guvi geeks network private limited"

# Get string with vowels removed
result_string = remove_vowels(input_string)

# Output result
print(f"Original string: {input_string}")
print(f"String without vowels: {result_string}")




def count_unique_characters(input_string):
    unique_chars = set(input_string)  # Convert the string to a set to get unique characters
    return len(unique_chars)  # Return the number of unique characters

# Input string
input_string = "guvi geeks network private limited"

# Get the number of unique characters
unique_count = count_unique_characters(input_string)

# Output result
print(f"Number of unique characters: {unique_count}")




def is_palindrome(input_string):
    # Remove spaces and convert the string to lowercase for comparison
    cleaned_string = ''.join(input_string.lower().split())
    
    # Check if the cleaned string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]

# Input string
input_string = "A man a plan a canal Panama"

# Check if the string is a palindrome
result = is_palindrome(input_string)

# Output result
print(f"Is the string a palindrome? {result}")




def longest_common_substring(str1, str2):
    m = len(str1)
    n = len(str2)
    
    # Create a 2D table to store lengths of longest common suffixes
    table = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize variables to track the length of the longest common substring and its position
    longest_len = 0
    end_pos = 0
    
    # Build the table and find the longest common substring
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
                if table[i][j] > longest_len:
                    longest_len = table[i][j]
                    end_pos = i  # Track the end position of the longest common substring in str1
            else:
                table[i][j] = 0

    # Extract the longest common substring from str1
    longest_common_substr = str1[end_pos - longest_len: end_pos]
    
    return longest_common_substr

# Input strings
str1 = "guvigeeksnetwork"
str2 = "geeksforgeeks"

# Get the longest common substring
result = longest_common_substring(str1, str2)

# Output result
print(f"Longest common substring: '{result}'")




from collections import Counter

def most_frequent_character(input_string):
    # Create a dictionary to count the frequency of each character
    frequency = Counter(input_string)
    
    # Find the character with the highest frequency
    most_frequent = max(frequency, key=frequency.get)
    
    return most_frequent, frequency[most_frequent]

# Input string
input_string = "guvi geeks network private limited"

# Get the most frequent character
most_frequent_char, frequency = most_frequent_character(input_string)

# Output result
print(f"The most frequent character is: '{most_frequent_char}' with a frequency of {frequency}")




def are_anagrams(str1, str2):
    # Remove spaces and convert strings to lowercase for comparison
    cleaned_str1 = ''.join(str1.lower().split())
    cleaned_str2 = ''.join(str2.lower().split())
    
    # Check if sorted characters of both strings are equal
    return sorted(cleaned_str1) == sorted(cleaned_str2)

# Input strings
str1 = "listen"
str2 = "silent"

# Check if the strings are anagrams
result = are_anagrams(str1, str2)

# Output result
print(f"Are the strings '{str1}' and '{str2}' anagrams? {result}")





def count_words(input_string):
    # Split the string by spaces to get the list of words
    words = input_string.split()
    
    # Return the number of words
    return len(words)

# Input string
input_string = "guvi geeks network private limited"

# Get the number of words
word_count = count_words(input_string)

# Output result
print(f"Number of words: {word_count}")
