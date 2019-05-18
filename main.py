import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from forth2 import Ui_Form
from third2 import Ui_Form2
import socket
import threading
import sys
import struct
import binascii

choice = '1'
tcp_socket = None

class firWin(QWidget,Ui_Form): 
    def __init__(self):
        super(firWin,self).__init__()
        self.setupUi(self)
        #self.pushButton.clicked.connect(self.changepix)
        #self.pushButton_2.clicked.connect(self.changecab)
        #self.pushButton_3.clicked.connect(self.changeWin)
        self.client_th = None
        self.link = False
        self.CalFrame.hide()
        self.hallChoiceFrame.hide()
        self.timeFrame.hide()
        pixmap = QPixmap('02.jpg').scaled(170, 200)
        self.label1.setScaledContents(True);
        self.label1.setPixmap(pixmap)
        pixmap = QPixmap('03.jpg').scaled(170, 200)
        self.label2.setScaledContents(True);
        self.label2.setPixmap(pixmap)
        pixmap = QPixmap('01.jpg').scaled(170, 200)
        self.label3.setScaledContents(True);
        self.label3.setPixmap(pixmap)
        pixmap = QPixmap('02.jpg').scaled(170, 200)
        self.label4.setScaledContents(True);
        self.label4.setPixmap(pixmap)
        pixmap = QPixmap('03.jpg').scaled(170, 200)
        self.label5.setScaledContents(True);
        self.label5.setPixmap(pixmap)
        pixmap = QPixmap('01.jpg').scaled(170, 200)
        self.label6.setScaledContents(True);
        self.label6.setPixmap(pixmap)
        pixmap = QPixmap('02.jpg').scaled(170, 200)
        self.label7.setScaledContents(True);
        self.label7.setPixmap(pixmap)
        pixmap = QPixmap('03.jpg').scaled(170, 200)
        self.label8.setScaledContents(True);
        self.label8.setPixmap(pixmap)
        pixmap = QPixmap('01.jpg').scaled(170, 200)
        self.label9.setScaledContents(True);
        self.label9.setPixmap(pixmap)
        pixmap = QPixmap('004.jpg').scaled(460, 300)
        self.Picture.setPixmap(pixmap)
        self.Picture.setScaledContents(True);
        self.toolButton11.clicked.connect(self.changecab)
        self.toolButton12.clicked.connect(self.changepix)
        
    def changepix(self):
        self.toolButton12.setEnabled(False)
        self.toolButton11.setEnabled(True)
        self.PictureFrame.show()
        self.CalFrame.hide()
        self.hallChoiceFrame.hide()
        
        pixmap = QPixmap('01.jpg').scaled(460,300)
        self.Picture.setPixmap(pixmap)
        self.Picture.setScaledContents(True)
        self.Introduce.setWordWrap(True)
        
        file = open("text.txt")
        str = ''
        while True: 
            line = file.readline()
            str+=line
            #str+='\n'
            if not line: 
                break
        file.close()
        self.Introduce.setText(str)
        
    def changecab(self):
        self.Introduce.setWordWrap(True)
        file = open("text.txt")
        str = ''
        while True: 
            line = file.readline()
            str+=line
            #str+='\n'
            if not line: 
                break
        file.close()
        self.Introduce.setText(str)
        self.toolButton11.setEnabled(False)
        self.toolButton12.setEnabled(True)
        self.tcp_client_start()
        #msg = 'GST Dead Pool'
        #msg = 'GST Die and Live'
        self.name = 'A gay life style'
        msg = 'GST A gay life style'
        self.tcp_send(msg)
        recv_msg = tcp_socket.recv(1024)
        if recv_msg:
            msg = recv_msg.decode('utf-8')
            print("Recv msg %s\n" %msg)
        self.arr = []
        self.arr = msg.split(',')
        self.darr = []
        self.CalFrame.show()
        self.PictureFrame.hide()
        for s in self.arr:
            s,s2 = s.split()
            y,m,d = s.split('-')
            d = QDate(int(y), int(m), int(d))
            self.darr.append(d)    
        self.calendarWidget.setDateRange(self.darr[0],self.darr[len(self.darr) - 1])
        self.calendarWidget.clicked[QDate].connect(self.showTime)
        #TODO 增加判断是否有演出计划以及时间先后问题
        #TODO 增加演出时间按钮
        
    def showTime(self, date):
        self.CalFrame.hide()
        self.timeFrame.show()
        while True:
            if date in self.darr:
                print("over")
                break
            else:
                QMessageBox.question(self, 'Message', '该日期无排片,请重新选择', QMessageBox.Yes)
                return
        time = []
        datestr = ''
        for s in self.arr:
            s,s2 = s.split()
            y,m,d = s.split('-')
            d = QDate(int(y), int(m), int(d))
            if d == date:
                time.append(s2)
                datestr = s
        for t in time:
            #pushButt = QPushButton()
            #self.gridLayout_5.addWidget(pushButt)
            #pushButt.setText(t)
            #pushButt.show()
            #pushButt.clicked.connect(lambda:self.showHall(datestr + ' ' + t))
            self.getButt(t, datestr)#此处若写成函数则可以一个按钮注册一个事件
                                    #若将函数在此展开，则注册的事件只有for循环的最后一个对象的事件,推测是for循环没有新建无名对象
        
    def getButt(self, t, datestr):
        pushButt = QPushButton()
        self.gridLayout_5.addWidget(pushButt)
        pushButt.setText(t)
        pushButt.show()
        pushButt.clicked.connect(lambda:self.showHall(datestr + ' ' + pushButt.text()))
      
    def showHall(self, time):
        print(time)
        msg = 'GHC '+self.name + ','+ time
        self.tcp_send(msg)
        recv_msg = tcp_socket.recv(1024)
        if recv_msg:
            msg = recv_msg.decode('utf-8')
            print("Recv msg %s\n" %msg)
        hall = []
        hall = msg.split()
        hallarr = []
        hallarr.append(self.hall1)
        hallarr.append(self.hall2)
        hallarr.append(self.hall3)
        hallarr.append(self.hall4)
        hallarr.append(self.hall5)
        hallarr.append(self.hall6)
        hallarr.append(self.hall7)
        hallarr.append(self.hall8)
        hallarr.append(self.hall9)
        for h in hallarr:
            h.setEnabled(False)
        for i in hall:
            hallarr[int(i) - 1].setEnabled(True)
        self.CalFrame.hide()
        self.timeFrame.hide()
        self.hallChoiceFrame.show()
        #str = date.toString() + 'Hall Information'
        for i in hall:
            self.outerFunc(hallarr, i, time)
        
    def outerFunc(self, hallarr, i, time):
        hallarr[int(i) - 1].clicked.connect(lambda:self.changeWin(i, time))#外置函数,必须传出参数才能生效 ??
        
    def tcp_client_start(self):
        global tcp_socket
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        address = ('127.0.0.1', 9981)
        try:
            tcp_socket.connect(address)
        except Exception as ret:
                print('Error In Connect\n')
        else:
            self.link = True
            #self.client_th = threading.Thread(target=self.tcp_client_concurrency, args=(address,))
            #self.client_th.start()
            print('TCPClient Established\n')
        
    #def tcp_client_concurrency(self, address):
    #   while True:
    #        recv_msg = self.tcp_socket.recv(1024)
    #        if recv_msg:
    #            msg = recv_msg.decode('utf-8')
    #            print("Recv msg %s\n" %msg)
            #else:
             #   self.tcp_socket.close()
              #  print("Close Socket\n")
               # break

    def tcp_send(self, send_msg):
        """
        功能函数，用于TCP服务端和TCP客户端发送消息
        :return: None
        """
        if self.link is False:
            print("Link Unlinked\n")
        else:
            #try:
                l = len(send_msg)
                msg = struct.pack('!i', l)
                send_msg = send_msg.encode('ascii')
                tcp_socket.send(msg);
                tcp_socket.send(send_msg)
                print("Already Send\n")
            #except Exception as ret:
                #print('发送失败\n')
           
    def changeWin(self, i, time):
        global choice
        print("Choice is %s" %i)
        choice = i + ',' + time
        
        self.hide()
        self.w=secWin()
        self.w.show()
                
