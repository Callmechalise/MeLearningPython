#Re module
#Discrette math
import re
from re import findall

li='''
This is a placeholder text commonly used in design and publishing. 
It 10 does not have any specific meaning but serves as a visual representation of content.
The purpose of this text is to fill space in a document or a website while 
the actual 55 content is being prepared.
Designers and developers use it to test layouts,
typography, and overall appearance before finalizing the real text.
'''
pattern1=r"[A-Z][a-z]*"#Pattern which says first capital and baki j sukai
caps=findall(pattern1,li)
print(caps)

pattern2=r"\d{2}" #find all int of two digit
num=findall(pattern2,li)
print(num)

#search method
y=re.search("purpose",li)
print(f" item found at {y}")
y=re.findall("purpose",li)
for match in y:
    print(match)
