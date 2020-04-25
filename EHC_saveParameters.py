import os

######################保存设置函数########################

def saveParameters(ui) :
    ui.Para[0] = str(ui.email_user.text())
    ui.Para[1] = str(ui.password.text())
    ui.Para[2] = str(ui.pop3_server.text())
    ui.Para[3] = str(ui.pathText.currentText())
    ui.Para[4] = str(ui.requireSubject.text())
    ui.Para[5] = str(ui.checkBox.isChecked())
    for i in range(0, 6):
        if ui.Para[i] =='':
            ui.Para[i] = ":?" # 占位

#    ###################指定目录的判断和创建#####################
#    if (os.access(ui.Para[3], os.F_OK)):
#        pass
#    else:
#        os.makedirs(ui.Para[3])
    try:
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

    except:
        return False # 非法目录将使关键文件创建失败，此时返回false
    #######################写入设置#########################
    with open(ui.m_path + "\\setting.ini", 'w', encoding = 'utf-8') as f:
        for i in range(0, 6):
            f.write(ui.Para[i] + '\n')

    print(ui.Para)
    return True
#############################################