class secWin(QWidget,Ui_Form2):
    def __init__(self):
        self.total = 0;
        print(choice)
        super(secWin,self).__init__()
        self.setupUi(self)
        self.ticArr = []
        self.buttonGroup.buttonClicked.connect(self.buttonGroClick)
        self.commitButton.clicked.connect(self.commitClick)
        
    def commitClick(self):
        for m in self.ticArr:
            self.tcp_send(m)
            recv_msg = tcp_socket.recv(1024)
            if recv_msg:
                msg = recv_msg.decode('utf-8')
                print("Recv msg %s\n" %msg)
            if msg[0] == 's':
                QMessageBox.question(self, 'Message', '  购买成功', QMessageBox.Yes)
            if msg[0] == 'f':
                QMessageBox.question(self, 'Message', '  购买失败', QMessageBox.Yes)
        self.close()
    
    def closeEvent(self, e):
        #self.hide()
        self.w=firWin()
        self.w.show()
        e.accept()
    
    def buttonGroClick(self):
        id = self.buttonGroup.checkedId()
        row = int(id / 20) + 1
        if id % 20 == 0:
            row = row - 1
        row = str(row)
        col = id % 20
        if id % 20 == 0:
            col=20
        col = str(col)
        msg = 'GSC ' + choice + ',' + row + ',' + col
        self.ticArr.append(msg)
        #TODO查询价格
        self.total += 20
        self.totalLabel.setText('Total: ' + str(self.total))
        
        
        but = self.buttonGroup.button(id)
        but.setEnabled(False)
        print("%d has been clicked" %id)
        self.pushButt = QPushButton()
        pushButt = self.pushButt
        self.pushButt.clicked.connect(lambda:self.buttClick(pushButt, but))#不能传入self.pushButt(地址),需要复制后传入
        self.verticalLayout_2.addWidget(self.pushButt)
        s = '第'+row+'行,第'+col+'列'
        self.pushButt.setText(s)
        self.pushButt.show()
        
    def buttClick(self, pushButt, but):
        pushButt.hide()
        but.setEnabled(True)
        
    def tcp_send(self, send_msg):
        """
        功能函数，用于TCP服务端和TCP客户端发送消息
        :return: None
        """
        #if self.link is False:
        #    print("Link Unlinked\n")
        #else:
            #try:
        l = len(send_msg)
        msg = struct.pack('!i', l)
        send_msg = send_msg.encode('ascii')
        tcp_socket.send(msg);
        tcp_socket.send(send_msg)
        print("Already Send\n")
        
if __name__=="__main__":
    app=QApplication(sys.argv)
    myshow=firWin()
    myshow.show()
    sys.exit(app.exec_())
