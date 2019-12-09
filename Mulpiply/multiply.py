def multiply(a, b):
  return a * b



def test_bench():

    test_data = [
                    (1, 0),
                    (3, 5),
                    (8, 2)
                ]

    
    # expected output:
    '''
    0
    15
    16
    '''

    for pair in test_data:

        print( multiply(*pair) )



if __name__ == '__main__':

    test_bench()