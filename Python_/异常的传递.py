import time
try:
    f = open('test.txt')
    try:
        while True:
            hang = f.readline()
            if len(hang) == 0:
                break
            time.sleep(3)
            print(hang)
    except:
        print('程序被意外终止')

except:
    print('该文件不存在')