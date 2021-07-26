"""
Fibonacci: a sequence is generated based on the summation of two Fibonacci functions. 
It is implemented using recursion with 2 cases, 0 and 1.
"""
def fibonacci(n): 
    if type(n)!=int:
        return "Input is not valid"
    if n < 0 : 
        return "Input is not valid"
    if n==0: 
        return 0
    elif n==1: 
        return 1
    while n!=1: 
       return fibonacci(n-1)+fibonacci(n-2)

"""
Lucas:a sequence is generated based on the summation of the first two Lucas functions. 
It is implemented using recursion with 2 cases, 2 and 1.
"""

def lucas(n):
    if type(n)!=int:
        return "Input is not valid"
    if n < 0 : 
        return "Input is not valid"
    if n==0: 
        return 2
    elif n==1: 
        return 1
    while n!=0: 
       return lucas(n-1)+lucas(n-2)

"""
sum_series: sequence is generated based on the summation of the first two functions, which are  0 and 1, this is by default.
  Lucas  if the two number => 2 and 1,
otherwise, a sequence is generated based on the two numbers as recived.
"""
def sum_series(n,n1=0,n2=1):
    # print(n,n1,n2)
    if type(n)!=int:
        return "Input is not valid"
    if n < 0 : 
        return "Input is not valid"
    if(n1==0 and n2==1):
        # print("fib running")
        return fibonacci(n)
    if( n1==2 and n2==1):
        # print("lucas running")
        return lucas(n)
    else: 
        if n==0:
            return n1
        if n==1:
            return n2
        else:
            # print("new series running")
            # print(n,n1,n2)
            # print("this is first sum",sum_series(n-1,n1,n2))
            # print("this is 2nd sum",sum_series(n-2,n1,n2))
            return sum_series(n-1,n1,n2)+sum_series(n-2,n1,n2)


# f(3)=f(2)+f(1)+f(0)
# print(sum_series(10,2,1))
# print(sum_series(5))
# print(sum_series(8,2,1))
# print(sum_series(8))
# print(sum_series(5,5,5))