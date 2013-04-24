#Problem 1
def multiplo():
    ac = 0
    for n in range(1,1001):
        if n % 3 == 0 or n % 5 == 0:
            ac += n
    return n

#Problem 2
def fibonacci():
    fib = []
    n = 0
    m = 1
    r = 0
    while n < 41:
        fib.append(n)
        r += n 
        if n == 0:
            n += 1
        else:
            f = m + n
            m = n
            n = f
    return fib
            
