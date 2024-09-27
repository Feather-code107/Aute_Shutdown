import easygui as gui  #导入EasyGUI，用于界面，并将其输入名称简化为“gui”
import sys  #导入sys模块，用于结束程序
import ctypes #导入ctypes模块，用于检测是否以管理员身份运行
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if is_admin():
    import time  #导入Time模块，用于等待
    import os
    from os import system  #导入os和system模块，用于关闭、重启电脑
    PromptTime = 0  #定义提示时间变量
    SRTime = 0  #定义关机、重启时间变量
    Button = "0"  #定义记录按钮变量
    Button = gui.buttonbox(msg='欢迎使用 Aute Shutdown Version 1.0.0，单击“下一步”以继续。'+'                   '+'Aute Shutdown V1.0.0 By Feather  Github：https://github.com/Feather-code107/Aute_Shutdown',title = '主页 - Aute Shutdown V1.0.0',choices=('退出程序','下一步'))
    #判断对话框选项
    if Button == '退出程序':  #退出按钮，结束程序
        gui.msgbox('点击 “OK” 退出程序。')
        sys.exit()
    elif Button == '下一步':  #下一步按钮，显示警告
        Button = gui.buttonbox(msg='警告：本软件造成的数据丢失、计算机损坏请自行负责！！您要继续吗？',title = '警告 - Aute Shutdown V1.0.0',choices=('退出程序','下一步'))
        #警告
        #判断对话框选项
        if Button == '退出程序':  #退出按钮，结束程序
            gui.msgbox('点击 “OK” 退出程序。')
            sys.exit()
        elif Button == '下一步':  #下一步按钮，显示第二次警告
            Button = gui.buttonbox(msg='这是最后一次警告！您要继续吗？',title = '警告 - Aute Shutdown V1.0.0',choices=('退出程序','下一步'))
            #第二次警告
            if Button == '退出程序':  #退出按钮，结束程序
                gui.msgbox('点击 “OK” 退出程序。')
                sys.exit()
            elif Button == '下一步':  #下一步按钮，启动程序
                PromptTime = int(gui.enterbox(msg='请设置提示时间。（输入整数，单位：分钟）',title='设置提示时间 - Aute Shutdown 1.0.0')) * 60
                #输入提示时间（分钟），并转换为整数秒数
                SRTime = int(gui.enterbox(msg='请设置提示后关机＆重启的时间。（输入整数，单位：秒）',title='设置提示后关机 & 重启的时间 - Aute Shutdown V1.0.0'))
                #输入提示后关机的时间（秒），并转换为整数
                Button = gui.buttonbox(msg='你想要关闭还是重启您的计算机？',title='选择操作 - Aute Shutdown V1.0.0',choices=('关闭','重启'))
                #选择关机或重启对话框
                #判断对话框选项
                if Button == '关闭':  #关闭选项
                    time.sleep(int(PromptTime))
                    Button = gui.buttonbox(msg='你的计算机将在 '+int(SRTime)+' 秒后关机。请保存你的工作。',title='关机提示 - Aute Shutdown V1.0.0',choices=('退出程序','确定'))
                    #判断对话框选项
                    if Button == '退出程序':  #退出程序
                        gui.msgbox('点击 “OK” 退出程序。')
                        sys.exit()
                    elif Button == '确定':  #继续
                        time.sleep(int(SRTime))  #等待提示后关机的时间
                        gui.msgbox(msg='您的计算机将要关机。',title='关机 - Aute Shutdown V1.0.0')
                        os.system("shutdown -s -t  0.5")  #提示并关机
                elif Button == '重启':  #重启选项
                    time.sleep(int(PromptTime))
                    Button = gui.buttonbox(msg='你的计算机将在 '+int(SRTime)+' 秒后重启。请保存你的工作。',title='重启提示 - Aute Shutdown V1.0.0',choices=('退出程序','确定'))
                    #判断对话框选项
                    if Button == '退出程序':  #退出程序
                        gui.msgbox('点击 “OK” 退出程序。')
                        sys.exit()
                    elif Button == '确定':  #继续
                        time.sleep(int(SRTime))  #等待提示后重启的时间
                        gui.msgbox(msg='您的计算机将要重启。',title='重启 - Aute Shutdown V1.0.0')
                        os.system("shutdown -r -t 0.5")  #提示并重启
else:
    Button = gui.msgbox(msg='请以管理员权限重新运行程序。',title='权限不足 - Aute Shutdown V1.0.0')
    sys.exit()