fp1=open("csea.txt","r")
if fp1:
    print("File is opened successfully")
for i in fp1:
    print(i)
fp1.seek(10,0)
'''content=fp1.read()
print(content)
content=fp1.readline()
print(content)'''
fp1.close()