'''
#1.调用父类属性方法
class Father():
    def __init__(self):
        self.a='aaa'
    def action(self):
        print("调用父类的方法")

class Son(Father):
    pass
son=Son() #子类Son继承父类Father的所有属性和方法
son.action() #调用父类方法
print(son.a) #调用父类的属性
'''
'''
#2.重写父类的方法
class Father():
    def __init__(self):
        self.a='你好'
    def action(self):
        print("调用父类的方法")

class Son(Father):
    def __init__(self):   #初始化
        self.b='nihao'
    def action(self):     #重写父类的方法
        print("子类重写父类的方法")
son = Son()  #类Son继承父类Father的所有属性和方法
son.action() #子类Son调用自身的action方法而不是父类的action方法
print(son.b) #调用子类的属性，父类已经被初始化无法使用son.a
'''
'''
#3.重写父类方法后重新要去调用父类方法
class Father():
    def __init__(self):
        self.a='你好'
    def action(self):
        print("调用父类的方法")

class Son(Father):
    def __init__(self):
        self.a='nihao'
    def action(self):
        super().action()
son=Son()
son.action()
print(son.a)
'''
'''
#4.如果父类的方法是私有方法,如 def __action(self)
#这样的话再去调用就提示没有这个方法,其实编译器是把这个方法的名字改成了 _Father__action()
#如果强制调用,可以这样
class Father():
    def __action(self):
        print("调用父类的方法")

class Son(Father):
    def action(self):
        super()._Father__action()
son = Son()
son.action()
'''
'''
#5.如果自己也定义了 __init__ 方法,那么父类的属性是不能直接调用的
class Father():
    def __init__(self):
        self.a='你好'

class Son(Father):
    def __init__(self):
#   self.a='nihao'  #这么写是没用的，后面son.a还是会取得子类
        super().__init__()
son =Son()
print(son.a)
'''
'''
#6.继承父类初始化过程中的参数
class Father():
    def __init__(self):
        self.a=1
        self.b=2

class Son(Father):
    def __init__(self):
        super().__init__()
        #也可以用 Father.__init__(self)  这里面的self一定要加上
    def add(self):
        return self.a+self.b
son=Son()
print(son.add())
'''
class Father():
    def __init__(self,a,b):
        self.a= a
        self.b= b
    def dev(self):
        return self.a - self.b

class Son(Father):
    def __init__(self,a,b,c=10):
        Father.__init__(self, a, b)  #调用父类初始化参数a,b,这种写法要带self
        # super().__init__(a,b)      #调用父类初始化参数a,b,这种写法不能带self
        self.c=c
    def add(self):
        return self.a + self.b
    def compare(self):
        if self.c > (self.a + self.b):
            return True
        else:
            return False

son = Son(5,6)
print(son.dev())
print(son.add())
print(son.compare())