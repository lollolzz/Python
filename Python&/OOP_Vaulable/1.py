class c :
    def __init__(self, v):
        self.value = v
    def show(self):
        print(self.value)

c1 = c(10)
print(c1.value)
# c1에 소속되어있는 value값을 읽어 온 것임
c1.value = 20
print(c1.value)
c1.show()