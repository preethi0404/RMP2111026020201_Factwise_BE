a = list(map(int,input("cardPoints:").split()))
k = int(input("Enter k value: "))
b=d=0
for i in range(k):#0 1 2  -1 -2 -3
    b+=a[i]
c= a[::-1]
for i in range(k):
    d+=c[i]
if b>d:
    print("Output:", b)
else:
    print("Output:", d)

