'''
require for name_list.txt
含线程类 checkThread
'''

import os
import time
import re # 正则表达式

from PyQt5.QtCore import QThread, pyqtSignal # qt多线程

#####################线程类#####################
class checkThread(QThread):
    m_finished_signal = pyqtSignal(str) # 信号
    m_process_signal = pyqtSignal(int) # 用于发射进度信号
    m_state_signal = pyqtSignal(str)

    def __init__(self, path, parent = None):
        super().__init__(parent)
        self.m_path = path

    def run(self):
        self.m_state_signal.emit("遍历目录树...")
        self.m_process_signal.emit(10)
        checkFile("none", self.m_path, self.m_path)
        self.m_process_signal.emit(80)
        self.m_finished_signal.emit("统计完成")
        self.m_state_signal.emit("统计完成")
        self.m_process_signal.emit(100)


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
    # 根据文件树取得当前目录下的文件名列表
    for fileName in filelist:
        NoSearch = re.search(r"[0-9]+", fileName) # 匹配学号
        if NoSearch != None :
            files.append(NoSearch.group())

    with open(working_path + "\\name_list.txt", 'r', encoding = 'utf-8-sig') as f:
        nameList = f.readlines()

    with open(file_path + '\\精确制导.txt', 'w', encoding = 'utf-8') as f:
        tot = 0
        for line in nameList:
            NO = re.search(r"[0-9]+", line).group() # 匹配学号

            if NO not in files:
                f.write(line)
                tot += 1
        if tot > 0:
            f.write('共{0}人未上交'.format(tot))
        else:
            f.write('已全部上交')

##############################################