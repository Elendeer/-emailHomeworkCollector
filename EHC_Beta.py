import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog
from PyQt5 import QtWidgets

import EHC_GUI
from EHC_core import coreThread
from EHC_Checker import checkThread
from EHC_saveParameters import saveParameters

class Window(EHC_GUI.Ui_MainWindow) :#包含了主窗口作为成员变量了
    def __init__(self):
        self.MainWindow = QMainWindow()
        super().setupUi(self.MainWindow)

        self.progressBar.setRange(0, 100)

        ##################增加的按钮触发################
        self.check.clicked.connect(self.__gotoCheck)
        self.get.clicked.connect(self.__gotoCore)
        self.save.clicked.connect(self.__gotoSaveParameters)

        ###############################################
        self.m_checking = False # 作业统计标志位
        self.m_coreRunning = False # 核心功能，即邮箱收作业标志位

        #################读取设置文档#################
        self.m_path = os.getcwd()
        try:
            with open(self.m_path + "\\setting.ini", 'r', encoding = 'utf-8-sig') as f:
                self.Para = f.readlines()
                for i in range(0, 6):
                    self.Para[i] = self.Para[i].strip('\n') # 去除过行
                self.email_user.setText(str(self.Para[0]))
                self.password.setText(self.Para[1])
                self.pop3_server.setText(self.Para[2])
                self.path.setText(self.Para[3])
                self.requireSubject.setText(self.Para[4])
                if self.Para[5] == "True": 
                    self.checkBox.setChecked(True)
                else:
                    self.checkBox.setChecked(False)
        except:
            with open(self.m_path + "\\setting.ini", 'w') as f:
                for i in range(0, 6):
                    f.write(':?\n') # 创建文件并写入占位
            with open(self.m_path + "\\setting.ini", 'r', encoding = 'utf-8-sig') as f:
                self.Para = f.readlines()
        print(self.Para)

        self.tabWidget.setCurrentIndex(0) # 标签页默认页面为第0页
        self.state.setText("初始化完毕")
        self.progressBar.setValue(100)

        ##############################################
    
    ##############槽###############
    def __setProgressBar(self,message):
        self.progressBar.setValue(int(message))

    def __showCheckMessage(self, message):
        self.m_checking = False
        print("{}".format(message))
        self.state.setText(str(message))

    def __showCoreMessage(self, message):
        self.m_coreRunning = False
        print("{}".format(message))
        self.state.setText(str(message))

    def __setState(self, message):
        self.state.setText(str(message))

 #########################增加的线程触发函数##############################
    def __gotoCheck(self):
        if self.m_checking:
            print("正在统计!")
            return

        path = self.path.text()
        if path == ':?': # 空路径判断
            self.tabWidget.setCurrentIndex(1)
            return
        
        self.gotoCheckThread = checkThread(path)
        self.gotoCheckThread.finished_signal.connect(self.__showCheckMessage) # finished_signal的emit将会传递给showmessage作为参数
        self.m_checking = True
        self.gotoCheckThread.start()
        #self.tabWidget.setCurrentIndex(1)
        
    def __gotoCore(self):
        if self.m_coreRunning:
            print("已经在努力收取了哦！")
            return
        for i in range(0, 6):
            if self.Para[i] == ":?":
                self.tabWidget.setCurrentIndex(1)
                return

        self.gotoCoreThread = coreThread(self.Para)

        self.gotoCoreThread.finished_signal.connect(self.__showCoreMessage)
        self.gotoCoreThread.progress_signal.connect(self.__setProgressBar)
        self.gotoCoreThread.state_signal.connect(self.__setState)

        self.m_coreRunning = True
        self.gotoCoreThread.start()
#################保存函数（没有新开线程）###############
    def __gotoSaveParameters(self):
        saveParameters(self)
#######################################################
   

if __name__ == "__main__" :
    print("初始化中...")
    app = QApplication(sys.argv) # 获取命令行参数列表
    ui = Window()
    ui.MainWindow.show()
    sys.exit(app.exec_())
    
    
    '''
    app.exec_()其实就是QApplication的方法，原来这个exec_()方法的作用是“进入程序的主循环直到exit()被调用”，
    如果没有这个方法，运行的时候窗口会闪退，所以show是有发挥作用的，但没有使用exec_()，所以没有进入程序的主循环就直接结束了。
   不用sys.exit(app.exec_())，只使用app.exec_()，程序一样可以正常运行，但是关闭窗口后进程却不会退出
    '''