def read_mat(A,r,c):
    for i in range(r):
        t=[]
        for j in range(c):
            val=int(input(f"Enter the A[{i}][{j}] value "))
            t.append(val)
        A.append(t)

def display_Mat(A):
    for i in A:
        print(i)
Mat_A=[]
read_mat(Mat_A,2,2)
print("Mat_A")
Mat_B=[]
read_mat(Mat_B,2,2)
print("Mat_B")
display_Mat(Mat_B)
display_Mat(Mat_A)
c=[]
for i in range(2):
    t=[]
    for j in range(2):
        val=Mat_A[i][j]+Mat_B[i][j]
        t.append(val)
    c.append(t)
display_Mat(c)