# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form3(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(397, 318)
        self.id = QtWidgets.QLineEdit(Form)
        self.id.setGeometry(QtCore.QRect(120, 130, 161, 27))
        self.id.setText("")
        self.id.setObjectName("id")
        self.passw = QtWidgets.QLineEdit(Form)
        self.passw.setGeometry(QtCore.QRect(120, 180, 161, 27))
        self.passw.setObjectName("pass")
        self.Title = QtWidgets.QLabel(Form)
        self.Title.setGeometry(QtCore.QRect(120, 30, 161, 91))
        font = QtGui.QFont()
        font.setFamily("URW Bookman L")
        font.setPointSize(28)
        font.setItalic(True)
        self.Title.setFont(font)
        self.Title.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Title.setObjectName("Title")
        self.idlabel = QtWidgets.QLabel(Form)
        self.idlabel.setGeometry(QtCore.QRect(50, 130, 67, 17))
        self.idlabel.setObjectName("idlabel")
        self.passlabel = QtWidgets.QLabel(Form)
        self.passlabel.setGeometry(QtCore.QRect(50, 180, 67, 17))
        self.passlabel.setObjectName("passlabel")
        self.login = QtWidgets.QPushButton(Form)
        self.login.setGeometry(QtCore.QRect(220, 240, 99, 27))
        self.login.setObjectName("login")
        self.register = QtWidgets.QPushButton(Form)
        self.register.setGeometry(QtCore.QRect(70, 240, 99, 27))
        self.register.setObjectName("register")
        self.manage = QtWidgets.QPushButton(Form)
        self.manage.setGeometry(QtCore.QRect(10, 10, 99, 27))
        self.manage.setObjectName("manage")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Title.setText(_translate("Form", "经典影院"))
        self.idlabel.setText(_translate("Form", "用户名"))
        self.passlabel.setText(_translate("Form", "密码"))
        self.login.setText(_translate("Form", "登录"))
        self.register.setText(_translate("Form", "注册"))
        self.manage.setText(_translate("Form", "切换管理员"))


