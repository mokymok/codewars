def get_count(s):
    x=0
    for i in s:x+=(0,1)[i in "aeiou"]
    return x
