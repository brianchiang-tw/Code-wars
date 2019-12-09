'''

Description:

An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
Implement a function that determines whether a string that contains only letters is an isogram. 

Assume the empty string is an isogram. 
Ignore letter case.

is_isogram("Dermatoglyphics" ) == true
is_isogram("aba" ) == false
is_isogram("moOse" ) == false # -- ignore letter case

'''


from collections import Counter

def is_isogram(string):
    
    # force covert to lower case
    # create a hash( python dictionary )
    
    # key: char
    # value: occurrence in string
    char_occ_dict = Counter( string.lower() )
    
    return len(char_occ_dict) == sum( char_occ_dict.values() )



def test_bench():

    test_data = ["Dermatoglyphics", "aba", "moOse"]

    # expected output:
    '''
    True
    False
    False
    '''

    for test_string in test_data:

        print( is_isogram( test_string ) )

    return



if __name__ == '__main__':

    test_bench()