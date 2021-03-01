class ShortInputError(Exception):
    def __init__(self, length, min_len):
        self.length = length
        self.min_len = min_len

    def __str__(self):
        return f'您输入的密码长度是{self.length},密码不能少于{self.min_len}'


def main():
        try:
            password = input('请输入密码：')
            if len(password) < 3:
                raise ShortInputError(len(password), 3)
        except Exception as result:
            print(result)
        else:
            print('没有异常，输入完成')
main()
