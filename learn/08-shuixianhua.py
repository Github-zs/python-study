def shuixianhua():
    for i in range(100, 999):
        ones = i % 10#个位
        tens = i % 100 // 10#十位
        hundreds = i // 100#百位，//为整除，保留整数 /会保留小数
        #  **表示幂操作 i**3 表示i的立方
        if((ones**3 + tens**3 + hundreds**3) == i):
            print(i)

shuixianhua()