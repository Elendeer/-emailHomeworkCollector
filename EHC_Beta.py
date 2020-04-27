import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QFileDialog
from PyQt5 import QtWidgets, Qt
from PyQt5.QtCore import QDir # 目录方法

import EHC_GUI
from EHC_core import coreThread
from EHC_Checker import checkThread
from EHC_saveParameters import saveParameters
from EHC_Packing import packingThread

class Window(EHC_GUI.Ui_MainWindow) :#包含了主窗口作为成员变量了
    def __init__(self):
        self.MainWindow = QMainWindow()
        super().setupUi(self.MainWindow)

        self.m_dialogUi = EHC_GUI.Ui_Dialog() # 弹窗UI成员
        self.m_dialog = QDialog(self.MainWindow) # 弹窗窗口成员
        self.m_dialog.setWindowModality(1) # 半模态
        self.m_dialogUi.setupUi(self.m_dialog)

        self.m_packingDiaUI = EHC_GUI.Ui_packingDialog() # 封包备份设置窗口UI成员
        self.m_packingDia = QDialog(self.MainWindow) # 封包备份设置窗口成员
        self.m_packingDia.setWindowModality(1)
        self.m_packingDiaUI.setupUi(self.m_packingDia)

        self.progressBar.setRange(0, 100)
        self.splitter.setStretchFactor(0, 9) # 设置splitter布局为9：1
        self.splitter.setStretchFactor(1, 1)

        ##################增加的按钮触发(主窗口）################
        self.check.clicked.connect(self.__gotoCheck)
        self.get.clicked.connect(self.__gotoCore)
        self.save.clicked.connect(self.__gotoSaveParameters)
        self.pathButton.clicked.connect(self.__setPath)
        self.backup.clicked.connect(self.__setPacking)

        ###############################################
        self.m_checking = False # 作业统计标志位
        self.m_coreRunning = False # 核心功能，即邮箱收作业标志位
        self.m_packing = False # 封包标志位

        #################读取设置文档#################
        self.m_path = os.getcwd()
        if not os.path.isfile(self.m_path + '\\setting.ini') : # 判断文件是否存在，不存在则自动创建
            with open(self.m_path + '\\setting.ini', 'w') as f:
                for i in range(0, 6):
                    if i == 3:
                        f.write(os.path.abspath(self.m_path) + "\n")
                    else :
                        f.write(':?\n') # 创建文件并写入占位
            with open(self.m_path + "\\setting.ini", 'r', encoding = 'utf-8-sig') as f:
                self.Para = f.readlines()
            for i in range(0, 6):
                self.Para[i] = self.Para[i].strip("\n")
        else :
            with open(self.m_path + "\\setting.ini", 'r', encoding = 'utf-8-sig') as f:
                self.Para = f.readlines()
                for i in range(0, 6):
                    self.Para[i] = self.Para[i].strip('\n') # 去除过行
                self.email_user.setText(str(self.Para[0]))
                self.password.setText(self.Para[1])
                self.pop3_server.setText(self.Para[2])
                self.pathText.addItem(self.Para[3])
                self.requireSubject.setText(self.Para[4])
                if self.Para[5] == "True":
                    self.checkBox.setChecked(True)
                else:
                    self.checkBox.setChecked(False)
        print(self.Para)

        self.tabWidget.setCurrentIndex(0) # 标签页默认页面为第0页
        ###############封包备份页面的初始化#################
        if not os.path.isfile(self.Para[3] + '\\pre_list.ini') : # 判断文件是否存在，不存在则自动创建
            with open(self.Para[3] + '\\pre_list.ini', 'w') as f:
                pass
        with open(self.Para[3] + '\\pre_list.ini', 'r', encoding = 'utf-8-sig') as f:
            for i in f.readlines(): # 取前缀用以识别
                self.m_packingDiaUI.itemComboBox.addItem(i.strip('\n'))

        self.m_packingDiaUI.packingName.setText("挺方便欸")

        self.state.setText("初始化完毕")
        self.progressBar.setValue(100)

        ##############################################

    ##############槽###############
    def __setProgressBar(self,message):
        self.progressBar.setValue(int(message))

    def __setState(self, message):
        self.state.setText(str(message))


    def __showCheckMessage(self, message):
        self.m_checking = False
        print("{}".format(message))
        self.state.setText(str(message))

    def __showCoreMessage(self, message):
        self.m_coreRunning = False
        print("{}".format(message))
        self.state.setText(str(message))

    def __showPackMessage(self, message):
        self.m_packing = False
        self.state.setText(str(message))
