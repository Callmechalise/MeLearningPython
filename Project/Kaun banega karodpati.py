#Function defination
def result(x,y):#Ans check
    if x==y:
        print("Correct answer\n")
    else:
        print("Oops sorry\n")

#Questions
question1=['''\nQuestion 1:\nWhich of the following data collection methods involves asking
individuals questions to gather information?          
''',
"Option A: Experimentation",
"Option B: Survey",
"Option C: Observation",
"Option D: Focus Group","B"]
question2=[
'''Question 2: What is a common approach to collecting data in debt collection?          
''',
"Option A: Offering incentives for early payment",
"Option B: Restricting payment options to checks only",
"Option C: Failing to stay in touch with customers regularly",
"Option D: Not developing standards for approving loans","A"]
question3=[
'''Question 3: Which of the following is not a data structure that is in the form of a dictionary?          
''',
"Option A: DefaultDict",
"Option B: OrderedDict",
"Option C: Counters",
"Option D: DeQue","D"]
question4=[
'''Question 4: Find the correct way to import the required module to use the ChainMap.        
''',
"Option A: import Collection",
"Option B: import collections",
"Option C: import collection",
"Option D: import Collections","B"]
#User input and printing qn and options


print(question1[0],"\n")
print(question1[1],"\n")
print(question1[2],"\n")
print(question1[3],"\n")
print(question1[4],"\n")
print("Current balance:\n")
a=input("Input answer: \n")
result(a,question1[5])
correctans1=question1[5]


print(question2[0],"\n")
print(question2[1],"\n")
print(question2[2],"\n")
print(question2[3],"\n")
print(question2[4],"\n")
a=input("Input answer: \n")
result(a,question2[5])
correctans2=question2[5]


print(question3[0],"\n")
print(question3[1],"\n")
print(question3[2],"\n")
print(question3[3],"\n")
print(question3[4],"\n")
a=input("Input answer: \n")
result(a,question3[5])
correctans3=question3[5]


print(question4[0],"\n")
print(question4[1],"\n")
print(question4[2],"\n")
print(question4[3],"\n")
print(question4[4],"\n")
a=input("Input answer: \n")
result(a,question4[5])
correctans4=question4[5]




