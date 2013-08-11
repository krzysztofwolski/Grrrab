# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'choose_files.ui'
#
# Created: Sun Aug 11 22:15:47 2013
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_dialog_choose_files(object):
    def setupUi(self, dialog_choose_files):
        dialog_choose_files.setObjectName("dialog_choose_files")
        dialog_choose_files.resize(400, 175)
        self.gridLayout = QtGui.QGridLayout(dialog_choose_files)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(dialog_choose_files)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtGui.QLineEdit(dialog_choose_files)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtGui.QLabel(dialog_choose_files)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtGui.QLabel(dialog_choose_files)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtGui.QLabel(dialog_choose_files)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.label_dst_catalog = QtGui.QLabel(dialog_choose_files)
        self.label_dst_catalog.setObjectName("label_dst_catalog")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.label_dst_catalog)
        self.comboBox_first_file = QtGui.QComboBox(dialog_choose_files)
        self.comboBox_first_file.setObjectName("comboBox_first_file")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.comboBox_first_file)
        self.comboBox_last_file = QtGui.QComboBox(dialog_choose_files)
        self.comboBox_last_file.setObjectName("comboBox_last_file")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.comboBox_last_file)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.pushButton_choosen = QtGui.QPushButton(dialog_choose_files)
        self.pushButton_choosen.setObjectName("pushButton_choosen")
        self.gridLayout.addWidget(self.pushButton_choosen, 2, 0, 1, 1)
        self.line = QtGui.QFrame(dialog_choose_files)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 1)

        self.retranslateUi(dialog_choose_files)
        QtCore.QMetaObject.connectSlotsByName(dialog_choose_files)

    def retranslateUi(self, dialog_choose_files):
        dialog_choose_files.setWindowTitle(QtGui.QApplication.translate("dialog_choose_files", "Wybierz pliki", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("dialog_choose_files", "Nazwa wydarzenia", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setPlaceholderText(QtGui.QApplication.translate("dialog_choose_files", "np. \"Wyjazd nad morze\"", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("dialog_choose_files", "Pierwsze zdjęcie", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("dialog_choose_files", "Ostatnie zdjęcie", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("dialog_choose_files", "Folder docelowy", None, QtGui.QApplication.UnicodeUTF8))
        self.label_dst_catalog.setText(QtGui.QApplication.translate("dialog_choose_files", "Folder końcowy...", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_choosen.setText(QtGui.QApplication.translate("dialog_choose_files", "Wybrałem już zdjęcia", None, QtGui.QApplication.UnicodeUTF8))