###################################子窗口触发######################################
    def __setPath(self):

        path = QDir.toNativeSeparators(QFileDialog.getExistingDirectory(self.MainWindow, str("Path"), QDir.currentPath()))
        if (self.pathText.findText(path) == -1):
            self.pathText.addItem(path)
        self.pathText.setCurrentIndex(self.pathText.findText(path))

    def __setPacking(self) :

        self.m_packingDiaUI.startButton.clicked.connect(self.__gotoPack)
        self.m_packingDiaUI.cancelButton.clicked.connect(self.m_packingDia.close)

        self.m_packingDia.show()


 #########################增加的线程触发函数##############################
    def __gotoCheck(self):
        if self.m_checking:
            print("正在统计!")
            return
        if self.m_coreRunning: # 事实上这三个线程并不冲突，只是为了UI整洁暂时不允许同时运行
            print("进度条君正跑着收作业程序哦")
            return
        if self.m_packing:
            print("进度条君正跑着封包备份程序哦")
            return

        path = self.Para[3]
        if path == ':?': # 空路径判断
            self.tabWidget.setCurrentIndex(1)
            return

        self.gotoCheckThread = checkThread(path)

        self.gotoCheckThread.m_finished_signal.connect(self.__showCheckMessage) # m_finished_signal的emit将会传递给showmessage作为参数
        self.gotoCheckThread.m_process_signal.connect(self.__setProgressBar)
        self.gotoCheckThread.m_state_signal.connect(self.__setState)

        self.m_checking = True
        self.gotoCheckThread.start()
        #self.tabWidget.setCurrentIndex(1)

    def __gotoCore(self):
        if self.m_coreRunning:
            print("已经在努力收取了哦！")
            return
        if self.m_packing:
            print("进度条君正跑着封包备份程序哦")
            return
        if self.m_checking:
            print("进度条君正跑着遍历统计程序哦")
            return

        for i in range(0, 6):
            if self.Para[i] == ":?":
                self.tabWidget.setCurrentIndex(1)
                return

        self.gotoCoreThread = coreThread(self.Para)

        self.gotoCoreThread.m_finished_signal.connect(self.__showCoreMessage)
        self.gotoCoreThread.m_progress_signal.connect(self.__setProgressBar)
        self.gotoCoreThread.m_state_signal.connect(self.__setState)

        self.m_coreRunning = True
        self.gotoCoreThread.start()

    def __gotoPack(self) :
        packingName = self.m_packingDiaUI.packingName.text()
        if packingName == '':
            self.m_dialogUi.label.setText("请输入压缩包名称！")
            self.m_dialog.show()
            return

        prefix = self.m_packingDiaUI.itemComboBox.currentText()
        ifDel = self.m_packingDiaUI.ifDelCheckBox.isChecked()
        ifOverwrite = self.m_packingDiaUI.ifOverwrite.isChecked()

        if self.m_packing:
            print("正在封包！")
            return
        if self.m_checking:
            print("进度条君正跑着遍历统计程序哦")
            return
        if self.m_coreRunning: # 事实上这三个线程并不冲突，只是为了UI整洁暂时不允许同时运行
            print("进度条君正跑着收作业程序哦")
            return

        savingPath = self.Para[3] + "\\backup"
        if not os.path.exists(savingPath) : # 判断backup文件夹是否存在，不存在则自动创建
            os.makedirs(savingPath)

        os.chdir(os.path.abspath(savingPath))
        fileList = os.listdir()
        if (packingName + ".zip" in fileList) and (not ifOverwrite) : # 判断是否重名
            self.m_dialogUi.label.setText("压缩包命名重叠！")
            self.m_dialog.show()
            return

        self.gotoPackThread = packingThread(prefix, ifDel, packingName, self.Para[3])

        self.gotoPackThread.m_finished_signal.connect(self.__showPackMessage)
        self.gotoPackThread.m_progress_signal.connect(self.__setProgressBar)
        self.gotoPackThread.m_state_signal.connect(self.__setState)

        self.m_packingDia.close()

        self.m_packing = True
        self.gotoPackThread.start()


#################保存函数（没有新开线程）###############
    def __gotoSaveParameters(self):
        if (saveParameters(self)):
            self.m_dialogUi.label.setText("保存成功！")
            self.m_dialog.show()
        else:
            self.m_dialogUi.label.setText("出错！可能有非法路径！")
            self.m_dialog.show()
            pass
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