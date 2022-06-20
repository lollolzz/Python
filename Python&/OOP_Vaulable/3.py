class Cal(object):
    def __init__(self, v1, v2):
        if isinstance(v1, int):
            self.v1 = v1
        if isinstance(v2, int):
            self.v2 = v2

    def add(self):
        return self.v1+self.v2
    def substract(self):
        return self.v1-self.v2
    def setV1(self, v):
        if isinstance(v, int): # 이렇게 만들어 두면 c1.setV1('one') 은 무시가 되버린다
            self.v1 = v

    def getV1(self):
        return self.v1

# instance를 만든 곳
c1 = Cal(10, 10)
print(c1.add())
print(c1.substract())
c1.setV1('one')
c1.v2 = 30
print(c1.add())
print(c1.substract())