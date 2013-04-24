def multiplo():
    ac = 0
    for n in range(1,1001):
        if n % 3 == 0 or n % 5 == 0:
            ac += n
    return n
