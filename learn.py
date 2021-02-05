#! /usr/bin/python
# -*- coding: UTF-8 -*-
if True:
    print("the quick brown fox","jumps over","the lazy dog")
    print(100+200)
    print("100+200=",300)
    print(300)
    print("hello!")
    print("I\"m "
          "OK ")
    print(1024*768)
    print(3 > 5)

    name = input("请输入你的名字：")
    print("hello",name)
    #input默认是str类型不能直接和数字对比，要先转换我int型
    age = int(input("请输入你的年龄："))
    if age >= 18:
        print("成年人")
    else:
        print("未成年")
    print(9/3)
    # 地板除
    print(10//3)
    print(r'你好\n 中国\t ')
    print(chr(66))
    #纯英文的str可以用ASCII编码为bytes
    print('ABC'.encode('ascii'))
    #中文的str可以用UTF-8编码为bytes
    print('中文'.encode('utf-8'))
    #把bytes变为str，就需要用decode()方法
    print(b'ABC'.decode('utf-8'))
    print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
    #bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节
    print(b'\xe4\xb8\xad\xff'.decode('utf-8',errors='ignore'))
    #要计算str包含多少个字符，可以用len()函数
    print(len('ABC'))
    print(len('中文'))
    #len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数
    print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
    #%运算符就是用来格式化字符串的,%s表示用字符串替换,%d表示用整数替换,有几个%?占位符，
    # 后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略
    x = '你好 , %s , you have $%d' %('liu',3.154)
    print(x)
    print('%2d-%02d' %(3,1))
    print('%.2f' % 3.1415926)
    y=3.1
    print('%.3f' %y)
    s1=72
    s2=85
    r=s1/s2*100
    #字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%
    print('%.1f%%' %r,)







