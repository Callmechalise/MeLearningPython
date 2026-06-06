f = open("demo.txt","r")
data=f.read()
print(data)
print(type(f))
f.close()
#Characters
'''
1."r",read (deafult)
2."w",Overwrite
3."x",create newfile and open it for writing
4."a",Append
5."b",Binary
6."+"Open disc file for reading and writing
'''