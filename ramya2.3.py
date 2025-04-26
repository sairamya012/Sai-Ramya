def palindrome (string):
    #remove any spaces and convert the string to lowercase
    string=string.replace("","").lower()
    #check if the string is equal to its reverse
    return string==string[::-1]

#Example usage:
print(palindrome("madam"))
