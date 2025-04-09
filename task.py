# nums = [1,2,3,4,5,6,7,8,9,10,11]

# nums = [x ** 2 for x in nums] 
# print(nums)

# def func(x=[]):

#     x.append(1)
#     return x
# print(func())
# print(func())

# def fibonacci(n):
#     a,b =0,1
#     result = []
#     for i in range(n):
#         result.append(a)
#         a,b = b,a+b
#     return result
# print(fibonacci(10))

nums = lambda x,y:max(x,y)
print(nums(4,5))
    