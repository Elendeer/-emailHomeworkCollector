'''
require for name_list.txt
'''

import os
import time



#################遍历目录函数################
def checkFile(prefix, cur_path, working_path):
    os.chdir(cur_path) # change directory
    print(os.path.abspath(os.curdir))

    allFile = os.listdir() # get a file/dir str list
    
    haveDir = False
    for f in allFile:
        if os.path.isdir(f):
            haveDir = True
            checkFile(f, cur_path + '\\' + f, working_path)

            os.chdir(cur_path) # back to current path
    
    if not haveDir and prefix != 'Unrecognized' and prefix != 'backup' and prefix != 'logs':
        checkNameList(prefix, os.path.abspath(cur_path), working_path)


###################名单对比函数################
def checkNameList(prefix, file_path, working_path):
    filelist = os.listdir()

    files = []
    for i in filelist:
        temp = i.split('_', -1)
        if len(temp) == 3: # 根据命名规则，作业名将被切割成三串
            files.append(temp[0] + temp[1])
    
    with open(working_path + "\\name_list.txt", 'r', encoding = 'utf-8-sig') as f:
        nameList = f.readlines()
    
    with open(file_path + '\\精确制导.txt', 'w', encoding = 'utf-8') as f: 
        tot = 0
        for line in nameList:
            line = line.strip('\n')
            if prefix + line not in files:
                f.write(line + '\n')
                tot += 1
        if tot > 0:
            f.write('共{0}人未上交'.format(tot))
        else:
            f.write('已全部上交')

##############################################
def EHC_Check(working_path):
    '''
    接口，请提供路径
    '''
    #time.sleep(3)
    checkFile("none", working_path, working_path)