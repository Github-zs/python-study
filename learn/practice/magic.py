'''
找出两个两位数，分别十位个位互换后，乘积不变
'''
import time
start = time.time()
for i in range(10, 100):
	for j in range(10, 100):
		ione = i % 10
		iten = i // 10
		jone = j % 10
		jten = j // 10
		if(i * j == (ione * 10 + iten) * (jone * 10 + jten)):
			print('i={},j={}'.format(i, j))

print("一共用时: {}s".format(time.time() - start))