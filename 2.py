str1=input()
str2=input()

char=str2[len(str2)-1]

count1=0
for i in str1:
    if i==char:
        count1+=1

print(count1)