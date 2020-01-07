def Fibonacci(n):
    fibonacci = []
    a, b = 0, 1
    flag = 0
    while flag < n:
        fibonacci.append(b)
        a, b = b, a + b
        flag+=1
    else:print(fibonacci)

Fibonacci(10)