# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'second.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(762, 495)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3.addWidget(self.frame)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.frame_3)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout_4.addWidget(self.calendarWidget)
        self.hallButton9 = QtWidgets.QPushButton(self.frame_3)
        self.hallButton9.setObjectName("hallButton9")
        self.verticalLayout_4.addWidget(self.hallButton9)
        self.hallButton8 = QtWidgets.QPushButton(self.frame_3)
        self.hallButton8.setObjectName("hallButton8")
        self.verticalLayout_4.addWidget(self.hallButton8)
        self.hallButton7 = QtWidgets.QPushButton(self.frame_3)
        self.hallButton7.setObjectName("hallButton7")
        self.verticalLayout_4.addWidget(self.hallButton7)
        self.hallButton6 = QtWidgets.QPushButton(self.frame_3)
        self.hallButton6.setObjectName("hallButton6")
        self.verticalLayout_4.addWidget(self.hallButton6)
        self.hallButton5 = QtWidgets.QPushButton(self.frame_3)
        self.hallButton5.setObjectName("hallButton5")
        self.verticalLayout_4.addWidget(self.hallButton5)
        self.hallButton4 = QtWidgets.QPushButton(self.frame_3)
        self.hallButton4.setObjectName("hallButton4")
        self.verticalLayout_4.addWidget(self.hallButton4)
        self.hallButton3 = QtWidgets.QPushButton(self.frame_3)
        self.hallButton3.setObjectName("hallButton3")
        self.verticalLayout_4.addWidget(self.hallButton3)
        self.hallButton2 = QtWidgets.QPushButton(self.frame_3)
        self.hallButton2.setObjectName("hallButton2")
        self.verticalLayout_4.addWidget(self.hallButton2)
        self.hallButton1 = QtWidgets.QPushButton(self.frame_3)
        self.hallButton1.setObjectName("hallButton1")
        self.verticalLayout_4.addWidget(self.hallButton1)
        self.horizontalLayout_2.addWidget(self.frame_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "TextLabel"))
        self.pushButton_3.setText(_translate("Form", "PushButton"))
        self.label_2.setText(_translate("Form", "TextLabel"))
        self.pushButton.setText(_translate("Form", "PushButton"))
        self.label_3.setText(_translate("Form", "TextLabel"))
        self.pushButton_2.setText(_translate("Form", "PushButton"))
        self.label_4.setText(_translate("Form", "TextLabel"))
        self.pushButton_5.setText(_translate("Form", "PushButton"))
        self.label_5.setText(_translate("Form", "TextLabel"))
        self.pushButton_4.setText(_translate("Form", "PushButton"))
        self.label_6.setText(_translate("Form", "TextLabel"))
        self.pushButton_6.setText(_translate("Form", "PushButton"))
        self.label_7.setText(_translate("Form", "TextLabel"))
        self.hallButton9.setText(_translate("Form", "PushButton"))
        self.hallButton8.setText(_translate("Form", "PushButton"))
        self.hallButton7.setText(_translate("Form", "PushButton"))
        self.hallButton6.setText(_translate("Form", "PushButton"))
        self.hallButton5.setText(_translate("Form", "PushButton"))
        self.hallButton4.setText(_translate("Form", "PushButton"))
        self.hallButton3.setText(_translate("Form", "PushButton"))
        self.hallButton2.setText(_translate("Form", "PushButton"))
        self.hallButton1.setText(_translate("Form", "PushButton"))

