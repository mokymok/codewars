def get_real_floor(n):
    if n<0:return n
    elif n==1or n==0:return 0
    elif 5>n>1or 0>n:return n
    elif 13>n>=5:return n-1
    elif n>=13:return n-2
