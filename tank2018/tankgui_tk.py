# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import socket
import tkinter as tk
# import tank_start_client as tsc
import os
# import webbrowser


class TankGui(object):

    def __init__(self):
        hostaddr = socket.gethostbyname(
            socket.getfqdn(socket.gethostname()))  # 获取本机IP
        self.ADDR = (hostaddr, 7777)

        # 连接服务器
    def serve_forever(self):
        # self.conn = socket.socket()
        # self.conn.connect(self.ADDR)
        self.login_gui()

    def login_gui(self):
        self.root = tk.Tk()
        self.root.geometry("800x400")
        self.root.title("登录界面")
        # 背景图片
        bgimage = tk.PhotoImage(file='tank2018/TKimage/login_bg.png')
        lab1 = tk.PhotoImage(file='tank2018/TKimage/lab1.png')
        lab2 = tk.PhotoImage(file='tank2018/TKimage/lab2.png')
        # label控件
        self.label = tk.Label(self.root, image=bgimage,
                              compound=tk.CENTER).pack()

        self.label1 = tk.Label(self.root, text="账号：",
                               fg='#F0F0F0', image=lab1, compound=tk.CENTER)
        self.label1.place(x=20, y=280, width=50, height=25)

        self.label2 = tk.Label(self.root, text="密码：", fg='#F0F0F0', image=lab1,
                               compound=tk.CENTER)
        self.label2.place(x=205, y=280, width=50, height=25)

        self.label3 = tk.Label(self.root, text="", fg='red', image=lab2,
                               compound=tk.CENTER)
        self.label3.place(x=110, y=300, width=150, height=25)
        # text控件
        self.entry1 = tk.Entry(self.root, )
        self.entry1.place(x=80, y=280, width=110)
        self.entry2 = tk.Entry(self.root, show="*")
        self.entry2.place(x=260, y=280, width=110)
        # button控件
        self.button1 = tk.Button(self.root, text="注册", fg='#F0F0F0',
                                 image=lab1, compound=tk.CENTER, relief='flat',
                                 command=self.register)
        self.button1.place(x=70, y=320, width=50, height=25)

        self.button2 = tk.Button(self.root, text="登录", fg='#F0F0F0',
                                 image=lab1, compound=tk.CENTER, relief='flat', command=self.login)
        self.button2.place(x=250, y=320, width=50, height=25)

        self.root.mainloop()

    def homegui(self):
        self.root1 = tk.Tk()
        self.root1.geometry("400x400")
        self.root1.title("个人中心")
        self.label = tk.Label(self.root1, width=400,
                              height=600, bg='#FFF',).pack()
        lab1 = tk.PhotoImage(file='TKimage/tx.png')

        self.label1 = tk.Label(self.root1, bg='#FFF',
                               image=lab1, compound=tk.CENTER)
        self.label1.place(x=30, y=30, height=180, width=180)

        self.label11 = tk.Label(self.root1, bg='#FFF', text="昵称：")
        self.label11.place(x=220, y=46, height=25, width=50)
        self.label12 = tk.Label(self.root1, bg='#FFF', text="UID：")
        self.label12.place(x=220, y=87, height=25, width=50)
        self.label13 = tk.Label(self.root1, bg='#FFF', text="win：")
        self.label13.place(x=220, y=128, height=25, width=50)
        self.label14 = tk.Label(self.root1, bg='#FFF', text="lose：")
        self.label14.place(x=220, y=169, height=25, width=50)

        self.label21 = tk.Label(self.root1, bg='#FFF',
                                anchor='e', text="xxxxxx")
        self.label21.place(x=280, y=46, height=25, width=100)
        self.label22 = tk.Label(self.root1, bg='#FFF',
                                anchor='e', text="00001")
        self.label22.place(x=280, y=87, height=25, width=100)
        self.label23 = tk.Label(self.root1, bg='#FFF', anchor='e', text="238")
        self.label23.place(x=280, y=128, height=25, width=100)
        self.label24 = tk.Label(self.root1, bg='#FFF', anchor='e', text="15")
        self.label24.place(x=280, y=169, height=25, width=100)

        btn = tk.PhotoImage(file='images/login/tankstart.png')
        self.button1 = tk.Button(self.root1, fg='#F0F0F0',
                                 image=btn, compound=tk.CENTER, relief='flat',
                                 command=self.start_game)
        self.button1.place(x=80, y=285, width=240, height=40)
        self.root1.mainloop()

    # 打开注册官网
    def register(self):
        os.system(
            ' "C:/Program Files/Mozilla Firefox/firefox.exe" \
            http://www.tmooc.cn/')

        # webbrowser.open('http://www.tmooc.cn/')
        self.label3["text"] = " "

    def login(self):
        name = self.entry1.get()
        pwd = self.entry2.get()
        msg = "LG#%s#%s" % (name, pwd)
        self.conn.send(msg.encode())
        data = self.conn.recv(2048).decode()
        if data == "OK":
            self.go_homegui()
        elif data == "UorPisError":
            self.label3["text"] = ""
            self.label3["text"] = "用户名或密码，请重试！"

    def go_homegui(self):
        self.root.destroy()
        self.homegui()

    def start_game(self):
        self.root1.destroy()
        tsc.main()


def main():
    tank = TankGui()
    tank.serve_forever()


if __name__ == '__main__':
    main()
