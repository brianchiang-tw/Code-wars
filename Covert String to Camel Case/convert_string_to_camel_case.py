'''

Description:

Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
The first word within the output should be capitalized only if the original word was capitalized 
(known as Upper Camel Case, also often referred to as Pascal case).

Examples
to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"

to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"

'''

import re
def to_camel_case(text):
    
    # parse symbol with separtor = '-' or '_'
    tokens = list( re.split( '-|_',text) )
    
    # convert symbol to camel case string
    return ''.join([ tokens[i] if i == 0 else ( tokens[i][0].upper() + tokens[i][1:] ) for i in range(len(tokens))  if len( tokens[i] ) != 0 ] )



def test_bench():

    test_data = ["the-stealth-warrior", "The_Stealth_Warrior"]

    # expected output:
    '''
    theStealthWarrior
    TheStealthWarrior
    '''


    for s in test_data:

        print( to_camel_case( s ) )

    return



if __name__ == '__main__':

    test_bench()