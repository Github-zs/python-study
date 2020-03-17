def CheckDuplicates(A):
	tmp = A[0]
	for i in range(1, len(A)):
        # 所有重复的数字异或运算后都是零 最后就剩下唯一的单独数字
		tmp = tmp ^ A[i];
	return tmp

A = [4, 4, 3, 2, 1, 2, 3]
print(CheckDuplicates(A))
