def create_phone_number(n):
    f=''
    for i in n:f+=str(i)
    return f"({f[:3]}) {f[3:6]}-{f[6:]}"
