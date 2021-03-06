# -*- coding: utf-8 -*
import shutil
import os
import sys
import time
import datetime
import json
import platform
from PIL import Image
from PIL.ExifTags import TAGS
from PySide import QtCore, QtGui

from main_window import Ui_MainWindow
from copy_dialog import Ui_dialog_copy # TODO: change names
from choose_files import Ui_dialog_choose_files
from select_type import Ui_SelectTypeDialog


class MediaFile():
    """
    Container class for media files.
    """

    def __init__(self, path = None, type = None):
        """
        :param path: string. path to file
        :param type: atring. type of file. Accepts "photo" or "video"
        """
        self.path = path
        self.type = type

        self.exif = None
        self.get_exif()
        self.date = None
        self.set_date()

    def get_exif(self):
        """
        Tries to read EXIF data from file. If there is any error, method return False
        """
        if self.path is None:
            return None
        else:
            try:
                ret = {}
                i = Image.open(self.path)
                info = i._getexif()
                if info is None:
                    return False
                for tag, value in info.items():
                    decoded = TAGS.get(tag, tag)
                    ret[decoded] = value
                self.exif = ret
                return True
            except Exception as e:
                return False


    def set_date(self):
        """
        Tries to gather data/time information.
        * first try read EXIF data
        * if failed takes fle modification time
        """
        if self.exif is None:
            self.get_exif()
        str_date = None
        try:
            str_date = self.exif.get("DateTime")
            self.date = time.strptime(str_date, "%Y:%m:%d %H:%M:%S")
        except:
            self.date = time.gmtime(os.path.getctime(self.path))

        return True


class MySignal(QtCore.QObject):
    sig = QtCore.Signal(str)
    sigCurrentFileLabel = QtCore.Signal(str)
    sigProgress = QtCore.Signal(int)
    sigSourceDirectoryChanged = QtCore.Signal(str)
    sigVideoDirectoryChanged = QtCore.Signal(str)
    sigPhotosDirectoryChanged = QtCore.Signal(str)
    sigTargetDirectoryChanged = QtCore.Signal(str)
    sigUpdateBigStatus = QtCore.Signal(str)
    sigFilesTypeChanged = QtCore.Signal(str)


