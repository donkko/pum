# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\DK\pum\prototype.ui'
#
# Created: Sun Feb 22 17:54:47 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

import json
import requests
from random import randint
from PyQt4 import QtCore, QtGui


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtGui.QMainWindow):

    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(484, 281)

        self.centralwidget = QtGui.QWidget(self)

        self.startButton = QtGui.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(180, 220, 131, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("System"))
        font.setPointSize(10)
        self.startButton.setFont(font)
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.startButton.clicked.connect(self.startButtonClicked)

        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(40, 80, 171, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("System"))
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))

        self.urlEdit = QtGui.QLineEdit(self.centralwidget)
        self.urlEdit.setGeometry(QtCore.QRect(220, 80, 221, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("System"))
        font.setPointSize(10)
        self.urlEdit.setFont(font)
        self.urlEdit.setObjectName(_fromUtf8("urlEdit"))

        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(38, 40, 422, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("System"))
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))

        self.dayLimitSpinBox = QtGui.QSpinBox(self.centralwidget)
        self.dayLimitSpinBox.setGeometry(QtCore.QRect(290, 150, 91, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("System"))
        font.setPointSize(10)
        self.dayLimitSpinBox.setFont(font)
        self.dayLimitSpinBox.setMinimum(1)
        self.dayLimitSpinBox.setMaximum(1000)
        self.dayLimitSpinBox.setProperty("value", 800)
        self.dayLimitSpinBox.setObjectName(_fromUtf8("dayLimitSpinBox"))

        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 150, 221, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("System"))
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.questionBox = QtGui.QToolButton(self.centralwidget)
        self.questionBox.setGeometry(QtCore.QRect(400, 160, 21, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("System"))
        font.setPointSize(10)
        self.questionBox.setFont(font)
        self.questionBox.setObjectName(_fromUtf8("questionBox"))
        self.questionBox.clicked.connect(self.showDialog)

        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(_translate(None, "Pum", None))
        self.startButton.setText(_translate(None, "자동방문 시작", None))
        self.comboBox.setItemText(0, _translate(None, "http://blog.naver.com/", None))
        #self.comboBox.setItemText(1, _translate("MainWindow", "tistory.com/", None))
        self.label.setText(_translate(None, "방문할 URL을 입력해주세요 (현재는 네이버블로그만 지원)", None))
        self.label_2.setText(_translate(None, "일일 방문자수 제한 (최대 1000)", None))
        # self.questionBox.setToolTip(_translate("MainWindow", "<html><head/><body><p>일일 방문자수 제한을 무제한으로 바꾸고 싶다면... fdsa@fdas.fds</p></body></html>", None))
        # self.questionBox.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>일일방문자수 제한을 무제한으로 바꾸고 싶다면!</p></body></html>", None))
        self.questionBox.setText(_translate(None, "?", None))

    def startButtonClicked(self):
        #sender = self.sender()

        self.type = self.comboBox.currentText().toUtf8().data()
        self.url = self.urlEdit.text().toUtf8().data()
        self.daylimit = self.dayLimitSpinBox.value()

        self.comboBox.setEnabled(False)
        self.urlEdit.setEnabled(False)
        self.dayLimitSpinBox.setEnabled(False)
        self.startButton.setEnabled(False)


        self.statusBar().showMessage(_translate(None, '자동방문을 시작합니다...', None))
        self.start_visiting()

    def start_visiting(self):
        try:
            #print type(self.daylimit)
            req = get_html('http://54.65.93.177/api/get/urllist', params={"myurl": self.url, "daylimit": self.daylimit})
            if req != None:
                json_dic = json.loads(req.text)
                if json_dic["status"] == 200:
                    self.statusBar().showMessage(_translate(None, '자동방문 동작중', None))
                    for url in json_dic["urls"]:
                        get_html(url)
                elif json_dic["status"] == 600:
                    self.statusBar().showMessage(_translate(None, '일일 방문자수 제한을 초과하였습니다.', None))
                else:
                    self.statusBar().showMessage(_translate(None, '예기치 못한 오류가 발생하였습니다. 관리자에게 문의해주시기 바랍니다.', None))
            else:
                self.statusBar().showMessage(_translate(None, '예기치 못한 오류가 발생하였습니다. 관리자에게 문의해주시기 바랍니다.', None))
        finally:
            QtCore.QTimer.singleShot(randint(60 * 1000, 180 * 1000), self.start_visiting)


    def showDialog(self):
        self.dialog = PopUpDialog()
        self.dialog.setupUi()
        self.dialog.show()
        self.dialog.exec_()


class PopUpDialog(QtGui.QDialog):
    def __init__(self):
        super(PopUpDialog, self).__init__()

    def setupUi(self):
        self.resize(200, 120)
        self.setWindowTitle(_translate(None, "Pum", None))
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(20, 20, 140, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("System"))
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setText(_translate(None, "일일 방문자수 제한풀기", None))

        self.label2 = QtGui.QLabel(self)
        self.label2.setGeometry(QtCore.QRect(20, 45, 140, 20))
        self.label2.setFont(font)
        self.label2.setText(_translate(None, "fdsa1234@fdsa.fds", None))

        self.label3 = QtGui.QLabel(self)
        self.label3.setGeometry(QtCore.QRect(20, 70, 140, 20))
        self.label3.setFont(font)
        self.label3.setText(_translate(None, "위 메일로 연락주세요", None))


HTML_REQUEST_HEADERS = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate, sdch',
'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4',
'Connection': 'keep-alive',
'Cookie': '',
'Host': 'blog.naver.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36'
}


def get_html(url, params=None, headers=HTML_REQUEST_HEADERS):
    req = requests.get(url, params=params, headers=headers)
    # print u'[get_html] url:', unicode(req.url)
    # print u'[get_html] status_code:', unicode(req.status_code)
    if req.status_code != 200:
        return None
    req.encoding = 'euc-kr'
    return req


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)

    mainWindow = Ui_MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
