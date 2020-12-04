import qrcode
from untitled import Ui_Form
from PyQt5.QtWidgets import QMainWindow

def gen_code(text):
    qr = qrcode.QRCode(version=20,)
    img = qr.make_image(fill_color="black", back_color="white")
    qr.add_data(text)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save('/mnt/c/Users/hypers/Desktop/advanced_usage.jpg')

class CodeWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # 调用Ui_Mainwindow中的函数setupUi实现显示界面
