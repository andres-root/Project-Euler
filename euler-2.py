def fibonacci():
    n = 0
    m = 1
    r = 0
    while n <= 4000000:
        if n % 2 != 0:
            r += n
        f = m + n
        m = n
        n = f
    return r
