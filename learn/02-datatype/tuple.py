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

#-----------------------------------------------------------------

# 定义元组
t = ('骆昊', 38, True, '四川成都')
print(t)
# 获取元组中的元素
print(t[0])
print(t[3])
# 遍历元组中的值
for member in t:
    print(member)
# 重新给元组赋值
# t[0] = '王大锤'  # TypeError
# 变量t重新引用了新的元组原来的元组将被垃圾回收
t = ('王大锤', 20, True, '云南昆明')
print(t)
# 将元组转换成列表
person = list(t)
print(person)
# 列表是可以修改它的元素的
person[0] = '李小龙'
person[1] = 25
print(person)
# 将列表转换成元组
fruits_list = ['apple', 'banana', 'orange']
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)