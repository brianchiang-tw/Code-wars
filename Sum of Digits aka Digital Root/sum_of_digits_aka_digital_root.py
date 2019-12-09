'''

Description:

In this kata, you must create a digital root function.

A digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n. 
If that value has more than one digit, continue reducing in this way until a single-digit number is produced. 

This is only applicable to the natural numbers.

Here's how it works:

digital_root(16)
=> 1 + 6
=> 7

digital_root(942)
=> 9 + 4 + 2
=> 15 ...
=> 1 + 5
=> 6

digital_root(132189)
=> 1 + 3 + 2 + 1 + 8 + 9
=> 24 ...
=> 2 + 4
=> 6

digital_root(493193)
=> 4 + 9 + 3 + 1 + 9 + 3
=> 29 ...
=> 2 + 9
=> 11 ...
=> 1 + 1
=> 2

'''


def digital_root(n):

    if n < 10:
        # base case, only one digit
        return n
    
    else:
        # inductive step
        # if more than one digit, solve digit_root recursively
        return digital_root( sum( map(int, list(str(n) ) ) ) )



def test_bench():

    test_data = [16, 942, 132189, 493193]


    # expected output
    '''
    7
    6
    6
    2
    '''

    for x in test_data:

        print( digital_root(x) )


    return



if __name__ == '__main__':

    test_bench()