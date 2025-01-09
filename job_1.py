a=int(input("enter no of elements"))
l=[]
for i in range(a):
    n=int(input("enter any number"))
    l.append(n)
print("MAX=",max(l))
print("MIN=",min(l))
print("SUM=",sum(l))