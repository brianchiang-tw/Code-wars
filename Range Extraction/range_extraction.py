'''

Description:

A format for expressing an ordered list of integers is to use a comma separated list of either

individual integers
or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example ("12, 13, 15-17")
Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.

Example:

solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-6,-3-1,3-5,7-11,14,15,17-20"

'''

def solution(args):
    # your code here
    
    start, end= None, None
    range_extraction = []
    
    for idx, x in enumerate(args):
    
        if idx == 0:
            # first element
            
            start, si = x, 0
            end, ei = x, 0
            
        elif idx == len(args)-1:
            # last element
        
            if x != end+1:
                # catch one range
                if start == end:
                
                    # single range:[start]
                    range_str = str(start)
                    range_extraction.append( range_str )
                    
                else:
                
                    if ei-si == 1:
                        # two single range, one is made of start, the other is made of end
                        range_str = str(start)
                        range_extraction.append( range_str )
                        
                        range_str = str(end)
                        range_extraction.append( range_str )
                        
                    else:
                        range_str = str(start) + "-" + str(end)
                    
                        # add current range into container
                        range_extraction.append( range_str )
                        
            
                # for last range consists of x
                range_str = str(x)
                
                # add last range into container
                range_extraction.append( range_str )
            
            
            else:
                    # still continouous with previous number, update end as well as end index
                    
                    # update end as x
                    end, ei = x, idx


                    if ei-si == 1:
                    
                        # two single range, one is made of start, the other is made of end
                        range_str = str(start)
                        range_extraction.append( range_str )
                        
                        range_str = str(end)
                        range_extraction.append( range_str )
                        
                    else:

                        # one range: [start, end]
                        range_str = str(start) + "-" + str(end)
        
                        # add last range into container
                        range_extraction.append( range_str )
            
        
        else:
            # elements in the middle
            
            if x != end+1:
                # catch one range
                if start == end:
                
                    # single range: [start]
                    range_str = str(start)
                    
                    # add current range into container
                    range_extraction.append( range_str )
                    
                else:
                
                    if ei-si == 1:

                        # two single range, one is made of start, the other is made of end
                        range_str = str(start)
                        range_extraction.append( range_str )
                        
                        range_str = str(end)
                        range_extraction.append( range_str )

                    else:
                        range_str = str(start) + "-" + str(end)
                    
                        # add current range into container
                        range_extraction.append( range_str )
            
                # for new range begin from x
                start, si = x, idx
                end, ei = x, idx
            
            else:
                # still continouous with previous number, update end
                
                end, ei = x, idx
                
    
    output_str = ','.join( range_extraction )
    
    return output_str
                


def test_bench():

    test_data = [-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]

    range_extraction = solution( test_data )
    
    # expected output:
    '''
    -6,-3-1,3-5,7-11,14,15,17-20
    '''
    print( range_extraction )

    return



if __name__ == '__main__':

    test_bench()