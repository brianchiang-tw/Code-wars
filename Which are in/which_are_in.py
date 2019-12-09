'''

Description:

Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings of a1 which are substrings of strings of a2.

#Example 1: a1 = ["arp", "live", "strong"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

returns ["arp", "live", "strong"]

#Example 2: a1 = ["tarp", "mice", "bull"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

returns []

Notes:
Arrays are written in "general" notation. See "Your Test Cases" for examples in your language.

In Shell bash a1 and a2 are strings. The return is a string where words are separated by commas.

Beware: r must be without duplicates.
Don't mutate the inputs.

'''


def in_array(array1, array2):
    

    # catch all substring of array2 from array1, and use set() to eliminate duplicates
    return sorted( list(set( [ x for x in array1 for y in array2 if x in y] ) ) )



def test_bench():

    test_data = [
                    (["arp", "live", "strong"],["lively", "alive", "harp", "sharp", "armstrong"]),
                    (["tarp", "mice", "bull"], ["lively", "alive", "harp", "sharp", "armstrong"])
                ]

    # expected output:
    '''
    ['arp', 'live', 'strong']
    []
    '''

    for test_lists in test_data:

        print( in_array(*test_lists) )

    return



if __name__ == '__main__':

    test_bench()