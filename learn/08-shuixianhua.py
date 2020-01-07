def shuixianhua():
    for i in range(100, 999):
        ones = i % 10
        tens = i % 100 // 10
        hundreds = i // 100
        if((ones**3 + tens**3 + hundreds**3) == i):
            print(i)

shuixianhua()