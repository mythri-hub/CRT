'''li=['a','b','c']
# 'a b c'
res="" 
for ch in li:
    res=res + ch +" "
    print(res)
print(" ".join(li))'''
# pyramid pattern
'''n=int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)'''
'''n=int(input())
for i in range(1,n+1):
    print(" "*(i-i)+"* "*)'''
#diamond pattern
'''n=int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)
for i in range(n-1,0,-1):
    print(" "*(n-i)+"* "*i)'''
#for number diamond pattern 
'''n=int(input())
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(1,i+1):
        print(k,end=" ")
    print()'''

