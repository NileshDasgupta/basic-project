# def factorial(a):
#     for a in factorial:
#         if a==1:
#             return a
#         else:
#             return a*(a-1)
          
# print(factorial(5))


    
# year = int(input("enter a year u want to check"))

# if year%400==0 and year%100==0 or year%4==0 and year%100!=0:
#     print("its a leap year")
# else:
#     print("its not a leap year")

my_list = [1, 2, 3, 4, 5]
squ = lambda x: x**2

print(list(map(squ,my_list)))