import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog

from functools import partial # 用于创建偏函数
from PyQt5.QtCore import QThread, pyqtSignal # qt多线程

import EHC_GUI
import EHC_core # 主框架
import EHC_Checker

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

if __name__ == "__main__" :
    print("初始化中...")
    

    app = QApplication(sys.argv) # 获取命令行参数列表
    MainWindow = QMainWindow() #创建主窗口对象
    ui = EHC_GUI.Ui_MainWindow() # 创建带UI的应用程序
    ui.setupUi(MainWindow) # 主窗口中放置UI
    
    ############################初始化##############################

    ui.tabWidget.setCurrentIndex(0) # 标签页默认页面为第0页



    ui.state.setText("初始化完毕")
    ui.progressBar.setValue(100)
    MainWindow.show()



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