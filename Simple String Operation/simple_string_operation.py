'''

Description:

Move the first letter of each word to the end of it, then add "ay" to the end of the word. 
Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !

'''


def pig_it(text):
    #your code here
    
    tokens = list( map(str,text.split() ) )
    
    for i, t in enumerate(tokens):
    
        
        if t[0].isalpha():
            # only modify alphabetic string, exclusing punctuation marks
            tokens[i] = tokens[i][1:] + tokens[i][0] + str("ay")
    
    
    # generate output string
    output_str = " ".join(tokens)
    
    
    return output_str



def test_bench():

    test_data = [
                    "Pig latin is cool",
                    "Hello world !"
                ]


    # expected output:
    '''
    igPay atinlay siay oolcay
    elloHay orldway !
    '''

    for s in test_data:

        print( pig_it(s) )

    return



if __name__ == '__main__':

    test_bench()