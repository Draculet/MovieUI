import time
import pymysql
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from forth2 import Ui_Form
from third2 import Ui_Form2
from login import Ui_Form3
from man import Ui_Form4
from order import Ui_Form5
import socket
import threading
import sys
import struct
import binascii


choice = '1'
tcp_socket = None
c_id = None
mvname = None

class login(QWidget, Ui_Form3):
    def __init__(self):
        super(login, self).__init__()
        self.setupUi(self)
        try:
            self.db = pymysql.connect("localhost","root","335369376","Movie")
        except:
            print("Error db")
        self.cursor = self.db.cursor()
        self.login.clicked.connect(self.loginLogic)
        self.register.clicked.connect(self.registerUI)
        self.passw.setEchoMode(2)
        self.manage.clicked.connect(self.changemanWin)
        
    def registerUI(self):
        self.login.hide()
        self.idlabel.setText("注册帐号")
        self.passlabel.setText("注册密码")
        self.register.setText("确定")
        self.register.clicked.connect(self.registerLogic)
        #self.register.clicked.connect(self.changeWin)
        
        
    def loginLogic(self):
        idstr = self.id.text();
        pastr = self.passw.text();
        sql = 'select * from Table_Customer where C_User=\'' + self.id.text() + '\'';
        self.cursor.execute(sql)
        data = self.cursor.fetchone()
        print(sql)
        if data == None:
            QMessageBox.question(self, 'Message', '用户不存在', QMessageBox.Yes)
            self.id.setText("")
            self.passw.setText("")
        else:
            print(data)
            if data[2] == self.passw.text():
                self.changefirWin()
                global c_id
                c_id = data[0]
            else:
                QMessageBox.question(self, 'Message', '密码错误', QMessageBox.Yes)
            
        #print("%s" %idstr)
        #print("%s" %pastr)
        
    def registerLogic(self):
        sql = 'insert into Table_Customer(C_User, C_Pass) values(\'' + self.id.text()+ '\',\'' + self.passw.text() + "\')";
        print(sql)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            print(e)
        global c_id
        sql = 'select C_ID from Table_Customer where C_User=\'' + self.id.text() + '\'';
        self.cursor.execute(sql)
        data = self.cursor.fetchone()
        #print(data)
        if data != None:
            print(data[0])
            c_id = data[0]
        self.changefirWin()
        
    def changefirWin(self):
        self.hide()
        self.w=firWin()
        self.w.show()
        
    def changemanWin(self):
        self.hide()
        self.w = manWin()
        self.w.show()
    #def 
        
       
class manWin(QWidget, Ui_Form4):
    def __init__(self):
        self.link = False
        super(manWin, self).__init__()
        self.setupUi(self)
        try:
            self.db = pymysql.connect("localhost","root","335369376","Movie")
        except:
            print("Error db")
        self.newmvFrame.hide()
        self.hallFrame.hide()
        self.cursor = self.db.cursor()
        self.pushButton.clicked.connect(self.hallFrame.hide)
        self.pushButton.clicked.connect(self.newmvFrame.show)
        self.pushButton_3.clicked.connect(self.newmvFrame.hide)
        self.pushButton_3.clicked.connect(self.hallFrame.show)
        self.commit.clicked.connect(self.insertMov)
        
    def insertMov(self):
        mvn = self.mvnameLine.text()
        mvh = self.mvhallLine.text()
        price = self.mvpriceLine.text()
        y = self.yearSpin.text()
        m = self.monSpin.text()
        d = self.daySpin.text()
        clock = self.timeLine.text()
        msg = "ADD " + mvn + ',' + mvh + ',' + price + ',' + y + '-' + m + '-' + d + " " + clock;
        print(msg)
        self.tcp_client_start()
        self.tcp_send(msg)
        QMessageBox.question(self, 'Message', '操作成功', QMessageBox.Yes)
        
    def closeEvent(self, e):
        #self.hide()
        self.w=login()
        self.w.show()
        e.accept()
        
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
                print("Send: %s" %send_msg)
                print("Already Send\n")
            #except Exception as ret:
                #print('发送失败\n')
                           
