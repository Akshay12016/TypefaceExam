# m=[-1]*256
# mat=[m]*256
# print(mat)

mat=[[1,0,0,1,1],[1,0,0,0,1],[1,0,0,1,1],[1,1,1,1,1]]

m=len(mat)
n=len(mat[0])

ltop=[255,255]
rtop=[255,0]
ldown=[0,255]
rdown=[0,0]

for i in range(m):
    for j in range(n):
        if mat[i][j]==0:
            if ltop[0]>i:
                ltop[0]=i
            if ltop[1]>j:
                ltop[1]=j
            if rtop[0]>i:
                rtop[0]=i
            if rtop[1]<j:
                rtop[1]=j
            if ldown[0]<i:
                ldown[0]=i
            if ldown[1]>j:
                ldown[1]=j
            if rdown[0]<i:
                rdown[0]=i
            if rdown[1]<j:
                rdown[1]=j

if ltop[1]>=ldown[1]:
    ldown[1]=ltop[1]
else:
    ltop[1]=ldown[1]

if ltop[0]<=rtop[0]:
    rtop[0]=ltop[0]
else:
    ltop[0]=rtop[0]

if rtop[1]>=rdown[1]:
    rdown[1]=rdown[1]
else:
    rtop[1]=rdown[1]

if ldown[0]>=rdown[0]:
    rdown[0]=ldown[0]
else:
    ldown[0]=rdown[0]

print(ltop,rtop,ldown,rdown)
