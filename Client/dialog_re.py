# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_re.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialog_re(object):
    def setupUi(self, dialog_re):
        dialog_re.setObjectName("dialog_re")
        dialog_re.resize(452, 503)
        self.groupBox = QtWidgets.QGroupBox(dialog_re)
        self.groupBox.setGeometry(QtCore.QRect(10, 170, 424, 321))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.key_value = QtWidgets.QLineEdit(self.widget)
        self.key_value.setObjectName("key_value")
        self.horizontalLayout_3.addWidget(self.key_value)
        self.value = QtWidgets.QLineEdit(self.widget)
        self.value.setObjectName("value")
        self.horizontalLayout_3.addWidget(self.value)
        self.comboBox_2 = QtWidgets.QComboBox(self.widget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_2)
        self.verticalLayout.addWidget(self.widget)
        self.noti = QtWidgets.QPlainTextEdit(self.groupBox)
        self.noti.setEnabled(False)
        self.noti.setObjectName("noti")
        self.verticalLayout.addWidget(self.noti)
        self.widget_2 = QtWidgets.QWidget(self.groupBox)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_send1 = QtWidgets.QPushButton(self.widget_2)
        self.btn_send1.setObjectName("btn_send1")
        self.horizontalLayout_4.addWidget(self.btn_send1)
        self.btn_xoa = QtWidgets.QPushButton(self.widget_2)
        self.btn_xoa.setObjectName("btn_xoa")
        self.horizontalLayout_4.addWidget(self.btn_xoa)
        self.verticalLayout.addWidget(self.widget_2)
        self.layoutWidget = QtWidgets.QWidget(dialog_re)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 431, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.btn_browser = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_browser.setObjectName("btn_browser")
        self.horizontalLayout.addWidget(self.btn_browser)
        self.layoutWidget1 = QtWidgets.QWidget(dialog_re)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 60, 431, 101))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.layoutWidget1)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.horizontalLayout_2.addWidget(self.plainTextEdit)
        self.btn_send = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_send.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_send.sizePolicy().hasHeightForWidth())
        self.btn_send.setSizePolicy(sizePolicy)
        self.btn_send.setMaximumSize(QtCore.QSize(16777215, 26))
        self.btn_send.setObjectName("btn_send")
        self.horizontalLayout_2.addWidget(self.btn_send)

        self.retranslateUi(dialog_re)
        QtCore.QMetaObject.connectSlotsByName(dialog_re)

    def retranslateUi(self, dialog_re):
        _translate = QtCore.QCoreApplication.translate
        dialog_re.setWindowTitle(_translate("dialog_re", "Register"))
        self.groupBox.setTitle(_translate("dialog_re", "Sửa giá trị trực tiếp"))
        self.comboBox.setItemText(0, _translate("dialog_re", "Get value"))
        self.comboBox.setItemText(1, _translate("dialog_re", "Set value"))
        self.comboBox.setItemText(2, _translate("dialog_re", "Delete value"))
        self.comboBox.setItemText(3, _translate("dialog_re", "Create key"))
        self.comboBox.setItemText(4, _translate("dialog_re", "Delete key"))
        self.lineEdit_2.setPlaceholderText(_translate("dialog_re", "Đường dẫn"))
        self.key_value.setPlaceholderText(_translate("dialog_re", "Name Value"))
        self.value.setPlaceholderText(_translate("dialog_re", "Value"))
        self.comboBox_2.setItemText(0, _translate("dialog_re", "String"))
        self.comboBox_2.setItemText(1, _translate("dialog_re", "Binary"))
        self.comboBox_2.setItemText(2, _translate("dialog_re", "DWORD"))
        self.comboBox_2.setItemText(3, _translate("dialog_re", "QWORD"))
        self.comboBox_2.setItemText(4, _translate("dialog_re", "Muti-String"))
        self.comboBox_2.setItemText(5, _translate("dialog_re", "Expandable String"))
        self.btn_send1.setText(_translate("dialog_re", "Gửi"))
        self.btn_xoa.setText(_translate("dialog_re", "Xóa"))
        self.btn_browser.setText(_translate("dialog_re", "Browser"))
        self.btn_send.setText(_translate("dialog_re", "Gửi nội dung"))