class firWin(QWidget,Ui_Form): 
    def __init__(self):
        super(firWin,self).__init__()
        self.setupUi(self)
        #self.pushButton.clicked.connect(self.changepix)
        #self.pushButton_2.clicked.connect(self.changecab)
        #self.pushButton_3.clicked.connect(self.changeWin)
        self.client_th = None
        self.link = True
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
        global tcp_socket
        #if tcp_socket == None:
        self.tcp_client_start()
        self.recvSetPicAndTxt();
        #mvname = input("电影名")
        #mvhid = input("影厅")
        #mvmoney = input("价格")
        #mvdate = input("日期")
        #msg = 'ADD ' + mvname + ',' + mvhid + ',' + mvmoney + ',' + mvdate;
        #print(msg)
        #self.tcp_send(msg)
        #self.toolButton11.clicked.connect(self.changecab)
        #self.toolButton12.clicked.connect(self.changepix)
        
        
        
    def recvSetPicAndTxt(self):
        buttonList = []
        buttonList.append(self.ButtonName1)
        buttonList.append(self.ButtonName2)
        buttonList.append(self.ButtonName3)
        buttonList.append(self.ButtonName4)
        buttonList.append(self.ButtonName5)
        buttonList.append(self.ButtonName6)
        buttonList.append(self.ButtonName7)
        buttonList.append(self.ButtonName8)
        buttonList.append(self.ButtonName9)
        labelList = []
        labelList.append(self.label1)
        labelList.append(self.label2)
        labelList.append(self.label3)
        labelList.append(self.label4)
        labelList.append(self.label5)
        labelList.append(self.label6)
        labelList.append(self.label7)
        labelList.append(self.label8)
        labelList.append(self.label9)
        toolList1 = []
        toolList1.append(self.toolButton11);
        toolList1.append(self.toolButton21);
        toolList1.append(self.toolButton31);
        toolList1.append(self.toolButton41);
        toolList1.append(self.toolButton51);
        toolList1.append(self.toolButton61);
        toolList1.append(self.toolButton71);
        toolList1.append(self.toolButton81);
        toolList1.append(self.toolButton91);
        toolList2 = []
        toolList2.append(self.toolButton12);
        toolList2.append(self.toolButton22);
        toolList2.append(self.toolButton32);
        toolList2.append(self.toolButton42);
        toolList2.append(self.toolButton52);
        toolList2.append(self.toolButton62);
        toolList2.append(self.toolButton72);
        toolList2.append(self.toolButton82);
        toolList2.append(self.toolButton92);
        
        current = 0;
        msg = 'GMI'
        self.tcp_send(msg)
        while True:
            num = tcp_socket.recv(4, socket.MSG_WAITALL)
            n = struct.unpack("!i", num)
            print('recv INT number %d ' %n[0])
            if n[0] == 1:
                str = tcp_socket.recv(n[0], socket.MSG_WAITALL)
                str = str.decode('utf-8')
                print(str)
                if str == 'E':
                    break
            info = tcp_socket.recv(n[0], socket.MSG_WAITALL)
            info = info.decode('utf-8')
            print(info)
            minfo = info.split('-')
            mid = minfo[0]
            mname = minfo[1]
            buttonList[current].setText(mname)
            picpath = mid + ".jpg"
            txtpath = mid + '.txt'
            fdp = open(picpath, "wb")
            fdt = open(txtpath, "wb")
      	
      	
            num = tcp_socket.recv(4, socket.MSG_WAITALL)
            n = struct.unpack("!i", num)
            print('recv INT number %d ' %n[0], socket.MSG_WAITALL)
            picmsg = tcp_socket.recv(n[0], socket.MSG_WAITALL)
            fdp.write(picmsg)
            fdp.close()
            pixmap = QPixmap(picpath).scaled(170, 200)
            labelList[current].setScaledContents(True)
            labelList[current].setPixmap(pixmap)
            
            num = tcp_socket.recv(4, socket.MSG_WAITALL)
            n = struct.unpack("!i", num)
            print('recv INT number %d ' %n[0], socket.MSG_WAITALL)
            txtmsg = tcp_socket.recv(n[0], socket.MSG_WAITALL)
            fdt.write(txtmsg)
            fdt.close()
            file = open(txtpath, encoding="gbk")
            txtmsg = ''
            while True:
            	line = file.readline()
            	txtmsg+=line
            #str+='\n'
            	if not line: 
                	break
            toolList2[current].setText("介绍")
            toolList1[current].setText("购票")
            self.showPicAndTxtOuterFunc(toolList2,toolList1, current, pixmap, txtmsg, mname)
            
            #toolList1[current].clicked.connect()
            
            current+=1
        
    def showPicAndTxtOuterFunc(self, toolList2,toolList1, current, pixmap, txtmsg, mname):
        toolList2[current].clicked.connect(lambda:self.showPicAndTxt(pixmap, txtmsg))
        toolList1[current].clicked.connect(lambda:self.changecab(mname))
       #self.Introduce.setText(txtmsg)
    def showPicAndTxt(self, pixmap, txtmsg):
        self.Picture.setPixmap(pixmap)
        self.Introduce.setText(txtmsg)
    
    '''def changepix(self):
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
    '''
    '''    
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
        
        self.recvSetPicAndTxt()
        
        
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
    '''
    def changecab(self, mname):
        '''self.Introduce.setWordWrap(True)
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
        self.recvSetPicAndTxt()
        '''
        
        
        #msg = 'GST Dead Pool'
        #msg = 'GST Die and Live'
        self.name = mname;
        global mvname
        mvname = mname;
        msg = 'GST ' + mname;
        print("Send msg %s" %msg);
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
        
    
    def showTime(self, date):
        self.CalFrame.hide()
        self.timeFrame.show()
        #while True:
        if date in self.darr:
            print("over")
       #         break
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
        else:
            QMessageBox.question(self, 'Message', '该日期无排片,请重新选择', QMessageBox.Yes)
        
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
                print("Send: %s" %send_msg)
                print("Already Send\n")
            #except Exception as ret:
                #print('发送失败\n')
           
    def changeWin(self, i, time):
        global choice
        print("Choice is %s" %i)
        choice = i + ',' + time
        msg = 'GSC ' + choice + ',0,0'
        self.tcp_send(msg)
        
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
        num = tcp_socket.recv(4, socket.MSG_WAITALL)
        n = struct.unpack("!i", num)
        print('recv INT number %d ' %n[0])
        col = n[0];
        tcp_socket.recv(n[0], socket.MSG_WAITALL)
        num = tcp_socket.recv(4, socket.MSG_WAITALL)
        n = struct.unpack("!i", num)
        print('recv INT number %d ' %n[0])
        total = n[0];
        recv_msg = tcp_socket.recv(n[0], socket.MSG_WAITALL)
        if recv_msg:
            seat_info = recv_msg.decode('utf-8')
        print("%s" %seat_info)
        
        for i in range (1, 121):
            but = self.buttonGroup.button(i)
            but.setEnabled(False)
        seatpos = 1
        #table是20的倍数,用来定位选座表位置
        table = 0
        j = 0
        while True:
            if total / col > 6:
                QMessageBox.question(self, 'Message', '座位已售罄', QMessageBox.Yes)
                break;
            for i in range (1, col + 1):
                pos = i + table * 20
                if seat_info[seatpos] == '0':
                    #print("%d" %pos)
                    but = self.buttonGroup.button(pos)
                    but.setEnabled(True)
                seatpos+=1
            table += 1
            if seatpos == len(seat_info):
                break
        
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
                mvinfo = m.split(',')
                try:
                    self.db = pymysql.connect("localhost","root","335369376","Movie")
                except:
                    print("Error db")
                self.cursor = self.db.cursor()
                global c_id
                print(c_id)
                global mvname
                print(mvname)
                mvinfo[0] = mvinfo[0].split()[1]
                sql = 'insert into Table_Order values(' + str(c_id) + ',\'' + mvname + '\',' + mvinfo[0] + ',\'' + mvinfo[1] + '\',' + mvinfo[2] + ',' + mvinfo[3] + ',' + '45)'
                print(sql)
                try:
                    self.cursor.execute(sql)
                    self.db.commit()
                except Exception as e:
                    self.db.rollback()
                    print(e)
                    
            if msg[0] == 'f':
                QMessageBox.question(self, 'Message', '  购买失败', QMessageBox.Yes)
        #self.close()
        self.hide()
        self.w=orderWin()
        self.w.show()
    
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
        self.total += 45
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
        print("Send: %s" %send_msg)
        print("Already Send\n")
        
