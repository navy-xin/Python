class SweetPotato():
    def __init__(self):

        self.cook_time = 0

        self.cook_state = '生的'

        self.condiments = []

    def cook(self,time):

        self.cook_time += time

        if 0 <= self.cook_time < 3:
            self.cook_state = '生的'
        elif 3 <= self.cook_time < 5:
            self.cook_state = '半生不熟'
        elif 5 <= self.cook_time <= 8:
            self.cook_state = '熟了'
        elif self.cook_time >= 8:
            self.cook_state = '糊了'

    def add_condiments(self,condiment):
        self.condiments.append(condiment)

    def __str__(self):
        return f'这个地瓜被烤的时间是{self.cook_time},状态是{self.cook_state},添加的调理是{self.condiments}'

digua = SweetPotato()
print(digua)
digua.cook(2)
print(digua)
digua.cook(2)
digua.add_condiments('老干妈')
print(digua)
digua.cook(2)
digua.add_condiments('辣条')
print(digua)


