def Fibonacci(n):
    fibonacci = []#列表
    a, b = 0, 1
    flag = 0
    while flag < n:
        fibonacci.append(b)
        a, b = b, a + b#数列的第二位以后每一位都是前两位的和
        flag+=1
    else:print(fibonacci)

Fibonacci(10)