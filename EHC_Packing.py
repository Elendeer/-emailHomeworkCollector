'''
含线程类PackingThread
'''
import zipfile
import os

#workingPath = os.path.abspath(os.curdir)
#print(workingPath)

#f = zipfile.ZipFile(workingPath + '\\try.zip', 'w', zipfile.ZIP_DEFLATED) # (保存路径，写入模式，压缩模式)
#f.write(workingPath + "\\setting.ini", "s.ini")
## 单个参数：该目录下的文件全部压缩到压缩文件中；多个参数：前者之文件直接添加到压缩文件中，以后者命名
#f.close()

# Parameters
savingPath = "D:" # savingPath不能不存在S
packingPath = "D:\\B-Work\\C++"
ifDel = False
packName = "testing" + ".zip"

f = zipfile.ZipFile(savingPath + '\\' + packName, "w", zipfile.ZIP_DEFLATED)
os.chdir(os.path.abspath(packingPath))
fileList = os.listdir()

print(fileList)

for _file in fileList:
    f.write(packingPath + '\\' + _file, _file)


f.close()