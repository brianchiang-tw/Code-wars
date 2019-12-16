'''

Description:

Write a function named first_non_repeating_letter that takes a string input, 
and returns the first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't', 
since the letter t only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character, 
but the function should return the correct case for the initial letter. 

For example, the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, it should return an empty string ("") or None 
-- see sample tests.

'''


from collections import Counter
from collections import OrderedDict

class OrderedCounter(Counter, OrderedDict):
    pass

def first_non_repeating_letter(string):
    #your code here
    
    # store a lowercase one of input
    string_lower = string.lower()
    
    # create a ordered counter
    # key: char
    # value: occurrence
    char_occ_dict = OrderedCounter(string_lower)

    first_non_repeat_char = None
    
    # get first non repeat char
    for char in char_occ_dict:
        
        if char_occ_dict[ char ] == 1:
            first_non_repeat_char = char
            break
    
    
    # early return if no non-repeating character
    if first_non_repeat_char is None:
        return ""
    
    
    # compute the index of first non-repeating character
    if string.find( first_non_repeat_char ) != -1:
        index_of_lower = string.find( first_non_repeat_char )
    else:
        index_of_lower = len(string)
    
    if string.find( first_non_repeat_char.upper() ) != -1:
        index_of_upper = string.find( first_non_repeat_char.upper() )
    else:
        index_of_upper = len(string)
    
    
    index_of_first_non_repeat_char = min(index_of_lower, index_of_upper)
    
    
    return string[index_of_first_non_repeat_char]