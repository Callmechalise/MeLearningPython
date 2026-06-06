with open('demo.txt','w') as f:
    f.write("Hello world")
    f.truncate(5)#File ko size 5 bytes hos vanerw lagako only hello will be there
with open('demo.txt','r') as f:
    print(f.read())
