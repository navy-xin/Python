import os

ml = 2

file_list = os.listdir()
print(file_list)

for i in file_list:
    if ml == 1:
        new_name = 'Python_' + i
    elif ml == 2:
        num = len('Python_')
        new_name = i[num:]

    os.rename(i, new_name)