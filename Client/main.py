import sys

from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox, QFileDialog
)
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from dialog_main import Ui_dialog_main
from dialog_capture import Ui_dialog_capture
from dialog_app import Ui_dialog_app
from dialog_keystroke import Ui_dialog_keystroke
from dialog_kill import Ui_dialog_kill
from dialog_process import Ui_dialog_process
from dialog_re import Ui_dialog_re
from dialog_start import Ui_dialog_start
import json
import socket
from PIL import Image
class Window(QDialog, Ui_dialog_main):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.trigger()
        self.lineEdit.setText('192.168.165.128:8080')

        self.btn_cap.setEnabled(False)
        self.btn_app.setEnabled(False)
        self.btn_key.setEnabled(False)
        self.btn_process.setEnabled(False)
        self.btn_re.setEnabled(False)
        self.btn_shutdown.setEnabled(False)
    def _ping(self):
        try:
            s.sendall(b'ping')
            return True
        except:
            self.label.setText("No Connection")
            self.btn_cap.setEnabled(False)
            self.btn_app.setEnabled(False)
            self.btn_key.setEnabled(False)
            self.btn_process.setEnabled(False)
            self.btn_re.setEnabled(False)
            self.btn_shutdown.setEnabled(False)
        return False
    def trigger(self):
        self.btn_cap.clicked.connect(self.capture)
        self.btn_process.clicked.connect(self.process)
        self.btn_app.clicked.connect(self.app)
        self.btn_re.clicked.connect(self.re)
        self.btn_key.clicked.connect(self.key)
        self.btn_connect.clicked.connect(self.connect)
        self.btn_shutdown.clicked.connect(self.shutdown)
        self.btn_exit.clicked.connect(self.exit)
    def connect(self):
        global s
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tmp = self.lineEdit.text().split(':')
        HOST = tmp[0]
        PORT = int(tmp[1])
        server_address = (HOST, PORT)
        print('connecting to %s port ' + str(server_address))
        try:
            s.connect(server_address)
            self.label.setText('Connect: '+self.lineEdit.text())
            QMessageBox.about(self, "Thông báo", "Connect thành công")
            self.btn_cap.setEnabled(True)
            self.btn_app.setEnabled(True)
            self.btn_key.setEnabled(True)
            self.btn_process.setEnabled(True)
            self.btn_re.setEnabled(True)
            self.btn_shutdown.setEnabled(True)
        except Exception as e:
            print(e)
            self.label.setText('No connection')
            QMessageBox.about(self, "Thông báo", "Connect không thành công")
    def capture(self):
        if (self._ping()==False):
            QMessageBox.about(self, "Thông báo", "Connect không thành công")
            return
        dialog = Dialog_capture(self)
        dialog.exec()
    def app(self):
        if (self._ping()==False):
            QMessageBox.about(self, "Thông báo", "Connect không thành công")
            return
        dialog = Dialog_app(self)
        dialog.exec()
    def key(self):
        if (self._ping()==False):
            QMessageBox.about(self, "Thông báo", "Connect không thành công")
            return
        dialog = Dialog_keystroke(self)
        dialog.exec()
    def process(self):
        if (self._ping()==False):
            QMessageBox.about(self, "Thông báo", "Connect không thành công")
            return
        dialog = Dialog_process(self)
        dialog.exec()
    def re(self):
        if (self._ping()==False):
            QMessageBox.about(self, "Thông báo", "Connect không thành công")
            return
        dialog = Dialog_re(self)
        dialog.exec()
    def shutdown(self):
        if (self._ping()==False):
            QMessageBox.about(self, "Thông báo", "Connect không thành công")
            return
        sendMsg('shutdown')
    def exit(self):
        try: 
            s.sendall(bytes('quit', "utf8"))
            s.close()
        except:
            s.close()
        exit()
class Dialog_capture(QDialog, Ui_dialog_capture):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.capture)
        self.pushButton_3.clicked.connect(self.save)
    
    def capture(self):
        s.sendall(bytes('capture', "utf8"))

        f=open('capture.png','wb')
        l=s.recv(4096)
        while (True):
            if (l==b'ok'):
                break
            f.write(l)
            l=s.recv(4096)
        print("done")
        f.close()
        
        pix = QPixmap('capture.png')
        item = QtWidgets.QGraphicsPixmapItem(pix)
        scene = QtWidgets.QGraphicsScene(self)
        scene.addItem(item)
        self.graphicsView.setScene(scene)
        self.graphicsView.fitInView(scene.sceneRect(), QtCore.Qt.KeepAspectRatio)
       
    def save(self):
        path = QFileDialog.getSaveFileName(self, 'Save File','capture.png')
        file1 = open("capture.png", "rb")
        file2 = open(str(path[0]), "wb")
        l = file1.readline()
        while l:
            file2.write(l)
            l = file1.read()
        file1.close()
        file2.close()

class Dialog_process(QDialog, Ui_dialog_process):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connect()

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(['name','PID','TC'])
    def connect(self):
        self.btn_xem.clicked.connect(self.xem)
        self.btn_xoa.clicked.connect(self.xoa)
        self.btn_kill.clicked.connect(self.kill)
        self.btn_start.clicked.connect(self.start)

    def xem(self):
        data = json.loads(sendMsg('process//list'))
        data=data['process']
        rows = len(data)
        cols = len(data[0])
        keys = ['name','PID','TC']
        self.tableWidget.setRowCount(rows)
        for row in range(rows):
            for col in range(cols):
                item = QtWidgets.QTableWidgetItem()
                item.setText(data[row][keys[col]] or '') # or '' for any None values
                self.tableWidget.setItem(row, col, item)
        self.tableWidget.show()
    def xoa(self):
        self.tableWidget.setRowCount(0)
    def kill(self):
        dialog = Dialog_kill('process', self)
        dialog.exec()
    def start(self):
        dialog = Dialog_start('process', self)
        dialog.exec()  

