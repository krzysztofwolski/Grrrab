# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Sun Aug 11 22:15:48 2013
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(348, 448)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit_path_source = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_path_source.setObjectName("lineEdit_path_source")
        self.verticalLayout.addWidget(self.lineEdit_path_source)
        self.label_status_source = QtGui.QLabel(self.centralwidget)
        self.label_status_source.setObjectName("label_status_source")
        self.verticalLayout.addWidget(self.label_status_source)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_auto_source = QtGui.QPushButton(self.centralwidget)
        self.pushButton_auto_source.setObjectName("pushButton_auto_source")
        self.horizontalLayout.addWidget(self.pushButton_auto_source)
        self.pushButton_manual_source = QtGui.QPushButton(self.centralwidget)
        self.pushButton_manual_source.setObjectName("pushButton_manual_source")
        self.horizontalLayout.addWidget(self.pushButton_manual_source)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 7, 0, 1, 1)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.lineEdit_path_dst_camera = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_path_dst_camera.setObjectName("lineEdit_path_dst_camera")
        self.verticalLayout_2.addWidget(self.lineEdit_path_dst_camera)
        self.label_status_dst_video = QtGui.QLabel(self.centralwidget)
        self.label_status_dst_video.setObjectName("label_status_dst_video")
        self.verticalLayout_2.addWidget(self.label_status_dst_video)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_auto_dst_videos = QtGui.QPushButton(self.centralwidget)
        self.pushButton_auto_dst_videos.setObjectName("pushButton_auto_dst_videos")
        self.horizontalLayout_2.addWidget(self.pushButton_auto_dst_videos)
        self.pushButton_manual_dst_videos = QtGui.QPushButton(self.centralwidget)
        self.pushButton_manual_dst_videos.setObjectName("pushButton_manual_dst_videos")
        self.horizontalLayout_2.addWidget(self.pushButton_manual_dst_videos)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_2, 2, 0, 1, 1)
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 13, 0, 1, 1)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.lineEdit_path_dst_photos = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_path_dst_photos.setObjectName("lineEdit_path_dst_photos")
        self.verticalLayout_3.addWidget(self.lineEdit_path_dst_photos)
        self.label_status_dst_photos = QtGui.QLabel(self.centralwidget)
        self.label_status_dst_photos.setObjectName("label_status_dst_photos")
        self.verticalLayout_3.addWidget(self.label_status_dst_photos)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_auto_dst_photos = QtGui.QPushButton(self.centralwidget)
        self.pushButton_auto_dst_photos.setObjectName("pushButton_auto_dst_photos")
        self.horizontalLayout_3.addWidget(self.pushButton_auto_dst_photos)
        self.pushButton_manual_dst_photos = QtGui.QPushButton(self.centralwidget)
        self.pushButton_manual_dst_photos.setObjectName("pushButton_manual_dst_photos")
        self.horizontalLayout_3.addWidget(self.pushButton_manual_dst_photos)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout_3, 8, 0, 1, 1)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_choose = QtGui.QPushButton(self.centralwidget)
        self.pushButton_choose.setObjectName("pushButton_choose")
        self.verticalLayout_4.addWidget(self.pushButton_choose)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.pushButton_grrrab = QtGui.QPushButton(self.centralwidget)
        self.pushButton_grrrab.setObjectName("pushButton_grrrab")
        self.verticalLayout_4.addWidget(self.pushButton_grrrab)
        self.gridLayout.addLayout(self.verticalLayout_4, 15, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Grrrab", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Źródło plików", None, QtGui.QApplication.UnicodeUTF8))
        self.label_status_source.setText(QtGui.QApplication.translate("MainWindow", "Status folderu źródłowego", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_auto_source.setText(QtGui.QApplication.translate("MainWindow", "Znajdź Automatycznie", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_manual_source.setText(QtGui.QApplication.translate("MainWindow", "Otwórz..", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Folder główny dla nagrań z kamery", None, QtGui.QApplication.UnicodeUTF8))
        self.label_status_dst_video.setText(QtGui.QApplication.translate("MainWindow", "Status folderu kamery", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_auto_dst_videos.setText(QtGui.QApplication.translate("MainWindow", "Znajdź Automatycznie", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_manual_dst_videos.setText(QtGui.QApplication.translate("MainWindow", "Otwórz...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Folder główny dla zdjęć", None, QtGui.QApplication.UnicodeUTF8))
        self.label_status_dst_photos.setText(QtGui.QApplication.translate("MainWindow", "Status folderu zdjęć", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_auto_dst_photos.setText(QtGui.QApplication.translate("MainWindow", "Znajdź Automatycznie", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_manual_dst_photos.setText(QtGui.QApplication.translate("MainWindow", "Otwórz...", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_choose.setText(QtGui.QApplication.translate("MainWindow", "Wybierz pliki", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Musisz jeszcze wybrać pliki!</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_grrrab.setText(QtGui.QApplication.translate("MainWindow", "Pobierz zdjęcia!", None, QtGui.QApplication.UnicodeUTF8))

