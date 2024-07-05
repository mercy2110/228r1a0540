fp1=open("csea.txt","r")
fp2=open("cse.txt","w")
if fp1:
    print("file opened successfully")
for i in fp1:
    fp2.write(i)
print("file is copied successfully")
content=fp2.read()
print(content)
fp1.close()
fp2.close()