class MainWindow(QtGui.QMainWindow):
    photos_file_types = (".jpg", ".jpeg", ".JPG", ".JPEG")
    videos_file_types = (".MTS")

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # signals oracle
        self.signal = MySignal()

        # loading settings from file
        self.json = {}
        self.path_settings = os.path.join(os.path.dirname( os.path.realpath(__file__) ), "settings.json")

        if not os.path.exists(self.path_settings):
            try:
                f = open(self.path_settings, "w")
                # f.open()
                self.json["path_destination_photos"] = ""
                self.json["path_destination_videos"] = ""
                f.write(json.dumps(self.json))
                f.close()
            except Exception as e:
                print "Nie można utworzyć pliku ustawień!"
                print e
        else:
            try:
                f = open(self.path_settings, "r")
                # f.open()
                self.json = json.loads(f.read())
                f.close()
            except Exception as e:
                print "Nie mogę otworzyć pliku ustawień"
                print e


        self.path_source = ""
        self.path_destination_photos = ""
        self.path_destination_videos = ""
        self.path_dir_name = ""

        self.files_type = None
        self.media_files = []
        self.found_videos = []
        self.found_photos = []
        self.found_videos_strings = []
        self.found_photos_strings = []
        self.media_files_strings = []
        self.first_file = 0
        self.last_file = 0
        self.event_name = None

        # signals connecting
        self.ui.pushButton_choose.clicked.connect(self.open_choose_files_dialog)
        self.ui.pushButton_grrrab.clicked.connect(self.open_copy_dialog)
        self.ui.pushButton_manual_source.clicked.connect(self.open_source_directory_dialog)
        self.ui.pushButton_manual_dst_photos.clicked.connect(self.open_photos_directory_dialog)
        self.ui.pushButton_manual_dst_videos.clicked.connect(self.open_videos_directory_dialog)
        self.ui.pushButton_auto_source.clicked.connect(self.auto_find_source)
        self.ui.pushButton_auto_dst_photos.clicked.connect(self.auto_find_destination_photos)
        self.ui.pushButton_auto_dst_videos.clicked.connect(self.auto_find_destination_videos)

        # todo: do it if bored: manually edited paths
        # self.ui.lineEdit_path_source.textEdited.connect(self.source_directory_edited)
        # self.ui.lineEdit_path_dst_photos.textEdited.connect(self.videos_directory_edited)
        # self.ui.lineEdit_path_dst_camera.textEdited.connect(self.photos_directory_edited)

        self.signal.sigSourceDirectoryChanged.connect(self.set_source_directory)
        self.signal.sigVideoDirectoryChanged.connect(self.set_video_directory)
        self.signal.sigPhotosDirectoryChanged.connect(self.set_photos_directory)
        self.signal.sigFilesTypeChanged.connect(self.set_files_type)
        # self.signal.sigTargetDirectoryChanged.connect()

        # paths setups
        self.signal.sigPhotosDirectoryChanged.emit(self.json.get("path_destination_photos"))
        self.signal.sigVideoDirectoryChanged.emit(self.json.get("path_destination_videos"))

    def closeEvent(self, event):
        f = open(self.path_settings, "w")
        # f.open()
        f.write(json.dumps(self.json))
        f.close()

    # todo: do it if bored: manually edited paths
    # def source_directory_edited(self):
    #     self.signal.sigSourceDirectoryChanged.emit(self.ui.lineEdit_path_source.text())
    #
    # def videos_directory_edited(self):
    #     self.signal.sigVideoDirectoryChanged.emit(self.ui.lineEdit_path_dst_camera.text)
    #
    # def photos_directory_edited(self):
    #     self.signal.sigPhotosDirectoryChanged.emit(self.ui.lineEdit_path_dst_photos.text)

    def auto_find_source(self):
        if platform.system() == "Windows":
            dl = 'EFGHIJKLMNOPQRSTUVWXYZ'
            drives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
            if len(drives) == 1:
                self.signal.sigSourceDirectoryChanged.emit(drives[0])

        else:
            # todo: make linux port
            print "Feature not supported in linux. ~Soon~"
        

    def auto_find_destination_photos(self):
        pass

    def auto_find_destination_videos(self):
        pass

    def set_files_type(self, type):
        if type == "photo":
            self.files_type = "photo"
            self.media_files = self.found_photos
            self.media_files_strings = self.found_photos_strings
        elif type == "video":
            self.files_type = "video"
            self.media_files = self.found_videos
            self.media_files_strings = self.found_videos_strings
        else:
            raise Exception("Invalid file type!")

    def set_source_directory(self, path):
        # todo: put some assets here

        path = os.path.normpath(path)

        if os.path.isdir(str(path)):
            self.path_source = path
            self.ui.lineEdit_path_source.setText(path)
            self.ui.label_status_source.setText("<font color='green'>Ok!</font>")
        else:
            print u"Niepoprawny katalog źródłowy"

    def set_photos_directory(self, path):
        # todo: put some assets here
        path = os.path.normpath(path)

        if os.path.isdir(str(path)):
            self.path_destination_photos = path
            self.json["path_destination_photos"] = path
            self.ui.lineEdit_path_dst_photos.setText(path)
            self.ui.label_status_dst_photos.setText("<font color='green'>Ok!</font>")
        else:
            print u"Niepoprawny katalog zdjęć"

    def set_video_directory(self, path):
        # todo: put some assets here
        path = os.path.normpath(path)

        if os.path.isdir(str(path)):
            self.path_destination_videos = path
            self.json["path_destination_videos"] = path
            #todo : rename this lineedit to "video"
            self.ui.lineEdit_path_dst_videos.setText(path)
            self.ui.label_status_dst_video.setText("<font color='green'>Ok!</font>")
        else:
            print u"Niepoprawny katalog kamery"

    def open_choose_files_dialog(self):
        #sprawdz czy podano dane

        if not (os.path.isdir(self.path_destination_videos) and\
            os.path.isdir(self.path_destination_photos) and\
            os.path.isdir(self.path_source)):
            reply = QtGui.QMessageBox.critical(self, u"Uzupełnij dane",\
                u"Nie wszystkie dane zostały uzupełnione.",\
                QtGui.QMessageBox.Ok)
            return

        # Clean up
        self.files_type = ""
        self.found_videos = []
        self.found_photos = []
        self.found_photos_strings = []
        self.found_videos_strings = []

        #zaladuj nazwy i daty
        for root, dirs, files in os.walk(self.path_source):
            for name in files:
                if name.endswith(self.photos_file_types):
                    mf = MediaFile(path=os.path.join(root,name))
                    t =  mf.date
                    mf.type = "photo"
                    if mf.date is not None:
                        self.found_photos.append(mf)
                        self.found_photos_strings.append(name + "  " + time.strftime("%Y-%m-%d %H:%M", t))
                elif name.endswith(self.videos_file_types):
                    mf = MediaFile(path=os.path.join(root,name))
                    t =  mf.date
                    mf.type = "video"
                    if mf.date is not None:
                        self.found_videos.append(mf)
                        self.found_videos_strings.append(name + "  " + time.strftime("%Y-%m-%d %H:%M", t))


        if len(self.found_photos) == 0 and len(self.found_videos) == 0:
            reply = QtGui.QMessageBox.critical(self, u"Nie znaleziono plikow",\
                u"Przykto mi, ale nie znaleziono plików",\
                QtGui.QMessageBox.Ok)
            return
        elif len(self.found_photos) > 0 and len(self.found_videos) == 0:
            self.signal.sigFilesTypeChanged.emit("photo")
        elif len(self.found_videos) > 0 and len(self.found_photos) == 0:
            self.signal.sigFilesTypeChanged.emit("video")
        else:
            dlg = SelectTypeDialog(mw = self)
            dlg.show()
            dlg.exec_()

            if self.files_type != "photo" and self.files_type != "video":
                print "asdasdasd"
                return # no files type selected


        self.last_file = len(self.media_files) - 1
        #odpal

        a = ChooseDialog(mw = self)
        a.show()
        a.exec_()

    def open_copy_dialog(self):
        if not (os.path.isdir(self.path_destination_videos) and\
            os.path.isdir(self.path_destination_photos) and\
            os.path.isdir(self.path_source)):
            reply = QtGui.QMessageBox.critical(self, u"Uzupełnij dane",\
                u"Nie wszystkie dane zostały uzupełnione.",\
                QtGui.QMessageBox.Ok)
            return

        a = CopyDialog(mw = self)
        a.show()
        a.exec_()

    def open_source_directory_dialog(self):
        selected_dir = self.openFile(directory=True)[0]
        if os.path.isdir(selected_dir):
            self.signal.sigSourceDirectoryChanged.emit(selected_dir)

    def open_videos_directory_dialog(self):
        selected_dir = self.openFile(directory=True)[0]
        if os.path.isdir(selected_dir):
            self.signal.sigVideoDirectoryChanged.emit(selected_dir)

    def open_photos_directory_dialog(self):
        selected_dir = self.openFile(directory=True)[0]
        if os.path.isdir(selected_dir):
            self.signal.sigPhotosDirectoryChanged.emit(selected_dir)

    def openFile(self, directory = False):
        dialog = QtGui.QFileDialog()
        if directory:
            dialog.setFileMode(QtGui.QFileDialog.Directory)
            dialog.setOption(QtGui.QFileDialog.ShowDirsOnly)
        dialog.exec_()

        return dialog.selectedFiles()


