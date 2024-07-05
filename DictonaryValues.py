n=int(input("Enter no of values"))
dic={}
for i in range(n):
    key=input("Enter Key")
    value=input("Enter value")
    dic[key]=value
print(dic)
print("after invertion")
print("invert_content")
def invert_content(dic):
    invert_dic={}
    invert_dic={v:k for k,v in dic.items()}
    return invert_dic