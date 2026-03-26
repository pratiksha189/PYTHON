# -------------------------------------------------------------------------------
# QUESTION 1 : print factorials of given number
# -------------------------------------------------------------------------------
# num = int(input("Enter any number to find its Factorial: "))
# fact = 1
# for i in range(num,0,-1):
#     fact = fact * i
# print(fact)

# num = int(input("Enter any number to find its Factorial: "))
# fact = 1
# for i in range(1,num+1):
#     fact = fact * i
# print(fact)


# -------------------------------------------------------------------------------
# QUESTION 2 : find prime numbers from given range (from given first to last number)
# -------------------------------------------------------------------------------

# num1 = int(input("Enter First Number: "))
# num2 = int(input("Enter Last Number: "))
# for i in range(num1,num2):
#     for j in range(2,i//2):
#         if i%j == 0:
#             break
#     else:
#         print(i,end=" ")

#


# ::::::::::::::::::::::::::::::::::SOLUTION 2:::::::::::::::::::::::::::::

# num1 = int(input("Enter First Number: "))
# num2 = int(input("Enter Last Number: "))
# for i in range(num1,num2):
#     bool = False
#     for j in range(2,i//2):
#         if i%j==0:
#             bool = True
#             break
#     if bool == False:
#         print(i)

# -------------------------------------------------------------------------------
# QUESTION 3
# input = 843 | output = 348
# ------------------------------------------------------------------------

#
# -------------------------------------------------------------------------------
# QUESTION 4
# COUNT DIGITS, EVEN ODD, SUM
# -------------------------------------------------------------------------------

num = int(input("Enter any number: "))
Total_digits = 0
even_digits = 0
odd_digits = 0
addition = 0
while num>0:
    Total_digits+=1
    digit = num%10
    addition += digit
    if digit%2==0:
        even_digits += 1
    else:
        odd_digits+=1
    num//=10
print(f'Total_digits: {Total_digits} ,even_digits: {even_digits},odd_digits: {odd_digits},addition: {addition}')


# -------------------------------------------------------------------------------
# QUESTION 5
# GCD AND LCM USING 2 GIVEN NUMBERS
# -------------------------------------------------------------------------------
# num1 = int(input("Enter first Number: "))
# num2 = int(input("Enter Last Number: "))
# lcm=max(num1,num2)
# for i in range(1,lcm):
#     if lcm%num1==0 and lcm%num2==0:
#         print(lcm)