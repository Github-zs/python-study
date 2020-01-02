list = [1,3,4,5,6,7]
print(list)

# 使用del删除对应元素
del list[1]
print(list)
# 根据值删除  删除列表中值为4的元素
list.remove(4)
print(list)
# 根据索引删除 返回值为删除的元素值
value = list.pop(3)
print("删除的元素为{0}".format(value))
print(list)

l1 = [1,2,3]
l2 = [4,5,6]
print(l1 + l2)
# 效果等同于l1+l2 为面向对象写法
print(l1.__add__(l2))
# 列表乘法是将列表重复几次  不能两个列表相乘会报错
print(l1 * 3)
# 效果等同于l1 * 3 面向对象写法
print(l1.__mul__(3))

l3 = [1,2,3,4,5,6]
print(2 in l3)
for i in l3:
  print(i)

# 列表长度
print("l3长度为：{0}".format(len(l3)))
print("l3长度为 %s" % format(l3.__len__()))

# 最大值 最小值
print("l3最大值 %d 最小值 %d" % (max(l3), min(l3)))
l3.reverse()
print(l3)
# 排序默认升序
l3.sort()
print(l3)
# 降序
l3.sort(reverse = True)
print(l3)

l4 = ["a","b","c","d","e","f","g"]
# list[start : end : step]
#   切片（字符串截取，包头不包尾，step为步长，step为负时从尾部开始截取）
print(l4[0:3])
l4.append("i")
print(l4)
print(l4.count("a"))
l4.extend(["j", "k"])
print(l4)
l4.insert(1,"f")
print(l4)
# 相当于l4[:]
print(l4.copy())
# 相当于 del l4[:]
l4.clear()
print(l4)