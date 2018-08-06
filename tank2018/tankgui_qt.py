#!/usr/bin/python3
from __future__ import unicode_literals
# -*- coding: utf-8 -*-

import sys
import socket
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLineEdit, QLabel)
from PyQt5.QtCore import Qt, QRect, QCoreApplication
from PyQt5 import QtGui
import webbrowser
import personal


class Tank2018(QWidget):

    def __init__(self):
        super().__init__()
        self.style = """ 
                QPushButton{background-color:#00aeff;color:white;} 
                #tank2018{ background:#2 02734; }
                #linet{background-color:#11151b;color:#474b53; border: 1px solid #00aeff;border-radius:3px}
                #btn1{ background-color:#202734;color:#474b53; border:0px;font:900 25px "Microsoft YaHei";}
                #btn2{ background-color:#202734;color:#474b53; border:0px;font:900 17px "Microsoft YaHei";}
                #btn4{background-color:#202734;color:#00aeff; border:0px;font:15px "Microsoft YaHei";}
                #label1{color:#474b53;font:13px "Microsoft YaHei";}
                #label4{background-color:#202734;color:red;font:13px "Microsoft YaHei";padding-left:30px}
               """
        self.setStyleSheet(self.style)  # 可以像写csss一样对控件进行设置
        self.setWindowFlags(Qt.FramelessWindowHint)  # 去除原始窗口的边框
        self.increment = 0

        hostaddr = socket.gethostbyname(
            socket.getfqdn(socket.gethostname()))  # 获取本机IP
        self.ADDR = (hostaddr, 7777)

    def serve_forever(self):
        self.conn = socket.socket()
        self.conn.connect(self.ADDR)
        self.login_gui()

    # 主界面
    def login_gui(self):
        self.setGeometry(400, 150, 360, 510)  # 设置界面出现的屏幕中的位置以及大小
        self.setWindowTitle('Tank2018')
        self.setObjectName("tank2018")
        _translate = QCoreApplication.translate

        # 商标区域
        self.label = QLabel(self)
        self.label.setGeometry(QRect(90, 50, 180, 90))
        self.label.setObjectName('label')
        # 商标背景
        self.label.setAutoFillBackground(True)
        palette1 = QtGui.QPalette()
        palette1.setBrush(self.backgroundRole(),
                          QtGui.QBrush(QtGui.QPixmap
                                       ('QTimage/LOGO.png')))
        self.label.setPalette(palette1)

        # 错误提示区域
        self.label4 = QLabel(self)
        self.label4.setGeometry(QRect(0, 155, 360, 35))
        self.label4.setObjectName('label4')
        # self.label3.hide()

        # 最小化按钮
        self.btn1 = QPushButton("-", self)
        self.btn1.clicked.connect(self.showMinimized)  # 最小化事件
        self.btn1.setObjectName('btn1')
        self.btn1.setGeometry(QRect(305, 12, 15, 15))

        # 关闭界面按钮
        self.btn2 = QPushButton("×", self)
        self.btn2.clicked.connect(self.close)  # 关闭事件
        self.btn2.setObjectName('btn2')
        self.btn2.setGeometry(QRect(330, 10, 15, 15))

        # 账号密码输入栏
        self.label1 = QLabel('账号', self)
        self.label1.setGeometry(QRect(35, 164, 50, 20))
        self.label1.setObjectName('label1')

        self.linet1 = QLineEdit(self)
        self.linet1.setGeometry(QRect(30, 187, 300, 30))
        self.linet1.setObjectName('linet')

        self.label2 = QLabel('密码', self)
        self.label2.setGeometry(QRect(35, 222, 50, 20))
        self.label2.setObjectName('label1')

        self.linet2 = QLineEdit(self)
        self.linet2.setGeometry(QRect(30, 245, 300, 30))
        self.linet2.setObjectName('linet')
        self.linet2.setEchoMode(QLineEdit.Password)

        # 登录按钮
        self.btn3 = QPushButton("登录", self)
        self.btn3.clicked.connect(self.login)  # 登录事件
        self.btn3.clicked.connect(self.show)
        self.btn3.setObjectName('btn3')
        self.btn3.setGeometry(QRect(30, 305, 300, 35))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.btn3.setFont(font)
        self.btn3.setCursor(QtGui.QCursor(Qt.PointingHandCursor))

        
        self.label3 = QLabel(self)
        # self.btn4.clicked.connect()
        self.label3.setGeometry(QRect(30, 360, 300, 20))
        self.label3.setText(_translate(
            "self", "<html><head/><body><p align=\"center\">\
            <span style=\" font-size:10pt; color:#474b53;\">或需要以下操作 \
            </span></p></body></html>"))

        # 注册链接按钮
        self.btn4 = QPushButton("免费创建游戏通行证", self)
        self.btn4.clicked.connect(self.register)
        self.btn4.setGeometry(QRect(30, 410, 300, 20))
        self.btn4.setObjectName('btn4')
        self.btn4.setCursor(QtGui.QCursor(Qt.PointingHandCursor))

        # 帮助链接按钮
        self.btn5 = QPushButton("无法登录？", self)
        self.btn5.clicked.connect(self.help)
        self.btn5.setGeometry(QRect(30, 440, 300, 20))
        self.btn5.setObjectName('btn4')
        self.btn5.setCursor(QtGui.QCursor(Qt.PointingHandCursor))

        self.show()

    # 几条画线的函数
    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()

    def drawLines(self, qp):
        pen = QtGui.QPen(QtGui.QColor('#474b53'), 1, Qt.SolidLine)

        qp.setPen(pen)
        # 2个数字是一对坐标
        qp.drawLine(105, 0, 110, 10)
        qp.drawLine(255, 0, 250, 10)
        qp.drawLine(110, 10, 250, 10)

        qp.drawLine(30, 368 + self.increment, 120, 368 + self.increment)
        qp.drawLine(230, 368 + self.increment, 330, 368 + self.increment)

    # 重写三个方法使我们的Tank2018窗口支持拖动,上面参数window就是拖动对象
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QtGui.QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_drag:
            self.move(QMouseEvent.globalPos() - self.m_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag = False
        self.setCursor(QtGui.QCursor(Qt.ArrowCursor))

    def login(self):
        self.account = self.linet1.text()
        pwd = self.linet2.text()
        # 连接数据库查询账号
        msg = "LG#%s#%s" % (self.account, pwd)
        self.conn.send(msg.encode())
        data = self.conn.recv(2048).decode()

        if self.account == "":
            flag = 'NoName'
            self.erorr_gui(flag)
        elif pwd == "":
            flag = "NoPwd"
            self.erorr_gui(flag)
        elif data == "OK":
            self.close()
            pe = personal.PersonalCenter()
            pe.serve_forever(self.account)
            pe.show()
        elif data == "UorPisError":
            flag = data
            self.erorr_gui(flag)

    # 错误提示界面
    def erorr_gui(self, flag):
        self.setGeometry(400, 150, 360, 550)
        self.increment = 40
        self.label1.setGeometry(QRect(35, 164 + self.increment, 50, 20))
        self.linet1.setGeometry(QRect(30, 187 + self.increment, 300, 30))
        self.label2.setGeometry(QRect(35, 222 + self.increment, 50, 20))
        self.linet2.setGeometry(QRect(30, 245 + self.increment, 300, 30))
        self.btn3.setGeometry(QRect(30, 305 + self.increment, 300, 35))
        self.label3.setGeometry(QRect(30, 360 + self.increment, 300, 20))
        self.btn4.setGeometry(QRect(30, 410 + self.increment, 300, 20))
        self.btn5.setGeometry(QRect(30, 440 + self.increment, 300, 20))

        self.style = ''' 
                QPushButton{background-color:#00aeff;color:white; } 
                #tank2018{ background:#202734; }
                #linet{background-color:#11151b;color:#474b53; border: 1px solid #00aeff;border-radius:3px}
                #btn1{ background-color:#202734;color:#474b53; border:0px;font:900 25px "Microsoft YaHei";}
                #btn2{ background-color:#202734;color:#474b53; border:0px;font:900 17px "Microsoft YaHei";}
                #btn4{background-color:#202734;color:#00aeff; border:0px;font:15px "Microsoft YaHei";}
                #label1{color:#474b53;font:13px "Microsoft YaHei";}
                #label4{background-color:#270a0c;color:red;font:15px  "Microsoft YaHei";padding-left:30px}
               '''

        if flag == 'NoName':
            self.label4.setText('请输入用户名')
        elif flag == "NoPwd":
            self.label4.setText('请输入密码')
        elif flag == "UorPisError":
            self.label4.setText('用户名或密码错误')

    # 注册跳转
    def register(self):
        webbrowser.open("http://www.baidu.com")

    # 帮助跳转
    def help(self):
        webbrowser.open("http://www.baidu.com")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Tank2018()
    ex.serve_forever()
    sys.exit(app.exec_())
