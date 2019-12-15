'''

Description:

You are given a node that is the beginning of a linked list. This list always contains a tail and a loop.

Your objective is to determine the length of the loop.

# Use the `next' attribute to get the following node
# Example of geeting next node:
node.next

'''


def count_loop_size( node_of_meet ):

    size = 1
    visit = node_of_meet
    
    # run the loop again to count loop size
    while( visit.next != node_of_meet ):
        
        visit = visit.next
        size += 1
      
    return size

def loop_size(node):
    
    slow, fast = node, node
    
    while True:
        
        # use double pointer technique to make a meeting 
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            loop_size = count_loop_size(slow)
            break
            
    return loop_size