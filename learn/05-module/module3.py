def foo():
    print("is foo")


def bar():
    print("is bar")

print('call foo()')
foo()

# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__
if __name__ == '__main__':
    print('call bar()')
    bar()