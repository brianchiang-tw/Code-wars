'''

Desription:

Check to see if a string has the same amount of 'x's and 'o's. 
The method must return a boolean and be case insensitive. 

The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false

'''


def xo(s):
    
    # Check whether count of o and O is equal to count of x and X or not
    return ( s.count('o') + s.count('O') ) == ( s.count('x') + s.count('X') )



def test_bench():

    test_data = ["ooxx", "xooxx", "ooxXm", "zpzpzpp", "zzoo"]
    
    # expected output:
    '''
    True
    False
    True
    True
    False
    '''

    for test_str in test_data:

        print( xo( test_str ) )

    return



if __name__ == '__main__':

    test_bench()