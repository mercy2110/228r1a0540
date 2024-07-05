fp=open("word.txt","N")
if fp:
    print("successfully opened")
fp.write("i")
fp.write("a")
fp.write(" ")
fp.close()