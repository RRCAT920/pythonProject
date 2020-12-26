# -*- coding: utf-8 -*-
from tkinter import *


class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()  # 将本Widgets加入父容器
        self._create_widgets()

    def _create_widgets(self):
        self.hello_lb = Label(self, text='Hello, world!')
        self.hello_lb.pack()  # 还有grid()布局

        self.quit_btn = Button(self, text='Quit', command=self.quit)
        self.quit_btn.pack()


app = App()
app.master.geometry('200x50+1500+400')  # 宽x高+左+上
app.master.title('Hello World')  # 设置标题
app.mainloop()  # 主消息循环
