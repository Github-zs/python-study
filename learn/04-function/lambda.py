p = lambda : print("调用")
s = lambda x: x+3
sum = lambda x,y: x+y
#使用lambda定义的匿名函数，调用时不要忘了()
p()
print(s(5))
print(sum(1,2))
