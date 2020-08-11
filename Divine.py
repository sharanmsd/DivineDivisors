#Optimized approach to find all the factors upto n

n=int(input())
i=1
l=[]
while(i*i<=n):
    if(n%i==0):
        l.append(i)
        l.append(n//i)
    i+=1
l=list(set(l))
l=sorted(l)
print(*l)
