import easygui as gui  #导入EasyGUI，用于界面，并将其输入名称简化为“gui”
import time  #导入Time模块，用于等待
import sys  #导入sys模块，用于结束程序
import os
from os import system  #导入os和system模块，用于关闭、重启电脑
PromptTime = 0  #定义提示时间变量
SRTime = 0  #定义关机、重启时间变量
SR = 0  #定义关机、重启变量
Button = 0  #定义记录按钮变量
Button = gui.buttonbox(msg='Hi, welcome! I can aute close or restart your computer.',title = 'Home - Aute Shutdown 1.0.0',choices=('Exit','Next'))
#主页对话框
while not Button == 0:  #判断对话框选项
    if Button == 'Exit':  #退出按钮，结束程序
        gui.msgbox('Exiting……')
        sys.exit()
    elif Button == 'Next':  #下一步按钮，显示警告
        Button = 0
        Button = gui.buttonbox(msg='Warning: Please be responsible for the data loss and computer damage caused by this software!! Do you want to continue?',title = 'Warning - Aute Shutdown 1.0.0',choices=('Exit','Next'))
        #警告
        while not Button == 0:  #判断对话框选项
            if Button == 'Exit':  #退出按钮，结束程序
                gui.msgbox('Exiting……')
                sys.exit()
            elif Button == 'Next':  #下一步按钮，显示第二次警告
                Button = 0
                Button = gui.buttonbox(msg='This is the last warning! Do you want to continue?',title = 'Warning - Aute Shutdown 1.0.0',choices=('Exit','Next'))
                #第二次警告
                while not Button == 0:  #退出按钮，结束程序
                    if Button == 'Exit':
                        gui.msgbox('Exiting……')
                        sys.exit()
                    elif Button == 'Next':  #下一步按钮，启动程序
                        break
PromptTime = int(gui.enterbox(msg='Please settings prompt time. (input number, unit: minutes)',title='Settings Prompt Time - Aute Shutdown 1.0.0')) * 60
#输入提示时间（分钟），并转换为整数秒数
SRTime = int(gui.enterbox(msg='Please settings time to shut down after prompt. (input number, unit: seconds)',title='Settings Shutdown & Restart Time - Aute Shutdown 1.0.0'))
#输入提示后关机的时间（秒），并转换为整数
Button = 0
Button = gui.buttonbox(msg='Do you want to shutdown or restart your computer?',title='Selection Operation - Aute Shutdown 1.0.0',choices=('Shutdown','Restart'))
#选择关机或重启对话框
while not Button == 0:  #判断对话框选项
    if Button == 'Shutdown':  #关机选项，设置模式变量为0
        SR = 0
        break
    elif Button == 'Restart':  #重启选项，设置模式变量为1
        SR = 1
        break
time.sleep(int(PromptTime))  #等待提示时间的秒数
if SR == 0:  #判断操作是关机还是重启，弹出不同的对话框提示用户
    Button = 0
    Button = gui.buttonbox(msg='Your computer will shutdown in '+int(SRTime)+' seconds. Please save your work.',title='Prompt - Aute Shutdown 1.0.0',choices=('Exit Program','OK'))
elif SR == 1:
    Button = 0
    Button = gui.buttonbox(msg='Your computer will restart in '+int(SRTime)+' seconds. Please save your work.',title='Prompt - Aute Shutdown 1.0.0',choices=('Exit Program','OK'))
while not Button == 0:  #判断对话框选项
    if Button == 'Exit Program':  #退出程序
        gui.msgbox('Exiting……')
        sys.exit()
    elif Button == 'OK':  #继续
        break
time.sleep(int(SRTime))  #等待提示后关机的时间
if SR == 0:  #判断操作是关机还是重启，弹出不同的对话框并执行操作
    gui.msgbox(msg='Your computer will shutdown.',title='Shutdown - Aute Shutdown 1.0.0')
    os.system("shutdown -s -t  0.5")  #提示并关机
elif SR == 1:
    gui.msgbox(msg='Your computer will restart.',title='Restart - Aute Shutdown 1.0.0')
    os.system("shutdown -r -t 0.5")  #提示并重启