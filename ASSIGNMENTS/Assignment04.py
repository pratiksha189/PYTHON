
'''------------------------------------------------------------------------------------------
Q1. Define a function overlapping () that takes two lists and returns True if they have at
least one member in common, False otherwise.
------------------------------------------------------------------------------------------'''
# list1=[2,3,4]
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
#         if i.endswith("e"):
#             word = i[:-1]+"ing"
#         elif i.endswith("ie"):
#             word = i[:-2]+"ying"
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
def outer(funct):
    def wrapper():
        return funct().upper()
    return wrapper

@outer
def display_greeting():
    return 'good morning'

print(display_greeting())