class ChooseDialog(QtGui.QDialog):
    def __init__(self, parent=None, mw = None):
        super(ChooseDialog, self).__init__(parent)
        self.ui = Ui_dialog_choose_files()
        self.ui.setupUi(self)
        self.mw = mw

        if mw is None:
            raise Exception("Ten dialog potrzebuje referencji do glownego okna!")

        self.ui.comboBox_first_file.addItems(self.mw.media_files_strings)
        self.ui.comboBox_last_file.addItems(self.mw.media_files_strings)

        self.ui.comboBox_last_file.setCurrentIndex(self.mw.last_file)

        self.set_event_name()

        self.ui.comboBox_first_file.currentIndexChanged.connect(self.set_first)
        self.ui.comboBox_last_file.currentIndexChanged.connect(self.set_last)
        self.ui.lineEdit.textChanged.connect(self.set_event_name)
        self.ui.pushButton_choosen.clicked.connect(self.close)

    def set_first(self):
        self.mw.first_file = self.ui.comboBox_first_file.currentIndex()
        self.set_event_name()

    def set_last(self):
        self.mw.last_file = self.ui.comboBox_last_file.currentIndex()

    def set_event_name(self):
        e = self.ui.lineEdit.text()
        date = self.mw.media_files[self.mw.first_file].date

        e = time.strftime("%Y-%m", date) + " " + e

        self.mw.event_name = e

        self.mw.path_dirname = os.path.join(self.mw.path_destination_photos, e)
        self.ui.label_dst_catalog.setText(self.mw.path_dirname)


