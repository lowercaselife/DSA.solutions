# Python 3 program to get lexicographically
# smallest palindrome string
 
# Utility method to check str is
# possible palindrome after ignoring
def isPossiblePalindrome(str):
    n = len(str)
    for i in range(n // 2):
         
        # If both left and right character
        # are not dot and they are not
        # equal also, then it is not possible
        # to make this string a palindrome
        if (str[i] != '?' and
            str[n - i - 1] != '?' and
            str[i] != str[n - i - 1]):
            return False
 
    return True
 
# Returns lexicographically smallest
# palindrome string, if possible
def smallestPalindrome(str):
    if (not isPossiblePalindrome(str)):
        return "NO"
 
    n = len(str)
    str = list(str)
     
    # loop through character of string
    for i in range(n):
        if (str[i] == '?'):
             
            # if one of character is dot,
            # replace dot with other character
            if (str[n - i - 1] != '?'):
                str[i] = str[n - i - 1]
 
            # if both character are dot,
            # then replace them with
            # smallest character 'a'
            else:
                str[i] = str[n - i - 1] = 'a'
 
    # return the result
    return str
 
# Driver code
if __name__ == "__main__":
    str = "?a?"
    print(''.join(smallestPalindrome(str)))
 