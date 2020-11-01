import os
from tkinter import Tk, Menu, Label, Button
from tkinter.filedialog import askopenfilenames
from tkinter.messagebox import showinfo,showerror
from remove_bg import remove_bg
# from multiprocessing import Process
'''
打开图形界面，选择需要处理的图片
'''
IMGPATH = ''

class GUI(object):

    def __init__(self, window):
        self.window = window
        self.window.title('去除图片背景')
        self.window.geometry('300x200')#设置窗口大小
        menubar = Menu(self.window)

        # 定义空菜单
        filemenu = Menu(menubar,tearoff=0)
        filemenu.add_command(label='帮助', command=self.helpme)
        filemenu.add_separator()
        # filemenu.add_separator()#分割线
        # filemenu.add_command(label='作者', command=self.whoisauthor)

        # menubar.add_cascade(label="File", menu=filemenu)#放入菜单中
        # self.window.config(menu=menubar)#在窗口显示

        # 显示
        self.l = Label(window, text='liyu？')
        self.l.pack(padx=5, pady=10)  # 固定标签位置
        # self.l2 = Label(window, text='')
        # self.l2.pack(padx=5, pady=20)

        # 选择图片
        btn1 = Button(window, text='选择图片', width=15, height=2, command=self.get_img)
        btn1.pack()

        # 生成图片
        self.send_btn = Button(window, text='去除背景', width=15, height=2, command=self.gen_img)
        self.send_btn.pack()

    def helpme(self):
        showerror("帮助","二两与csdn作者陈加伦")
    # def whoisauthor(self):
    #     showerror('作者', '陈加伦')

    def get_img(self):
        global IMGPATH
        # 选择文件 可以定义图片的格式
        filenames = askopenfilenames(filetypes=(("jpeg img", "*.jpeg"), ("jpg img", "*.jpg"), ("png img", "*.png")))
        if len(filenames) > 0:
            fnlist = [fn for fn in filenames]
            fnstr = '\n'.join(fnlist)
            # self.l.config(text="已选择的文件：")
            self.l.config(text=fnstr)
            IMGPATH = fnlist
        else:
            self.l.config(text='目前没有选择任何图片文件')

    def gen_img(self):
        global IMGPATH
        respathlist = []
        for imgpath in IMGPATH:
            filepath,tempfilename = os.path.split(imgpath)
            filename,extension = os.path.splitext(tempfilename)
            remove_bg(imgpath)
            showinfo('完成生成', f'{filename}图片处理已完成')
            respathlist.append(imgpath)
        respath = ' '.join(respathlist)
        showinfo('完成生成', f'图片处理完成，路径为:{respath}')

if __name__ == '__main__':
    # 生成主窗口对象
    window = Tk()
    GUI(window)
    # 显示窗口 一直消息循环
    window.mainloop()
    
