'''

Description:

Your task is to construct a building which will be a pile of n cubes. 
The cube at the bottom will have a volume of n^3, 
the cube above will have volume of (n-1)^3 and so on until the top which will have a volume of 1^3.

You are given the total volume m of the building. 
Being given m can you find the number n of cubes you will have to build?

The parameter of the function findNb (find_nb, find-nb, findNb) will be an integer m 
and you have to return the integer n such as n^3 + (n-1)^3 + ... + 1^3 = m if such a n exists 
or -1 if there is no such n.

Examples:
findNb(1071225) --> 45
findNb(91716553919377) --> -1

mov rdi, 1071225
call find_nb            ; rax <-- 45

mov rdi, 91716553919377
call find_nb            ; rax <-- -1

'''

from math import sqrt

def find_nb(m):
    
    # check square root of m is an integer or not
    if sqrt(m).is_integer() is False:
        return -1
    
    sum_of_cube = 0
    
    n = int( sqrt( sqrt(m) * 2 ) ) - 1
    while sum_of_cube < m:
        
        n += 1
        sum_of_cube = int( ( n * (n+1) // 2 )**2 )
        
    
    if sum_of_cube == m:
        return n
    else:
        return -1



def test_bench():

    test_data = [ 1071225, 91716553919377]

    # expected output:
    '''
    45
    -1
    '''
    for m in test_data:

        print( find_nb( m ) )

    return



if __name__ == '__main__':

    test_bench()