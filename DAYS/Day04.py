# # -----------------------------------------------------------------------------------------------
# '''FUNCTIONS'''
# # -----------------------------------------------------------------------------------------------
# def add(n1,n2):
#     return n1+n2
#
# print(add("San","desh"))
# print(add(89.34,36.39))
#
# def calculate_discount(product, price):
#     price = price * 0.8
#     print(f"Price of {product} after 20% discount: {price}")
#
# calculate_discount("APPLE",200)
# # -----------------------------------------------------------------------------------------------
# # default Parameter:
# # -----------------------------------------------------------------------------------------------
# def calculate_discount(product="Book", price = 0):
#     price = price * 0.8
#     print(f"Price of {product} after 20% discount: {price}(DEFAULT PARAM)")
#
# calculate_discount(price=100)
# calculate_discount("LaundryBag",291)
# # -----------------------------------------------------------------------------------------------
#
# # -----------------------------------------------------------------------------------------------
# '''args and kwargs(Dictionary)'''
# # -----------------------------------------------------------------------------------------------
# # def addition(*nums):
# #     print(addition(*nums))
# # nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # addition(nums)
#
#
#
#
#
#
#
#
#
# '''-------------------------------------------------------------------------------------------------
# SCOPE OF VARIABLE
# # -------------------------------------------------------------------------------------------------'''
# # GLOBAL VARIABLES
# name = "Ritika"
# age = 24
#
# def display_data():
#     # LOCAL VARIABLES
#     name = "PAYAL"
#     age = 28
#     print(f"NAME: {name}\nAGE : {age}" )
# print("-------------------------LOCAL VAR---------------------------------------------")
# display_data()
# print("-------------------------GLOBAL VAR---------------------------------------------")
# print(f"NAME: {name}\nAGE : {age}" )
# # ------------------------------------------------------------------------------------------------
#
# # ------------------------------------------------------------------------------------------------
# import platform as p
# print(p.system())
# import fun
# while True:
#     print('''Enter any option:
#                 1.addition:
#                 2.substraction
#                 3.multiplication
#                 4.division
#                 5.exit
#                 ''')
#     input1 = int(input("enter your choice: "))
#     if input1 == 5:
#         print("Goodbye!")
#         break
#     elif input1 != 1 or input1 != 2 or input1 != 3 or input !=4:
#         print("Invalid choice, try again.")
#     num1=int(input("enter your first number"))
#     num2=int(input("enter your second number"))
#
#     if input1==1:
#         result = fun.add(num1 ,num2)
#         print(result)
#
#     elif input1==2:
#         result = fun.sub(num1 ,num2)
#         print(result)
#
#     elif input1==3:
#         result = fun.mul(num1 ,num2)
#         print(result)
#
#     elif input1==4:
#         result = fun.div(num1 ,num2)
#         print(result)
#
# # ------------------------------------------------------------------------------------------------
# '''yield = Generators'''
# # ------------------------------------------------------------------------------------------------

# def generate_series():
#     i = 1
#     while True:
#         yield i
#         i+=1
# series = generate_series()
# print(next(series))
# print(next(series))
# print(next(series))
# print(next(series))
# ------------------------------------------------------------------------------------------------
# user_input = int(input("enter number upto which u want to print fibonacci : "))
# def generate_fib_series():
#     a,b = 0,1
#     while a<=user_input:
#         yield a
#         a, b = a + b, a
#
# generate_series()

# Following data displays min/max/average temp for cities
weather= [{'Mumbai' : [28, 30, 32]},
          {'Pune':[34,35,26]},
          {'Nashik': [24, 25, 27]}]

#
# 1. Print the weather data
print(weather)

# 2. Print the city with maximum/min temp
# print(max(weather,key=lambda item: max(list(item.values())[0])))
# print(min(weather,key=lambda item: min(list(item.values())[0])))
#
# map

# -----------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------
