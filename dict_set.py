#! /usr/bin/python
# -*- coding: UTF-8 -*-
# dict全称dictionary，在其他语言中也称为map,使用 x={ },tuple是s=(),list是s=[]
# set和dict类似，也是一组key的集合，但不存储value。不可以放入可变对象
a = {'刘乒乒': 91, 'Dae': 85, 'BOB': 88}
print(a['刘乒乒'])
a['刘乒乒'] = 75
print(a['刘乒乒'])
a['Zhao'] = 66
print(a)
# 通过in判断key是否存在
print('Liu' in a)
print('Dae' in a)
# 通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value.返回None的时候Python的交互环境不显示结果。
print(a.get('Liu'))
print(a.get('Liu', -1))
# 删除一个key，用pop(key)方法
a.pop('刘乒乒')
print(a)
# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key
# set使用 x= set(['a','b','c'])
b = set([1, 2, 3])
c = set([2, 3, 4])
d = b & c
print('交集', d)
print('并集', b | c)
e = set([1, 1, 2, 2, 3, 3])
print(e)
#add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
e.add(4)
e.add(3)
print(e)
e.remove(1)
print(e)
