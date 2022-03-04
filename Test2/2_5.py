"""
날짜 : 20/08/13
이름 : 권능한
내용 : 파이썬 클래스 연습문제

"""

class King:

    def __init__(self,name='태조',year=1392):
        self.name = name
        self.year = year

    def show(self):
        print('----------------')
        print('name :', self.name)
        print('name :', self.year)

if __name__ == '__main__':

    King1 = King()
    King2 = King('태종')
    King3 = King('세종대왕', 1418)

    King1.show()
    King2.show()
    King3.show()