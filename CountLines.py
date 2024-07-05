fp=open("count.txt","r")
words =0
lines=0

for i in fp:
    words=i.split()
print(len(words))