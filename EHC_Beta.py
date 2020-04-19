import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog

from functools import partial # 用于创建偏函数
from PyQt5.QtCore import QThread, pyqtSignal # qt多线程

import EHC_GUI
import EHC_core # 主框架
import EHC_Checker


########################线程类#########################
class checkThread(QThread):
    finished_signal = pyqtSignal(str) # 信号

    def __init__(self, path, parent = None):
        super().__init__(parent)
        self.m_path = path
    
    def run(self):
        EHC_Checker.EHC_Check(self.m_path)
        self.finished_signal.emit("统计完成")

class coreThread(QThread):
    finished_signal = pyqtSignal(str)

    def __init__(self, Para, parent = None):
        super().__init__(parent)
        self.m_Para = Para

    def run(self):
        EHC_core.entrance(self.m_Para)
        self.finished_signal.emit("收取完成，log已生成")
#######################################################



######################函数########################

def saveParameters(ui) :
    a = ui.email_user.text()
    print(a)
    ui.Para[0] = str(ui.email_user.text())
    ui.Para[1] = str(ui.password.text())
    ui.Para[2] = str(ui.pop3_server.text())
    ui.Para[3] = str(ui.path.text())
    ui.Para[4] = str(ui.requireSubject.text())
    ui.Para[5] = str(ui.checkBox.isChecked())
    for i in range(0, 6):
        if ui.Para[i] =='':
            ui.Para[i] = ":?" # 占位

    ###################指定目录的判断和创建#####################
    if (os.access(ui.Para[3], os.F_OK)):
        pass
    else:
        os.makedirs(ui.Para[3])
    ###################关键文件的判断和创建#####################
    try:
        with open(ui.Para[3] + "\\name_list.txt", 'r',  encoding = 'utf-8') as f:
            pass
    except:
        with open(ui.Para[3] + "\\name_list.txt", 'w',  encoding = 'utf-8') as f:
            pass
    try:
        with open(ui.Para[3] + "\\pre_list.txt", 'r', encoding = 'utf-8') as f:
            pass
    except:
        with open(ui.Para[3] + "\\pre_list.txt", 'w', encoding = 'utf-8') as f:
            pass
        
    #######################写入设置#########################
    with open(ui.m_path + "\\setting.ini", 'w', encoding = 'utf-8') as f:
        for i in range(0, 6):
            f.write(ui.Para[i] + '\n')

    print(ui.Para)
    #print(path)
    #print(ifDel)
#############################################

class Window(EHC_GUI.Ui_MainWindow) :#包含了主窗口作为成员变量了
    def __init__(self):
        self.MainWindow = QMainWindow()
        super().setupUi(self.MainWindow)
        ##################增加的按钮触发################
        self.check.clicked.connect(self.gotoCheck)
        self.get.clicked.connect(self.gotoCore)

        ###############################################


        self.m_checking = False # 作业统计标志位
        self.m_coreRunning = False # 核心功能，即邮箱收作业标志位
        
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
    
    def showCheckMessage(self, message):
        self.m_checking = False
        print("{}".format(message))
    def showCoreMessage(self, message):
        self.m_coreRunning = False
        print("{}".format(message))


 #########################增加的线程触发函数##############################
    def gotoCheck(self):
        if self.m_checking:
            print("正在统计!")
            return

        path = self.path.text()
        if path == ':?': # 空路径判断
            self.tabWidget.setCurrentIndex(1)
            return
        
        self.gotoCheckThread = checkThread(path)
        self.gotoCheckThread.finished_signal.connect(self.showCheckMessage) # finished_signal的emit将会传递给showmessage作为参数
        self.m_checking = True
        self.gotoCheckThread.start()
        #self.tabWidget.setCurrentIndex(1)
        
    def gotoCore(self):
        if self.m_coreRunning:
            print("正在收取！")
            return
        for i in range(0, 6):
            if self.Para[i] == ":?":
                self.tabWidget.setCurrentIndex(1)
                return

        self.gotoCoreThread = coreThread(self.Para)
        self.gotoCoreThread.finished_signal.connect(self.showCoreMessage)
        self.m_coreRunning = True
        self.gotoCoreThread.start()

#######################################################
   

if __name__ == "__main__" :
    print("初始化中...")
    

    app = QApplication(sys.argv) # 获取命令行参数列表
    #MainWindow = QMainWindow() #创建主窗口对象
    ui = Window() # 创建带UI的应用程序
    #ui.setupUi(MainWindow) # 主窗口中放置UI的操作已经在创建对象时完成
    
    ############################初始化##############################

    ui.tabWidget.setCurrentIndex(0) # 标签页默认页面为第0页



    ui.state.setText("初始化完毕")
    ui.progressBar.setValue(100)
    ui.MainWindow.show()



#############################按钮检测#################################
    
    #ui.get.clicked.connect(partial(EHC_core.entrance, ui, Para))
    ui.save.clicked.connect(partial(saveParameters, ui))
    
    #ui.check.clicked.connect(partial(EHC_Checker.EHC_Check, ui, Para))
    
    
######################################################################

    sys.exit(app.exec_())
    
    
    '''
    app.exec_()其实就是QApplication的方法，原来这个exec_()方法的作用是“进入程序的主循环直到exit()被调用”，
    如果没有这个方法，运行的时候窗口会闪退，所以show是有发挥作用的，但没有使用exec_()，所以没有进入程序的主循环就直接结束了。
   不用sys.exit(app.exec_())，只使用app.exec_()，程序一样可以正常运行，但是关闭窗口后进程却不会退出
    '''