old_name = input('请输入您要备份的文件名：')
# print(old_name)
# print(type(old_name))
index = old_name.rfind('.')
# print(index)
# print(old_name[:index])
# print(old_name[index:])

if index > 0:
    postfix = old_name[index:]



# new_name = old_name[:index] + '[备份]' + old_name[index:]
new_name = old_name[:index] + '[备份]' + postfix
print(new_name)


old_f = open(old_name,'rb')
new_f = open(new_name,'wb')


while True:
    con = old_f.read(1084)
    if len(con) == 0:
        break
    new_f.write(con)

old_f.close()
new_f.close()