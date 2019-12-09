'''

Description:

A pangram is a sentence that contains every single letter of the alphabet at least once. 

For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, 
because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. 
Return True if it is, False if not. 

Ignore numbers and punctuation.

'''

def is_pangram(s):
    char_occ_dict = dict()
    
    # case-insensitive, force convert to lower case
    s = s.lower()
    
    # build the dictionary for alphabet letter
    for char in s:
        if char.isalpha():
            char_occ_dict[char] = char_occ_dict.get(char, 0) + 1
            
      
    return len(char_occ_dict) == 26


def test_bench():

    test_data = [
                    "The quick brown fox jumps over the lazy dog",
                    "bcde fghi jklm nopq rstu vwxy z"
                ]

    # expected output:
    '''
    True
    False
    '''

    for s in test_data:

        print( is_pangram(s) )

    return



if __name__ == '__main__':

    test_bench()