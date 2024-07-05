def convert(str):
    ch=list(str)
    for i in range(len(str)):
        if (i==0 and ch[i]!=' '):
            if (ch[i]>='a' and ch[i]<='z'):
                ch[i]=chr(ord(ch[i]-ord('a')+ord('A')))
        str1="",ch[i]
    return str1
print("hello good morning")