class orderWin(QWidget, Ui_Form5):
    def __init__(self):
        super(orderWin ,self).__init__()
        self.setupUi(self)
        try:
            self.db = pymysql.connect("localhost","root","335369376","Movie")
        except:
            print("Error db")
        global c_id
        self.cursor = self.db.cursor()
        sql = 'select * from Table_Order where C_ID = ' + str(c_id)
        print(sql)
        try:
            self.cursor.execute(sql)
            #self.db.commit()
        except Exception as e:
            self.db.rollback()
            print(e)
        len = self.cursor.rowcount;
        print(len)
        self.delSpin.setMinimum(1)
        self.delSpin.setMaximum(len)
        self.tableWidget.setRowCount(len);
        for i in range(0, len):
            for j in range(0, 7):
                item = QTableWidgetItem()
                self.tableWidget.setItem(i, j, item)
        #item = self.tableWidget.item(10, 10)
        #item.setText("hello")
        for i in range(0, len):
            res = self.cursor.fetchone()
            for j in range(0, 7):
                item = self.tableWidget.item(i, j)
                item.setText(str(res[j]))
        self.delButt.clicked.connect(self.delrow)
        self.back.clicked.connect(self.toFirWin)
        
    def delrow(self):
        row = int(self.delSpin.text())
        for j in range(0, 7):
            item = self.tableWidget.item(row - 1, j)
            item.setText('')
            
    def toFirWin(self):
        self.hide()
        self.w=firWin()
        self.w.show()
        
        
if __name__=="__main__":
    app=QApplication(sys.argv)
    #myshow=firWin()
    myshow = login()
    #myshow = orderWin()
    myshow.show()
    sys.exit(app.exec_())
