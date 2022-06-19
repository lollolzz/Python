class Cal(object):
    def __init__(self, v1, v2):
        print(v1, v2)
        self.v1 = v1
        self.v2 = v2
       # python에서는 첫 번째 매개변수를 꼭 정의해야한다
       # 언제나 그 인스턴스가 된다.

    def add(self):
        return self.v1 + self.v2

    def subtract(self):
        return self.v1 - self.v2

c1 = Cal(10, 10)
print(c1.add())
print(c1.subtract())

c2 = Cal(30, 20)
print(c2.add())
print(c2.subtract())
