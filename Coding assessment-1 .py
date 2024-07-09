l=["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
l1=["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
l2=["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety", "hundred"]
#1 to 1000
r=0


for i in range(1,10):
        r += len(l[i-1])

k=e=e1=n=0
for i in range(10,100):
    if i>10 and i<20:
        n+= len(l1[i-11])
    elif i%10==0:
            k = i//10
            n += len(l2[k-1])
    else:
            e=i//10
            e1=i%10
            str= len(l2[e-1])+len(l[e1-1])
            n += str

p=p1=p2=0
for i in range(101,1000):
    if i%100==0:
            q=1//100
            str1= len(l[q-1])
            p += str1 + len("hundred")
    else:
            a=i//100
            str2= len(l[a-1])
            p1 = str2 + len("hundred") + len("and")
            a1=i%100
            if a1<10:
                  p2 = len(l[a1-1])
            elif a1>=10 and a1<20:
                  p2 = len(l1[a1-11])
            elif a1>=20:
                  a2=a1//10
                  a3=a1%10
                  str3= len(l2[a2-1])+len(l[a3-1])
                  p2 = str3
            p += p1+p2

print("Result: ", r+n+p+len("Thousand"))
            
