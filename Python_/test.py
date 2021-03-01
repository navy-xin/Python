
#
# age = input('How old are you?')
#
# height = input('How tall are you?')
#
# weight = input('How much do you weigh?')
#
# print('SO,you\'re %r old,%r tall and %r heavy.' %(age,height,weight))
#

# from sys import argv

class Dog(object):
    @staticmethod
    def info_print():
        print('这是一个静态方法')
wangcai = Dog()

aa = wangcai.info_print()
print()
Dog.info_print()
