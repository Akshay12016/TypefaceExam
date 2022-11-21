def digits(n):
    num=[0,1,2,5,6,8,9]
    while n!=0:
        if n%10 not in num:
            return False
        n//=10
    return True

n=int(input())
ser=[0,1,2,5,6,8,9]

for i in range(10,2*n):
    if digits(i):
        ser.append(i)

print(ser[n])