class Dialog_app(QDialog, Ui_dialog_app):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connect()
    def connect(self):
        self.btn_kill.clicked.connect(self.kill)
        self.btn_start.clicked.connect(self.start)
        self.btn_xem.clicked.connect(self.xem)
        self.btn_xoa.clicked.connect(self.xoa)
    def xem(self):
        data = json.loads(sendMsg('app//list'))
        data=data['app']
        rows = len(data)
        cols = len(data[0])
        keys = ['name','ID','TC']
        self.tableWidget.setRowCount(rows)
        self.tableWidget.setColumnCount(cols)
        for row in range(rows):
            for col in range(cols):
                item = QtWidgets.QTableWidgetItem()
                item.setText(data[row][keys[col]] or '') # or '' for any None values
                self.tableWidget.setItem(row, col, item)

        keys = [item.title() for item in keys]  # capitalize
        self.tableWidget.setHorizontalHeaderLabels(keys) # add header names
        self.tableWidget.resizeColumnsToContents() # call this after all items have been inserted
    def xoa(self):
        self.tableWidget.setRowCount(0)
    def kill(self):
        dialog = Dialog_kill('app', self)
        dialog.exec()
    def start(self):
        dialog = Dialog_start('app', self)
        dialog.exec()  

class Dialog_re(QDialog, Ui_dialog_re):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.btn_browser.clicked.connect(self.browser)
        self.btn_send.clicked.connect(self.sendnd)
        self.btn_send1.clicked.connect(self.send)
        self.btn_xoa.clicked.connect(self.xoa)
        self.comboBox.currentIndexChanged.connect(self.change)
        self.value.hide()
        self.comboBox_2.hide()
    def browser(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilters(["reg (*.reg)"])
        file_dialog.selectNameFilter("reg (*.reg)")
        # show the dialog
        filenames = []

        if file_dialog.exec_():
            filenames = file_dialog.selectedFiles()
            self.lineEdit.setText(filenames[0]) 
            f = open(filenames[0], 'r', encoding="utf-16")
            with f:
                data = f.read()
                print(data)
                self.plainTextEdit.setPlainText(data)
    def sendnd(self):
        sendMsg('re//sendnd//'+self.plainTextEdit.toPlainText())
    def send(self):
        cbid = self.comboBox.currentIndex()
        path = self.lineEdit_2.text()
        if(cbid==0):
            text = sendMsg('re//send//get_value//'+path+'//'+self.key_value.text())
        elif (cbid==1):
            text = sendMsg('re//send//set_value//'+path+'//'+self.key_value.text()+'//'+self.value.text()+'//'+self.comboBox_2.currentText())
        elif (cbid==2):
            text = sendMsg('re//send//delete_value//'+path+'//'+self.key_value.text())
        elif (cbid==3):
            text = sendMsg('re//send//create_key//'+path)
        elif (cbid==4):
            text = sendMsg('re//send//delete_key//'+path)
        self.noti.insertPlainText(str(text)+'\n')
        self.noti.ensureCursorVisible()
    def xoa(self):
        self.noti.setPlainText("")
    def change(self):
        cbid = self.comboBox.currentIndex()
        if (cbid==1):
            self.key_value.show()
            self.value.show()
            self.comboBox_2.show()
        elif(cbid==3 or cbid==4):
            self.key_value.hide()
            self.value.hide()
            self.comboBox_2.hide()
        else:
            self.key_value.show()
            self.value.hide()
            self.comboBox_2.hide()
class Dialog_keystroke(QDialog, Ui_dialog_keystroke):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.btn_hook.clicked.connect(self.hook)
        self.btn_unhook.clicked.connect(self.unhook)
        self.btn_key.clicked.connect(self.getkey)
        self.btn_delete.clicked.connect(self.delete)
    def hook(self):
        sendMsg('key//hook')
    def unhook(self):
        sendMsg('key//unhook')
    def getkey(self):
        self.textBrowser_2.setText(sendMsg('key//getkey'))
    def delete(self):
        self.textBrowser_2.setText("")

class Dialog_kill(QDialog, Ui_dialog_kill):
    def __init__(self , status, parent=None ):
        super().__init__(parent)
        self.status = status
        self.setupUi(self)       
        self.btn_kill.clicked.connect(self.kill)
    def kill(self):
        sendMsg(self.status+'//'+'kill'+'//'+self.lineEdit.text())
class Dialog_start(QDialog, Ui_dialog_start):
    def __init__(self, status, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.status = status
        self.btn_start.clicked.connect(self.start)
    def start(self):
        sendMsg(self.status+'//'+'start'+'//'+self.lineEdit.text())

def sendMsg(msg):
    s.sendall(bytes(msg, "utf8"))
    data=""
    while True:
        part = s.recv(1024)
        print(len(part))
        data += part.decode("utf8")
        if len(part) < 1024:
            break
    print(data)
    return data

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())