def is_palindrome(s):
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()

    # Check if the string is the same forwards and backwards
    if s == s[::-1]:
        return "Yes"  # It's a palindrome
    else:
        return "No"  # It's not a palindrome

# Testing the program
s = input()
print(is_palindrome(s))  # Output: Yes

