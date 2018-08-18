# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import socket
import threading
import pymysql
import time

#文件的存储因为有配合djiango的使用所以数据库是共用的
class LoginSwrver(object):

    def __init__(self):
        self.ADDR = ("0.0.0.0", 7777)
        self.name = ""
        self.pwd = ""
        # 服务器头像存储文件夹路径
        self.path = r'C:\Users\Administrator\Desktop\2018tank-0723\Tank2018-GUI\tank2018'

    # 连接套接字
    def client_socket(self):
        self.sock = socket.socket()
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(self.ADDR)
        self.sock.listen(10)

    # 连接数据库
    def conn_sql(self):
        print('conn_sql')
        self.db = pymysql.connect(
            "localhost", "root", "tarena", charset="utf8")
        self.cur = self.db.cursor()
        self.cur.execute("use Tank;")

    # 创建线程
    def serve_forever(self):
        self.client_socket()
        self.conn_sql()
        print("Listen...")
        while True:
            conn, addr = self.sock.accept()
            print(addr)
            self.clientThread = threading.Thread(
                target=self.handle_thing, args=(conn,))
            self.clientThread.setDaemon(True)
            self.clientThread.start()

    # 线程事件
    def handle_thing(self, conn):
        self.conn = conn
        while True:
            data = conn.recv(2048).decode()
            data = data.split("#")
            if data[0] == "LG":
                self.login(data)
            elif data[0] == "QR":
                self.query(data)
                time.sleep(0.0000000000000000000001)
                self.favicon()
            elif data[0] == "Q":
                print(self.name, "退出！")

    # 登录函数
    def login(self, data):
        # data-->[flag,account,pwd]
        self.account = data[1]
        self.pwd = data[2]
        self.cur.execute(
            "select email,pwd from user \
            where email ='%s';" % self.account)
        count = self.cur.fetchall()
        try:
            if count[0][0] == self.account and count[0][1] == self.pwd:
                self.conn.send(b"OK")
            else:
                self.conn.send(b"UorPisError")
        except:
            self.conn.send(b"UorPisError")

    # 个人信息查询函数，并发送
    def query(self, data):
        self.account = data[1]
        self.cur.execute(
            "select nickname,uid,win,lose,favicon from user \
            where email ='%s';" % self.account)
        self.count = self.cur.fetchall()
        print(self.count)
        msg = '%s#%s#%s#%s' % (self.count[0][0], self.count[0][
            1], self.count[0][2], self.count[0][3])

        self.conn.send(msg.encode())

    #发送头像图片给客户端
    def favicon(self):
        iconpath = self.path + '\\'+self.count[0][4]
        with open(iconpath, "rb") as f:
            data = f.read()
        self.conn.send(data)
        print(iconpath)


def main():
    tank = LoginSwrver()
    tank.serve_forever()


if __name__ == '__main__':
    main()
