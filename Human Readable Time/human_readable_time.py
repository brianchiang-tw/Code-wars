'''

Description:

Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.

'''

def make_readable(seconds):
    
    # convert to hour, minute, and seconds
    h, m, s = seconds // 3600, seconds % 3600 // 60, seconds % 60
    
    # formatted output as specified in description
    return f'{h:02}:{m:02}:{s:02}'



def test_bench():

    test_data = [ 5, 61, 121, 3599, 3601, 7201]

    # expected output:
    '''
    00:00:05
    00:01:01
    00:02:01
    00:59:59
    01:00:01
    02:00:01
    '''


    for second_string in test_data:

        print( make_readable( second_string ) )

    return



if __name__ == '__main__':

    test_bench()