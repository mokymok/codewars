def last_digit(x,y):
    if y==0:return 1
    c=[x%10]
    while 1:
        n=(c[-1]*x)%10
        if n==c[0]:break
        c.append(n)
    return c[(y-1)%len(c)]
