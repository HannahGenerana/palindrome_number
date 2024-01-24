# Exercise 9: Check Palindrome Number
# Write a program to check if the given number is a palindrome number.
# A palindrome number is a number that is the same after reverse. For example, 545, is the palindrome numbers

# pseudocode

def checking_palindrome (random_number):

# convert the number to a string
    original_number = str (random_number)

# check if the string is equal to its reverse
    if original_number == original_number[::-1]:
        print (f"{original_number} is a palindrome number.")

    else:
        print(f"{original_number} is not a palindrome number.")

# print the result
checking_palindrome (123)
checking_palindrome (555)
checking_palindrome (121)
checking_palindrome (1092)