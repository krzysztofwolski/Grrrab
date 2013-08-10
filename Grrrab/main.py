import shutil
import os
import time
from PIL import Image
from PIL.ExifTags import TAGS
from PySide import QtCore



class MediaFile():

    def __init__(self, path = None, type = None):
        self.path = path
        self.type = type

        self.exif = None
        self.get_exif()
        self.date = None
        self.set_date()

    def get_exif(self):
        if self.path is None:
            return None
        else:
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

    def set_date(self):
        if self.exif is None:
            if self.get_exif() is False:
                return None

        str_date = self.exif.get("DateTime")
        if str_date is None:
            return None
        # 2004:11:28 14:03:46
        self.date = time.strptime(str_date, "%Y:%m:%d %H:%M:%S")
        return True

# folder = "/media/krzyh/Album/Aparat/2004-11 Futra, u Irki"
# plik = "Obraz 001.jpg"

folder = "/media/krzyh/Album/Aparat/2004-11 Futra, u Irki"
plik = "DSC00489.JPG"
# mf = MediaFile(path=os.path.join(folder, plik))

i = 1
for root, dirs, files in os.walk(folder):
    for name in files:
        if name.endswith((".jpg", "jpeg", ".JPG", "JPEG")):
            # print(root, name)
            # shutil.copy(src=os.path.join(root,name), dst=os.path.join(flat_path, os.path.split(root)[-1] + " " +name))
            print os.path.join(root,name),
            mf = MediaFile(path=os.path.join(root,name))
            t =  mf.date
            print time.strftime("%Y-%m-%d %H:%M", t)
