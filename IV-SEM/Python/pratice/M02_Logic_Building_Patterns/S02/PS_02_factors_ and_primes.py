'''n=int(input())
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
        print(i,end=" 20")
print(count)

n=int(input())
if n>=0 :
    print(int(str(n)[:: -1]))
else:
    n=-1*n
    print(-1*int(str(n)[: : -1]))
    '''
n=int(input())
if n%i==0:
    n=n//i 
    print(i)
else:
    i+=1