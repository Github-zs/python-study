def wanmeishu():
    for i in range(1, 10000):
        sum = 0
        for j in range(1, i):#注意分母不能为零
            if(i % j == 0):#判断是否是因子
                sum += j#所有因子的和
        else:
            if(sum == i):#判断所有因子和是否和当前数相等，相等则为完美数
                print(i)

wanmeishu()
