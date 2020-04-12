import os

#####################################
def checkFile(cur_path):
    os.chdir(cur_path)                  # change directory
    print(os.path.abspath(os.curdir))
    
    allFile = os.listdir()
    files = []
    for f in allFile:
        if os.path.isdir(f): #文件夹
            files.extend(checkFile(cur_path + '\\' + f))
            # extend递归使用新列表拓展原列表
            os.chdir(cur_path)
        else:               #文件
            t_list = f.split('_', -1)       #按下划线切割
            if len(t_list) == 3:
                files.append(t_list[0] + t_list[1])
            
    return files
######################################

cur_path = os.getcwd()
H_list = checkFile(cur_path)
#list of hand-oned file
print("getting data...\n")
for i in range(0, len(H_list) - 1):
    print(H_list[i])

with open('name_list.txt', 'r', encoding = 'gbk') as n_f:
    list1 = n_f.readlines()
    front_w = list1[0].strip('\n')
    del list1[0]
    N_list = []
    for line in list1:
        N_list.append(line.strip('\n'))
        # append列表末尾插入,strip去除首尾字符，默认为空格或换行

print('\n{0}'.format(N_list))

with open('精确制导.txt', 'w', encoding = 'gbk') as f:
    tot = 0
    for line in N_list:
        if front_w + line not in H_list:
            f.write(line + '\n')
            tot += 1
    if tot > 0:
        f.write('共{0}人未上交'.format(tot))
    else:
        f.write('已全部上交')

print('\nReport have been created!\n\nInput any key to quit...')
#input()