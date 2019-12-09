'''

Description:

Write a function that takes in a string of one or more words, and returns the same string, 
but with all five or more letter words reversed (Just like the name of this Kata). 

Strings passed in will consist of only letters and spaces. 

Spaces will be included only when more than one word is present.

Examples: 
spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
spinWords( "This is a test") => returns "This is a test" 
spinWords( "This is another test" )=> returns "This is rehtona test"

'''

def spin_words(sentence):
    
    tokens = list( sentence.split() )
    
    for i in range( len( tokens) ):
    
        if len( tokens[i] ) >= 5:
            # reverse word with length >= 5
            tokens[i] = tokens[i][::-1]
            
        else:
            pass
    
    # generate output string, separated by white space
    output_string = ' '.join(tokens)
    
    return output_string



def test_bench():

    test_data = [
                    "Hey fellow warriors",
                    "This is a test",
                    "This is another test"
                ]


    # expected output:
    '''
    Hey wollef sroirraw
    This is a test
    This is rehtona test
    '''


    for test in test_data:

        print( spin_words(test) )

    return



if __name__ == '__main__':

    test_bench()