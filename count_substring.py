'''
The user enters a string and a substring. You have to print the number of times that the substring 
occurs in the given string. String traversal will take place from left to right, not from right to left. 
'''

def count_substring(string, sub_string):
    n=0
    
    for i in range(len(string)):
        if string[i:i+(len(sub_string))]==sub_string:
            n+=1
    return n