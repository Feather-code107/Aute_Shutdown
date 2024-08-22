import easygui as gui  #导入EasyGUI，用于界面，并将其输入名称简化为“gui”
import time  #导入Time模块，用于等待
import sys  #导入sys模块，用于结束程序
import os
from os import system  #导入os和system模块，用于关闭、重启电脑
PromptTime = 0  #定义提示时间变量
SRTime = 0  #定义关机、重启时间变量
SR = 0  #定义关机、重启变量
Button = 0  #定义记录按钮变量
Button = gui.buttonbox(msg='您好，欢迎！我可以关闭或重启您的计算机。',title = '主页 - Aute Shutdown 1.0.1',choices=('退出程序','下一步'))
#主页对话框
while not Button == 0:  #判断对话框选项
    if Button == '退出程序':  #退出按钮，结束程序
        gui.msgbox('点击 “OK” 退出程序。')
        sys.exit()
    elif Button == '下一步':  #下一步按钮，显示警告
        Button = 0
        Button = gui.buttonbox(msg='警告：本软件造成的数据丢失、计算机损坏请自行负责！！您要继续吗？',title = '警告 - Aute Shutdown V1.0.1',choices=('退出程序','下一步'))
        #警告
        break
while not Button == 0:  #判断对话框选项
    if Button == '退出程序':  #退出按钮，结束程序
        gui.msgbox('点击 “OK” 退出程序。')
        sys.exit()
    elif Button == '下一步':  #下一步按钮，显示第二次警告
        Button = 0
        Button = gui.buttonbox(msg='This is the last warning! Do you want to continue?',title = 'Warning - Aute Shutdown V1.0.1',choices=('退出程序','下一步'))
        #第二次警告
        while not Button == 0:  #退出按钮，结束程序
            if Button == '退出程序':
                gui.msgbox('点击 “OK” 退出程序。')
                sys.exit()
            elif Button == '下一步':  #下一步按钮，启动程序
                break
PromptTime = int(gui.enterbox(msg='请设置提示时间。（输入整数，单位：分钟）',title='设置提示时间 - Aute Shutdown 1.0.1')) * 60
#输入提示时间（分钟），并转换为整数秒数
SRTime = int(gui.enterbox(msg='请设置提示后关机 & 重启的时间. (输入整数，单位：秒)',title='设置提示后关机 & 重启的时间 - Aute Shutdown V1.0.1'))
#输入提示后关机的时间（秒），并转换为整数
Button = 0
Button = gui.buttonbox(msg='你想要关闭还是重启您的计算机？',title='选择操作 - Aute Shutdown V1.0.0',choices=('关闭','重启'))
#选择关机或重启对话框
while not Button == 0:  #判断对话框选项
    if Button == '关闭':  #关闭选项，设置模式变量为0
        SR = 0
        break
    elif Button == '重启':  #重启选项，设置模式变量为1
        SR = 1
        break
time.sleep(int(PromptTime))  #等待提示时间的秒数
if SR == 0:  #判断操作是关机还是重启，弹出不同的对话框提示用户
    Button = 0
    Button = gui.buttonbox(msg='你的计算机将在 '+int(SRTime)+' 秒后关机。请保存你的工作。',title='关机提示 - Aute Shutdown V1.0.1',choices=('退出程序','确定'))
elif SR == 1:
    Button = 0
    Button = gui.buttonbox(msg='你的计算机将在 '+int(SRTime)+' 秒后重启。请保存你的工作。',title='重启提示 - Aute Shutdown V1.0.1',choices=('退出程序','确定'))
while not Button == 0:  #判断对话框选项
    if Button == '退出程序':  #退出程序
        gui.msgbox('点击 “OK” 退出程序。')
        sys.exit()
    elif Button == '确定':  #继续
        break
time.sleep(int(SRTime))  #等待提示后关机的时间
if SR == 0:  #判断操作是关机还是重启，弹出不同的对话框并执行操作
    gui.msgbox(msg='您的计算机将要关机。',title='Shutdown - Aute Shutdown V1.0.1')
    os.system("shutdown -s -t  0.5")  #提示并关机
elif SR == 1:
    gui.msgbox(msg='您的计算机将要重启。',title='Restart - Aute Shutdown V1.0.1')
    os.system("shutdown -r -t 0.5")  #提示并重启