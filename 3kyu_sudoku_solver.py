E=range;z=E(9)
def f(b):
 for x in z:
  for y in z:
   if 1>>b[x][y]:return x,y
 return-1,-1
def V(b,i,j,e):
 if R:=all([e!=b[i][x]for x in z]):
  if C:=all([e!=b[x][j]for x in z]):
   for x in E(X:=3*(i//3),X+3):
    for y in E(Y:=3*(j//3),Y+3):
     if b[x][y]==e:return 0
   return 1
def S(b,i=0,j=0):
 i,j=f(b)
 if i<0:return 1
 for e in E(1,10):
  if V(b,i,j,e):
   b[i][j]=e
   if S(b,i,j):return 1
   b[i][j]=0
def sudoku(p):
    if S(p):return p
