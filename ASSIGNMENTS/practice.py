# # write a program that asks user how many days are in a particular month, and what day of the week the month
# # begins on (0 for monday, 1 for tuesday) and then prints a calender for that month.
# # for example, here is the output for a 30 day month that begins on day 4(THURSDAY):
# #     MON TUE WED THUR FRI SAT SUN
# #                   1   2   3   4
# #     5    6   7    8   9   10  11
# from operator import truediv
#
# #
#
#
#
# mystr=input("enter your string")
# isupper=True
# for i in mystr:
#     if 65>ord(i) and ord(i)<90:
#         continue
#     else:
#         isupper=False
#         break
# if isupper==False:
#     print("is not in uppercase")
#
# else:
#     print("is in uppercase")


# a=int(input("enter the starting number"))
# b=int(input("enter your ending number"))
# for i in range(a,b+1):
#     if i<0:
#         print("your range must ne positive")
#
#     elif i%2==1:
#         print(i)
#
#     else:
#        factorial of 1to 10 numbers



# fact=1
# for i in range(0,11):
#     if i==0:
#         fact=1
#     else:
#         fact=fact*i
#         print(f"{i}!={fact}")

# num=int(input('entr your string'))
# n1=num%10
# n2=(num//10)%10
# n3=num//100
# num1=n1*100+n2*10+n3*1
# print(num1)


# num1=int(input("enter your number"))
# num_str=str(num1)
# digit_count=len(num_str)
# even_count=0
# odd_count=0
# sum_digits=0
# for i in num_str:
#     digit=int(i)
#     sum_digits+=digit
#
#     if num1%2==0:
#         even_count+=1
#     else:
#         odd_count += 1
#
# print(digit_count)
# print(sum_digits)
# print(even_count)
# print(odd_count)

# num1 = int(input("enter your number: "))
# num_str = str(num1)
# digit_count = len(num_str)
# even_count = 0
# odd_count = 0
# sum_digits = 0
#
# for i in num_str:
#     digit = int(i)
#     sum_digits += digit
#
#     if digit % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1

# print("Total digits:", digit_count)
# print("Sum of digits:", sum_digits)
# print("Even digits:", even_count)
# print("Odd digits:", odd_count)

# class Solution:
#     def addition(self, a, b):
#         self.a = a
#         self.b = b
#         print(f"Addition of {a} and {b} is: {self.a + self.b}")
# ob = Solution()
# ob.addition(1, 2)


# num1=int(input('ENTER YOUR FIRST NUMBER'))
# num2=int(input("ENTER YOUR SECECOND NUMBER"))
# gcd=1
# min_num=min(num1,num2)
# max_num=max(num1,num2)
# for i in range(1,min(num1,num2)+1):
#     if num1%i==0 and num2%i==0:
#         gcd=i
# print(gcd)
# while True:
#     for i in range (1,max_num+1):
#         if  max_num%num1==0 and max_num%num2==0:
#             lcm=max_num
#             break
#             max_num+=1
#         print(lcm)

# lcm = (num1 * num2) // gcd
# print(lcm)


words=['cat','bat','rat','sat','pat']
for word in words:
    print(word)
print(len(words))
print('cat'in words)
print('mat'not in words)

# --------------slicing -----------
print(words[4])
print(words[-3])
# print(words[5])
print(words[2:4])
print(words[1:4:2])
print(words[1:4:-2])
# -----------------methods-------------------
words.append('mat')
print(words)
words.remove('mat')
print(words)
words.insert(2,'pat')
print(words)
index=words.index('sat')
print(index)
words.sort()
print(words)
lst=['pat','chat']
lst.append(words)
print(lst)
words.pop(3)
print(words)
words.reverse()
print(words)
words=['cat','bat','rat','sat','pat']
for word in words:
    if isinstance(word,list):
         for item in word:
             print(item)
    else:
        print(word)
for index ,j in enumerate(words, start=5):
    print(index,'',j)

