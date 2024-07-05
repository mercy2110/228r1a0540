'''
def avg(marks):
    assert len(marks) !=0,"The list is empty."
    return sum(marks)/len(marks)
marks1=[23,67,48,89,78]
print("The Average of Marks1:",avg(marks1))
marks2=[10,20,30,40]
print("The Average of ,marks2:",avg(marks2))
'''

list12=[1,2,3,45,5,6]
x=6
assert x in list12," x is in list"
assert x not in list12, "x not in list"