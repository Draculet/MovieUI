# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'order.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form5(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(662, 549)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(120, 180, 461, 301))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        #self.tableWidget.setVerticalHeaderItem(0, item)
        #item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        '''item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 5, item)
        '''
        self.orderTitle = QtWidgets.QLabel(Form)
        self.orderTitle.setGeometry(QtCore.QRect(220, 20, 271, 81))
        self.orderTitle.setObjectName("orderTitle")
        self.back = QtWidgets.QPushButton(Form)
        self.back.setGeometry(QtCore.QRect(490, 90, 99, 27))
        self.back.setObjectName("back")
        self.delButt = QtWidgets.QPushButton(Form)
        self.delButt.setGeometry(QtCore.QRect(550, 50, 99, 27))
        self.delButt.setObjectName("delButt")
        self.delSpin = QtWidgets.QSpinBox(Form)
        self.delSpin.setGeometry(QtCore.QRect(490, 50, 48, 27))
        self.delSpin.setObjectName("delSpin")
        self.delLabel = QtWidgets.QLabel(Form)
        self.delLabel.setGeometry(QtCore.QRect(490, 10, 161, 41))
        self.delLabel.setObjectName("delLabel")
        self.fleshButt = QtWidgets.QPushButton(Form)
        self.fleshButt.setGeometry(QtCore.QRect(30, 90, 99, 27))
        self.fleshButt.setObjectName("fleshButt")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        #item = self.tableWidget.verticalHeaderItem(0)
        #item.setText(_translate("Form", "订单1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "用户id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "电影名"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "电影厅"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "时间"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "座位行"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "座位列"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "价格"))
        '''__sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("Form", "1"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("Form", "DeadPool"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("Form", "1"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("Form", "1"))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("Form", "1"))
        item = self.tableWidget.item(0, 5)
        item.setText(_translate("Form", "40"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)'''
        self.orderTitle.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:36pt; font-weight:600;\">用户订单</span></p></body></html>"))
        self.back.setText(_translate("Form", "返回"))
        self.delButt.setText(_translate("Form", "退票"))
        self.delLabel.setText(_translate("Form", "请输入要退的票号"))
        self.fleshButt.setText(_translate("Form", "刷新"))

