r=int(input("Enter no of rows"))
c=int(input("Enter no of columns"))
a=[]
b=[]
for i in range(r):
    x=[]
    for i in range(c):
        (x.append(int(input("enter the values"))))
    a.append(x)
for i in range(r):
    for j in range(c):
        print(a[i][j],end=" ")
    print()