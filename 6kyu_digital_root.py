def digital_root(n):
    x=y=z=0
    for i in str(n):x+=int(i)
    for i in str(x):y+=int(i)
    for i in str(y):z+=int(i)
    return z
