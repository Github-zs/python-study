tuple = (1,2,3,4,5)
print(tuple)
print(type(tuple))

# tuple是不可变序列 没有添加 删除 元素赋值等方法

print(tuple[2])

# 元组的解包
test_tuple = (1,2,3,4,5)
# 解包时变量个数要与元组长度一致
a,b,c,d,e = test_tuple
print(f'a={a}\nb={b}\nc={c}\nd={d}\ne={e}')
# 元素的交换
a,b = b,a
print(f'a={a}\nb={b}')
# 解包时 使用 *变量 可以将匹配变量剩余的元组转为list
tpl = (1,2,3,4,5)
a,b,*c = tpl
print(f'a={a}\nb={b}\nc={c}')

# == 和 is  ==判断的是值  is判断的是对象（地址）


d = {'name':'Tom','age':'20','gender':'male'}
print(d,type(d))

for key in d.keys():
	print(d[key])

for value in d.values():
	print(value)

for key,value in d.items():
	print(key,value)