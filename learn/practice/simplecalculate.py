import random


def calculate():
    count = 0
    right = 0

    while True:
        first = random.randint(1, 9)
        sec = random.randint(1, 9)
        op = ['+', '-', '*', '//']
        symbol = random.choice(op)
        #expression = "%d %s %d"%(first, symbol, sec)
        #join方法，是用join前边的字符串拼接后边的字符串中字符之间的间隔
        #result = input("please input answer".join(expression))
        if((symbol == '//' and first % sec != 0) or (symbol == '-' and first < sec)):
            continue
        expression = "{0} {1} {2}".format(first, symbol, sec)
        answer = input("please input answer {0} {1} {2}:".format(first, symbol if symbol != '//' else '/', sec))
        result = eval(expression)
        if(answer == str(result)):
            print("you are right")
            right += 1
            count += 1
        elif answer == 'q':
            print("you have quit")
            break
        else:
            count += 1
            print("you are wrong")
    percent = right / count
    print('测试结束,共回答%d道题,正确个数为%d,正确率为%.2f%%'
          % (count, right, percent * 100))

calculate()
