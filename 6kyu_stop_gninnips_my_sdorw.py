def spin_words(j):
    z=''
    for i in j.split(' '):
        if len(i)<5:z+=i+' '
        else:z+=i[::-1]+' '
    return z.rstrip()
