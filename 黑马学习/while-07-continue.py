


i =1
while i <= 5:
    # 条件
    if i == 3:
        print('吃出一个大虫子，这个苹果不吃了')
        # 如果使用continue,在continue之前，一定要修改计数器，否则进入死循环
        i += 1
        continue
    print(f'吃了第{i}个苹果')
    i += 1