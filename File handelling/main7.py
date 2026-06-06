#seek and tell
with open('demo.txt','r') as f:
    f.seek(10)#10 byte ma pugxa
    data=f.read(5)#5 byte read garxa
    print(data)
    print(f.tell())#It tells the position of cursor 