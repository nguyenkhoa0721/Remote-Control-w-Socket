# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_process.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialog_process(object):
    def setupUi(self, Dialog_process):
        Dialog_process.setObjectName("Dialog_process")
        Dialog_process.resize(504, 460)
        self.layoutWidget = QtWidgets.QWidget(Dialog_process)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 481, 441))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_kill = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_kill.setObjectName("btn_kill")
        self.horizontalLayout.addWidget(self.btn_kill)
        self.btn_xem = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_xem.setObjectName("btn_xem")
        self.horizontalLayout.addWidget(self.btn_xem)
        self.btn_xoa = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_xoa.setObjectName("btn_xoa")
        self.horizontalLayout.addWidget(self.btn_xoa)
        self.btn_start = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_start.setObjectName("btn_start")
        self.horizontalLayout.addWidget(self.btn_start)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.layoutWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 1)

        self.retranslateUi(Dialog_process)
        QtCore.QMetaObject.connectSlotsByName(Dialog_process)

    def retranslateUi(self, Dialog_process):
        _translate = QtCore.QCoreApplication.translate
        Dialog_process.setWindowTitle(_translate("Dialog_process", "Process"))
        self.btn_kill.setText(_translate("Dialog_process", "Kill"))
        self.btn_xem.setText(_translate("Dialog_process", "Xem"))
        self.btn_xoa.setText(_translate("Dialog_process", "Xóa"))
        self.btn_start.setText(_translate("Dialog_process", "Start"))
