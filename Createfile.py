'''
open()
read()
readline()
write()
writeline()
close()
seek()
tell()
'''
fp=open("csea.txt","w")
if fp:
    print("file is created successfully")
fp.writelines("welcome to cmrec\n hi everyone\n python class is on files")

fp.close()