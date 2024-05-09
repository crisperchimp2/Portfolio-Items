import re

def find_pattern(text, pattern):
    # Compile the regular expression pattern
    regex = re.compile(pattern)
    
    # Search for the pattern in the text
    match = regex.search(text)
    
    # Check if a match was found
    if match:
        # Return the matched text
        return match.group()
    else:
        return "No match found."

# Define the text string with hidden patterns
text = """
Here are some email addresses:
john.doe@example.com is John's email.
jane_smith123@email.co.uk is Jane's email.
jim@email-domain.com is Jim's email.
"""

# Define the pattern to search for (email addresses)
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

# Call the find_pattern function
result = find_pattern(text, pattern)

# Print the result
print("Found pattern:", result)
