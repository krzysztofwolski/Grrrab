# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'copy.ui'
#
# Created: Sun Aug 11 22:15:48 2013
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_dialog_copy(object):
    def setupUi(self, dialog_copy):
        dialog_copy.setObjectName("dialog_copy")
        dialog_copy.resize(400, 118)
        self.gridLayout = QtGui.QGridLayout(dialog_copy)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.progressBar = QtGui.QProgressBar(dialog_copy)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.label = QtGui.QLabel(dialog_copy)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_file_now = QtGui.QLabel(dialog_copy)
        self.label_file_now.setObjectName("label_file_now")
        self.verticalLayout.addWidget(self.label_file_now)
        self.pushButton_end = QtGui.QPushButton(dialog_copy)
        self.pushButton_end.setEnabled(False)
        self.pushButton_end.setObjectName("pushButton_end")
        self.verticalLayout.addWidget(self.pushButton_end)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.retranslateUi(dialog_copy)
        QtCore.QMetaObject.connectSlotsByName(dialog_copy)

    def retranslateUi(self, dialog_copy):
        dialog_copy.setWindowTitle(QtGui.QApplication.translate("dialog_copy", "Kopiowanie w trakcie", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("dialog_copy", "Kopiuję teraz: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_file_now.setText(QtGui.QApplication.translate("dialog_copy", "nic.", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_end.setText(QtGui.QApplication.translate("dialog_copy", "Koniec", None, QtGui.QApplication.UnicodeUTF8))

