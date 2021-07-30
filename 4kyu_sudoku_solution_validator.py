def validSolution(b):
    t=[]
    for r in b:
        for i in range(1,10):
            if i not in r:return 0
    for c in range(9):
        t=[]
        for r in b:t.append(r[c])
        for i in range(1,10):
            if i not in t:return 0
    j=0
    while j<=2:
        t=[]
        for r in range(3*j,3*j+3):
            k=0
            for c in range(3*j,3*j+3):
                t.append(b[r][c])
        for i in range(1,10):
            if t.count(i)!=1:
                return 0                          
        j+=1
    return 1
