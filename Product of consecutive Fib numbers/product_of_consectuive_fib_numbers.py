def Fib(n):
    
    if n == 0 or n == 1:
        # Base case:
        return n
    
    f0, f1 = 0, 1
    
    a, b = f0, f1
    
    for i in range(1, n):
        a, b = b, a+b
        
    
    return a


def productFib(prod):
    
    cur_product = 0
    n = -1
    f_n, f_n_1 = 0, 1
    while cur_product <= prod :
        
        n += 1
        f_n, f_n_1 = Fib(n), Fib(n+1)
        cur_product = f_n * f_n_1
        
        if cur_product == prod:
            return [f_n, f_n_1, True]
            
    return [f_n, f_n_1, False]