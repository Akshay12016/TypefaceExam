n=int(input())
l=[]
rem=0
while n!=0:
    l.append(n%3)
    n//=3
l=l[::-1]
print(*l,sep='')