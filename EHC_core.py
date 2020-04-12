'''
emailHomeworkCollector

require for pre_list.txt
'''

import email
from email.parser import Parser
from email.header import decode_header
import time
import datetime
import re # 正则表达式
import poplib

import time
import os

##########################字符串解码#############################
def decode_str(str_in):
    value, charset = decode_header(str_in)[0]
    if charset: # 不懂为什么要判断
        value = value.decode(charset)
    return value
#########################################################

##########################附件下载和分类#######################
def get_attachment(msg_in, path):
    gotfile = False
    attachment_files=[]

    with open(path + '\\pre_list.txt', 'r', encoding = 'utf-8-sig') as f:
            list_prefix = []
            for i in f.readlines(): # 取前缀用以识别
                list_prefix.append(i.strip('\n'))
        
    print("文件中读取到的前缀列表")
    print(list_prefix)

    for part in msg_in.walk(): # walk()遍历
        # 获取附件名称类型
        file_name = part.get_filename() # 若存在，返回文件名
        
        if file_name:
            h = email.header.Header(file_name)
            # 对附件名称进行解码
            dh = email.header.decode_header(h)
            filename = dh[0][0]
            if dh[0][1]:
                # 将附件名称可读化
                filename = decode_str(str(filename, dh[0][1]))
                print(filename)

            # 下载附件
            try:
                data = part.get_payload(decode = True)
            except:
                print('Download Error :{}'.format(filename))
                raise Exception('Download Error')
            # 无异常时
            else:
                prefix = filename.split(re.findall('[0-9]+?', filename)[0])[0] # 按照学号(数字)切割，学号前面是前缀

                # 根据前缀在指定目录下创建文件，注意二进制文件需要用wb模式打开
                for i in list_prefix:
                    if prefix == i:
                        
                        #######判断路径是否存在######
                        if (os.access(path + '\\' + i, os.F_OK)):
                            print(prefix + "文件夹存在")
                            pass
                        else:
                            os.makedirs(path + '\\' + i)
                            print(prefix + "文件夹不存在，已创建")
                        ########写入附件######
                        with open(path + '\\' + i + '\\' + filename, 'wb') as att_file:
                            att_file.write(data)
                        
                        attachment_files.append(filename)

                        break
                else : # 前缀错误处理
                    print("前缀 " + prefix + " 无法识别")
                    #######判断路径是否存在######
                    if (os.access(path + '\\Unrecognized', os.F_OK)):
                        pass
                    else:
                        os.makedirs(path + '\\Unrecognized')
                    #############在 未识别 文件夹中写入附件###############
                    with open(path + '\\Unrecognized\\' + filename, 'wb') as att_file:
                        att_file.write(data)
                    attachment_files.append(filename)
                
                gotfile = True
        

    return gotfile, attachment_files
###########################################################



# today = str(datetime.date.today()).replace('-','')

def EHC(Para):
    #ui.state.setText("功能连接...")
    #ui.progressBar.setRange(0, 0)

    requireSubject = Para[4]

    email_user = Para[0]
    password = Para[1]
    pop3_server = Para[2]

    path = Para[3]
    if Para[5] == "True":
        ifDel = True
    else :
        ifDel = False

    #ui.state.setText("连接邮箱...")

    # 连接到POP3服务器:
    server = poplib.POP3_SSL(pop3_server,995,timeout=20)
    # 995端口安全传输

    # 可以打开或关闭调试信息:
    server.set_debuglevel(1)
    # 打印POP3服务器的欢迎文字:
    print(server.getwelcome().decode('utf-8'))
    try:
        server.user(email_user)
        server.pass_(password)
    except poplib.error_proto as e:
        print("login error :%s" % e)
        return

    print('Messages: %s. Size: %s' % server.stat())

    resp, mails, octets = server.list()
    index = len(mails)
    print(mails)
   # server.quit()
    
    localtime = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
    #ui.state.setText("收取中...")
    #ui.progressBar.setRange(0, 100)
    #ui.progressBar.setValue(0)
    
    ###################logs目录的判断和创建#####################
    if (os.access(path + '\\logs', os.F_OK)):
        pass
    else:
        os.makedirs(path + '\\logs')
    #####################打开logs目录创建接收记录#####################
    with open(path + "\\logs\\" + localtime + ".txt", "w", encoding = 'utf-8') as f:

        for i in range(1, index + 1):
            try:
                resp, lines, octets = server.retr(i)# retr命令获得第i封邮件
            except:
                print("RETR命令异常")
                continue
            # 邮件的原始文本:
            try:
                msg_content = b'\r\n'.join(lines).decode('utf-8')# 逐行用\r\n连接并解码
            except:
                print("编码异常")
                continue
            # 解析邮件:
            msg = Parser().parsestr(msg_content)# 解析器解析邮件文本
            subject=msg.get('Subject','')
            if subject:
                subject=decode_str(subject)

            
            if subject == requireSubject:
                    # 依照邮件主题获取附件
                try:
                    get, attachment_files = get_attachment(msg, path)
                    
                    if get:
                        for line in attachment_files:
                            f.write(line + '\n')
                    else:
                        print('未从第{}封邮件中获取到附件，可能使用了超大附件功能，请手动上邮箱接收'.format(i))
                        f.write('未从第{}封邮件中获取到附件，可能使用了超大附件功能，请手动上邮箱接收\n'.format(i))
                    if get and ifDel:
                        try:
                            server.dele(i)
                        except: # 可能已经被标记
                            pass
                except Exception: #Download Error
                    pass
            #ui.progressBar.setValue(float(100) / index * i)

    #ui.progressBar.setValue(100)
    try:
        server.quit()
    except:
        print("QUIT命令异常，可能由RETR命令异常引起")
        pass
    #ui.state.setText("收取完成，log已生成")
    #print("收取完成，log已生成")
###################################################################
def entrance(Para):
    
    EHC(Para)


if __name__ == "__main__":# __name__内置变量，指当前模块
    Para = ["", "", "", "", "", ""]
    EHC(Para)