'''

Description:

How many ways can you make the sum of a number?
From wikipedia: https://en.wikipedia.org/wiki/Partition_(number_theory)#

In number theory and combinatorics, a partition of a positive integer n, also called an integer partition, is a way of writing n as a sum of positive integers. Two sums that differ only in the order of their summands are considered the same partition. If order matters, the sum becomes a composition. For example, 4 can be partitioned in five distinct ways:

4
3 + 1
2 + 2
2 + 1 + 1
1 + 1 + 1 + 1
Examples
Basic
exp_sum(1) # 1
exp_sum(2) # 2  -> 1+1 , 2
exp_sum(3) # 3 -> 1+1+1, 1+2, 3
exp_sum(4) # 5 -> 1+1+1+1, 1+1+2, 1+3, 2+2, 4
exp_sum(5) # 7 -> 1+1+1+1+1, 1+1+1+2, 1+1+3, 1+2+2, 1+4, 5, 2+3

exp_sum(10) # 42

'''


from collections import defaultdict

def get_partition( n, m, look_up):
    
    if look_up.get( (n,m) ) is not None:
        # top-down memorization
        #print("#A {} {} direct return {}".format(n, m, look_up[(n,m)] ) )
        
        return look_up[(n,m)]
    
    if n == 1 or m == 1:
        look_up[(n,m)] = 1
        #print("#B {} {} return {}".format(n, m, look_up[(n,m)] ) )
        return look_up[(n,m)]
    
    if n < m:
        look_up[(n,m)] = get_partition(n, n, look_up)
        #print("#C {} {} return {}".format(n, m, look_up[(n,m)] ) )
        return look_up[(n,m)]
        
    if n == m:
        look_up[(n,m)] = 1 + get_partition(n, n-1, look_up)
        #print("#D {} {} return {}".format(n, m, look_up[(n,m)] ) )
        return look_up[(n,m)]
        
    if n > m > 1:
        #print("#E {} {} split {} {} and {} {}".format(n, m, n-m, m, n, m-1 ) )
        
        by_plus_m = get_partition( n - m, m, look_up )
        by_plus_one = get_partition( n, m - 1, look_up )
        look_up[(n,m)] =  by_plus_m + by_plus_one
        #print("#F {} {} return {}".format(n, m, look_up[(n,m)] ) )
        return look_up[(n,m)]

    
    
    
def exp_sum(n):

    look_up = defaultdict( None ) 
    
    partition_num = get_partition( n, n, look_up)
    
    return partition_num



def test_bench(): 


    # expected output:
    '''
    1
    2
    3
    5
    7
    42
    '''
    print( exp_sum(1) )
    print( exp_sum(2) )
    print( exp_sum(3) )
    print( exp_sum(4) )
    print( exp_sum(5) )
    print( exp_sum(10) )



if __name__ == '__main__':

    test_bench()
