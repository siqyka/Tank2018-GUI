#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QApplication, QWidget,QPushButton,
    QLineEdit,QHBoxLayout, QVBoxLayout,QColorDialog,QInputDialog,QFileDialog,
    QLabel,QLineEdit)
from PyQt5.QtCore import Qt,QRect,QCoreApplication
from PyQt5 import QtGui
import webbrowser


class Tank2018_2(QWidget):
    
    def __init__(self):
        super().__init__()
        self.style = """ 
                QPushButton{background-color:#00aeff;color:white;} 
                #tank2018{ background:#202734; }
                #linet{background-color:#11151b;color:#474b53; border: 1px solid #00aeff;border-radius:3px}
                #btn1{ background-color:#202734;color:#474b53; border:0px;font:900 25px "Microsoft YaHei";}
                #btn2{ background-color:#202734;color:#474b53; border:0px;font:900 17px "Microsoft YaHei";}
                #btn4{background-color:#202734;color:#00aeff; border:0px;font:15px "Microsoft YaHei";}
                #label{background-color:#202734;color:#565657;font:13px "Microsoft YaHei";}
                #label4{background-color:#202734;color:red;font:13px "Microsoft YaHei";padding-left:30px}
               """
        self.setStyleSheet(self.style)#可以像写csss一样对控件进行设置
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.increment=0
        self.login_gui()

        

    #主界面
    def login_gui(self):
        self.setGeometry(400, 150, 360, 510)  #设置界面出现的屏幕中的位置以及大小
        self.setWindowTitle('Tank2018') 
        self.setObjectName("tank2018")
        _translate = QCoreApplication.translate

        #头像区域
        self.label = QLabel(self)
        self.label.setGeometry(QRect(50, 40, 120, 120))
        self.label.setObjectName('label-1')
        #头像
        self.label.setAutoFillBackground(True)
        palette1 = QtGui.QPalette()
        palette1.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap('timg.jpg')))  
        self.label.setPalette(palette1)


        self.label2 = QLabel(self)
        self.label2.setGeometry(QRect(200, 100, 120, 60))
        self.label2.setObjectName('label-2')
        #商标背景
        self.label2.setAutoFillBackground(True)
        palette2 = QtGui.QPalette()
        palette2.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap('PLOGO.png')))  
        self.label2.setPalette(palette2)
        

        #错误提示区域
        # self.label4 = QLabel(self)
        # self.label4.setGeometry(QRect(0, 155, 360, 35))
        # self.label4.setObjectName('label4')

        #最小化按钮
        self.btn1 = QPushButton("-",self)
        self.btn1.clicked.connect(self.showMinimized)#最小化事件
        self.btn1.setObjectName('btn1')
        self.btn1.setGeometry(QRect(305, 12, 15, 15))

        #关闭界面按钮
        self.btn2 = QPushButton("×",self)
        self.btn2.clicked.connect(self.close)#关闭事件
        self.btn2.setObjectName('btn2')
        self.btn2.setGeometry(QRect(330, 10, 15, 15))

        #个人信息
        self.label11 = QLabel('昵称:',self)
        self.label11.setGeometry(QRect(50, 180, 40, 20))
        self.label11.setObjectName('label')

        self.label12 = QLabel('UID:',self)
        self.label12.setGeometry(QRect(230, 180, 40, 20))
        self.label12.setObjectName('label')

        self.label13 = QLabel('记忆落在时光里',self)
        self.label13.setGeometry(QRect(90, 180, 100, 20))
        self.label13.setObjectName('label')

        self.label14 = QLabel('00001',self)
        self.label14.setGeometry(QRect(270, 180, 100, 20))
        self.label14.setObjectName('label')

        self.label21 = QLabel('WIN:',self)
        self.label21.setGeometry(QRect(50, 230, 40, 20))
        self.label21.setObjectName('label')

        self.label22 = QLabel('LOSE:',self)
        self.label22.setGeometry(QRect(230, 230, 40, 20))
        self.label22.setObjectName('label')

        self.label21 = QLabel('098',self)
        self.label21.setGeometry(QRect(90, 230, 100, 20))
        self.label21.setObjectName('label')

        self.label22 = QLabel('005',self)
        self.label22.setGeometry(QRect(270, 230, 100, 20))
        self.label22.setObjectName('label')

        self.label3 = QLabel(self)
        self.label3.setGeometry(QRect(30, 300, 300, 20))
        self.label3.setText(_translate("self", "<html><head/><body><p align=\"center\">\
        <span style=\" font-size:15px; color:#00aeff;\"> pirate ship  </span>\
        </p></body></html>"))

        self.btn3 = QPushButton(self)
        #self.btn3.clicked.connect(self.login)   #登录事件
        self.btn3.setObjectName('btn3')
        self.btn3.setGeometry(QRect(55, 380, 250, 50))
        self.btn3.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
        self.btn3.setStyleSheet('#btn3{background-image:url(tankbtn.png);}')
        #self.btn3.setStyleSheet('#btn3{border-image:url(timg.jpg);bord}')


    #几条画线的函数
    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()

    def drawLines(self, qp):
        pen = QtGui.QPen(QtGui.QColor('#00aeff'), 1, Qt.SolidLine)

        qp.setPen(pen)
        #2个数字是一对坐标
        qp.drawLine(105,0 ,110 , 10)
        qp.drawLine(255,0 ,250 , 10)
        qp.drawLine(110,10 ,250 , 10)

        qp.drawLine(30,308+self.increment ,120 , 308+self.increment)
        qp.drawLine(230,308+self.increment ,330 , 308+self.increment)


    #重写三个方法使我们的Tank2018窗口支持拖动,上面参数window就是拖动对象
    def mousePressEvent(self, event):
        if event.button()==Qt.LeftButton:
            self.m_drag=True
            self.m_DragPosition=event.globalPos()-self.pos()
            event.accept()
            self.setCursor(QtGui.QCursor(Qt.OpenHandCursor))
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_drag:
            self.move(QMouseEvent.globalPos()-self.m_DragPosition)
            QMouseEvent.accept()
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag=False
        self.setCursor(QtGui.QCursor(Qt.ArrowCursor))

    



    def erorr_gui(self,flag):
        self.setGeometry(400, 150, 360, 550)
        self.increment=40
        self.label1.setGeometry(QRect(35, 164+self.increment, 50, 20))
        self.linet1.setGeometry(QRect(30, 187+self.increment, 300, 30))
        self.label2.setGeometry(QRect(35, 222+self.increment, 50, 20))
        self.linet2.setGeometry(QRect(30, 245+self.increment, 300, 30))
        self.btn3.setGeometry(QRect(30, 305+self.increment, 300, 35))
        self.label3.setGeometry(QRect(30, 360+self.increment, 300, 20))
        self.btn4.setGeometry(QRect(30, 410+self.increment, 300, 20))
        self.btn5.setGeometry(QRect(30, 440+self.increment, 300, 20))

        self.style = """ 
                QPushButton{background-color:#00aeff;color:white;} 
                #tank2018{ background:#202734; }
                #linet{background-color:#11151b;color:#474b53; border: 1px solid #00aeff;border-radius:3px}
                #btn1{ background-color:#202734;color:#474b53; border:0px;font:900 25px "Microsoft YaHei";}
                #btn2{ background-color:#202734;color:#474b53; border:0px;font:900 17px "Microsoft YaHei";}
                #btn4{background-color:#202734;color:#00aeff; border:0px;font:15px "Microsoft YaHei";}
                #label1{color:#474b53;font:13px "Microsoft YaHei";}
                #label4{background-color:#270a0c;color:red;font:15px  "Microsoft YaHei";padding-left:30px}
               """
        self.setStyleSheet(self.style)
        self.label4.setText('erorr')




  


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = Tank2018_2()
   #ex.login_gui()
   ex.show()
   sys.exit(app.exec_())