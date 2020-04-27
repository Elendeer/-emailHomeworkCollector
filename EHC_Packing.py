'''
含线程类packingThread
'''
import zipfile
import os
from PyQt5.QtCore import QThread, pyqtSignal # qt多线程

#workingPath = os.path.abspath(os.curdir)
#print(workingPath)

#f = zipfile.ZipFile(workingPath + '\\try.zip', 'w', zipfile.ZIP_DEFLATED) # (保存路径，写入模式，压缩模式)
#f.write(workingPath + "\\setting.ini", "s.ini")
## 单个参数：该目录下的文件全部压缩到压缩文件中；多个参数：前者之文件直接添加到压缩文件中，以后者命名
#f.close()

# Parameters
class packingThread(QThread) :
    m_finished_signal = pyqtSignal(str)
    m_progress_signal = pyqtSignal(int) # 用于发射进度信号
    m_state_signal = pyqtSignal(str) # 用于发射状态信号（显示在进度条上方

    def __init__(self, prefix, ifDel, packingName, workingPath, parent = None) :
        super().__init__(parent)

        self.m_prefix = prefix
        self.m_ifDel = ifDel
        self.m_packingName = packingName + ".zip"
        self.m_workingPath = workingPath

    def run(self) :
        self.m_state_signal.emit("准备压缩...")

        savingPath = self.m_workingPath + "\\backup"

        packingPath = self.m_workingPath + "\\" + self.m_prefix

        f = zipfile.ZipFile(savingPath + '\\' + self.m_packingName, "w", zipfile.ZIP_DEFLATED)
        os.chdir(os.path.abspath(packingPath))
        fileList = os.listdir()
        print(fileList)

        length = len(fileList)
        print(length)
        index = 0
        self.m_progress_signal.emit(0)
        self.m_state_signal.emit("压缩中，共{}份文件...".format(length))

        if self.m_ifDel :
            for _file in fileList:
                f.write(packingPath + '\\' + _file, _file)
                os.remove(packingPath + "\\" + _file)
                index = index + 1
                self.m_progress_signal.emit(100 / length * index)
        else :
            for _file in fileList:
                f.write(packingPath + '\\' + _file, _file)
                index = index + 1
                self.m_progress_signal.emit(100 / length * index)

        f.close()
        self.m_finished_signal.emit("封包完成！请前往backup文件夹查看！")