class SelectTypeDialog(QtGui.QDialog):
    def __init__(self, parent=None, mw = None):
        super(SelectTypeDialog, self).__init__(parent)
        self.ui = Ui_SelectTypeDialog()
        self.ui.setupUi(self)
        self.signal = MySignal()

        self.mw = mw
        if mw is None:
            raise Exception("Ten dialog potrzebuje referencji do glownego okna!")

        self.ui.label_counter_photos.setText(str(len(self.mw.found_photos)))
        self.ui.label_counter_videos.setText(str(len(self.mw.found_videos)))
        self.ui.pushButton_copy_photos.clicked.connect(self.set_type_photos)
        self.ui.pushButton_copy_videos.clicked.connect(self.set_type_videos)
        self.ui.pushButton_cancel.clicked.connect(self.close)

    def set_type_photos(self):
        self.mw.signal.sigFilesTypeChanged.emit("photo")
        self.close()

    def set_type_videos(self):
        self.mw.signal.sigFilesTypeChanged.emit("video")
        self.close()


class CopyDialog(QtGui.QDialog):
    def __init__(self, parent=None, mw = None):
        super(CopyDialog, self).__init__(parent)
        self.ui = Ui_dialog_copy()
        self.ui.setupUi(self)
        self.signal = MySignal()

        self.ui.pushButton_end.clicked.connect(self.close)

        self.signal.sigCurrentFileLabel.connect(self.set_file_label)
        self.signal.sigProgress.connect(self.set_progress)

        self.mw = mw
        if mw is None:
            raise Exception("Ten dialog potrzebuje referencji do glownego okna!")
        # todo: we need some asserts hereee!

        self.ui.progressBar.setValue(0)
        self.ui.progressBar.setMaximum(len(self.mw.media_files))

        self.thread = CopyThread(mw = self.mw, cw = self)
        self.thread.start()
        #

    def set_file_label(self, text):
        self.ui.label_file_now.setText(text)

    def set_progress(self, v):
        self.ui.progressBar.setValue(int(v))


class CopyThread(QtCore.QThread):
    def __init__(self, parent = None, mw = None, cw = None):
        QtCore.QThread.__init__(self, parent)
        self.exiting = False
        self.mw = mw
        self.cw = cw

    def run(self):
        print "Worker thread started it's work."

        if not os.path.exists(self.mw.path_dirname):
            os.makedirs(self.mw.path_dirname)

        # f_nr = len([name for name in os.listdir('.') if os.path.isfile(name)])

        v = 0
        for f in self.mw.media_files:
            print f.path, self.mw.path_dirname
            self.cw.signal.sigCurrentFileLabel.emit(f.path)
            # todo: nazwa pliku powinna zalezec od liczby plikow w folderze
            try:
                # ext = os.path.basename(f.path).split(".")[-1]
                # n = self.mw.path_dirname

                shutil.move(f.path, self.mw.path_dirname)
            except Exception as e:
                print e

            v += 1
            self.cw.signal.sigProgress.emit(v)

            if v > self.mw.last_file:
                break

        self.cw.signal.sigCurrentFileLabel.emit(u"Operacja zakończona sukcesem!")
        self.cw.ui.pushButton_end.setEnabled(True)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())