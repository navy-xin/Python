class Furniture():
    def __init__(self,name,area):
        self.name = name
        self.area = area

class Home():
    def __init__(self,address,area):
        self.address = address
        self.area = area
        self.free_area = area
        self.furniture = []

    def __str__(self):
        return f'房子地理位置在{self.address},房子面积是{self.area},房子剩余面积是{self.free_area},家具有{self.furniture}'

    def add_furniture(self,item):
        if item.area <= self.free_area:
            self.furniture.append(item.name)
            self.free_area -= item.area
        else:
            print('用户家具面积太大，剩余面具不足，无法容纳！')

bed = Furniture('双人床', 6)
sofa = Furniture('沙发',10)

jia1 = Home('北京', 1000)
print(jia1)

jia1.add_furniture(bed)
print(jia1)

zuqiuchang = Furniture('足球场',20000)
jia1.add_furniture(zuqiuchang)
print(jia1)