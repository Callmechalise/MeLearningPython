import string
import random
while True:
    s1=string.ascii_lowercase#small abcd 26
    s2=string.ascii_uppercase#Capital abcd 26
    s3=string.digits#0 dekhi 9
    s4=string.punctuation#special characters
    s5=string.whitespace

    lenp=int(input("How many characters should be in your password:\n"))

    s=[]
    s.extend(list(s1))#Extend le garda repeat hunna
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    s.extend(list(s5))
    random.shuffle(s)
    print("".join(s[0:lenp]))

