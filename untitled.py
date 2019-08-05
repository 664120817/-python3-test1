# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(791, 641)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.widget.setObjectName("widget")
        self.textBrowser = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser.setGeometry(QtCore.QRect(-5, 1, 401, 641))
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 12pt \"Arial\";")
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.widget_2.setObjectName("widget_2")
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setGeometry(QtCore.QRect(110, 350, 141, 41))
        self.pushButton.setStyleSheet("font: 9pt \"微软雅黑\";\n"
"")
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.widget_2)
        self.textEdit.setGeometry(QtCore.QRect(0, -4, 401, 321))
        self.textEdit.setStyleSheet("background-color: rgb(153, 153, 153);")
        self.textEdit.setObjectName("textEdit")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.widget_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 451, 401, 171))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 390, 91, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.widget_2)

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.slot1)
        self.pushButton_2.clicked.connect(Form.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "点击翻译"))
        self.textBrowser_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">请在上方灰色区域输入要翻译的句子</p></body></html>"))
        self.pushButton_2.setText(_translate("Form", "清空"))

import image_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

