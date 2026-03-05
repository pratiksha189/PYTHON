'''------------------------------------------------------------------------------------------
Q1. Define a function overlapping () that takes two lists and returns True if they have at
least one member in common, False otherwise.
------------------------------------------------------------------------------------------'''
# list1=[2,0,4]
# list2=[5,0,9]
# def overlapping(list1,list2):
#     flag=False
#
#     for i in list1:
#         for j in list2:
#             if i==j:
#                 flag=True
#     return flag
# print(overlapping(list1,list2))
'''------------------------------------------------------------------------------------------
Q.2.In English, present participle is formed by adding suffix -ing to infinite form: go -> going.
A simple set of rules can be given as follows:
 a. If the verb ends in e, drop the e and add ing
 b. If the verb ends in ie, change ie to y and add ing
Write a function make_ing_form() which accepts a list of verbs and returns a dictionary with
verb : present participle
----------------------------------------------------------------------------------------'''

# result = {}
# def make_ing_form(list1):
#     for i in list1:
#         if i.endswith("ie"):
#             word = i[:-2]+"ying"
#         elif i.endswith("e"):
#             word = i[:-1]+"ing"
#         else:
#             word = i+"ing"
#         result[i]=word
#     return result
# list1=  [ "code","rude","go","saddie","die"]
# print(make_ing_form(list1))

'''------------------------------------------------------------------------------------------
Q.3. Function display_greeting(message) prints message sent as argument as today's greeting. Decorate the
function using appropriate decorated so that the greeting is displayed using Uppercase.
----------------------------------------------------------------------------------------'''
# def outer(funct):
#     def wrapper():
#         return funct().upper()
#     return wrapper
#
# @outer
# def display_greeting():
#     return 'good morning'
#
# print(display_greeting())

'''------------------------------------------------------------------------------------------
Q. 4. Create series of 'n' prime numbers and display first 10 using generator.
----------------------------------------------------------------------------------------'''

# def prime_generator():
#     num = 2
#     while True:
#         count = 0
#         for i in range(1, num + 1):
#             if num % i == 0:
#                 count += 1
#         if count == 2:
#             yield num
#         num += 1
#
# gen = prime_generator()
# n = int(input("Enter value of n: "))
# print(f"First {n} prime numbers:")
#
# for i in range(n):
#     print(next(gen))
#


'''-----------------------------------------------------------------------------------------------
Q.5
1. Find employees that know 'python'
2. Add a new skill - 'test' in skillset of all employees
3. Sort employees by skills
for the given dictionary of employees

emp_data = {'Amol': ['C', 'C++', 'Java'], 'Aditya': ['Angular', 'Java'],
            'Aditi': ['Python', 'PHP', 'Database']}
_________________________________________________________________________________________________'''
emp_data = {'Amol': ['C', 'C++', 'Java'], 'Aditya': ['Angular', 'Java'],
           'Aditi': ['Python', 'PHP', 'Database']}

# 1.
print("\nemployees that know 'python': \n")
l1=dict(filter(lambda item:'Python' in item[1],emp_data.items()))
print(l1)

# 2.
print("\nAdd a new skill - 'test' in skillset of all employees: \n")
l2=dict(map(lambda item:(item[0], item[1]+['test']),emp_data.items()))
print(l2)

# 3.
print("\nSort employees by skills: \n")
l3=dict(sorted(emp_data.items(),key=lambda item:item[1][1]))
print(l3)

''' =========================================================================
Q.6 Following data displays min/max/average temp for cities
========================================================================='''
# weather= [{'Mumbai' : [28, 30, 32]},
#           {'Pune':[34,35,26]},
#           {'Nashik': [24, 25, 27]}]
#
# # 1. Print the weather data
# print(weather)
#
# # 2. Print the city with maximum/min temp
# print(max(weather,key=lambda item: max(list(item.values())[0])))
# print(min(weather,key=lambda item: min(list(item.values())[0])))
#
# # 3. Print all the cities that experience min temp more than 30 degree
# print(list(filter(lambda item: any(item>30 for item in list(item.values())[0]),weather)))
#
# # 4. Create a dictionary to print 'City':'Ave temp'
# avg_temp=dict(map(lambda v: (list(v.keys())[0],sum(list(v.values())[0])/len(list(v.values())[0])),weather))
# print(avg_temp)
