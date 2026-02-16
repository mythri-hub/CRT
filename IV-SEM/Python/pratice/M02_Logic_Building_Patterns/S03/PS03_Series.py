
'''a=int(input())
d=int(input())
for i in range(10):
    print(a+i*d, end=" ")
    '''
''' series using recursive'''
'''a=0
b=1
n=int(input())
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b
    '''
'''L=[0,1]
n=int(input())
for i in range(2,n):#here i value =  index values
    L.append(L[i-2] + L[i-1])
print(L)
'''
n=int(input())
for i in range(1,n+1):
    print(n**i,end=" ")
