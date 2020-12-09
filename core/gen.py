import qrcode
from PyQt5.QtGui import QIcon

from untitled import Ui_Form
from PyQt5.QtWidgets import QMainWindow, QAction, QFileDialog


class CodeWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # 调用Ui_Mainwindow中的函数setupUi实现显示界面
        self.set_click()

    def set_click(self):
        self.pushButton.clicked.connect(self.gen_code)
        self.openPathButton.clicked.connect(self.open_file_path)

    def open_file_path(self):
        get_directory_path = QFileDialog.getExistingDirectory(self,
                                                              "选取指定文件夹",
                                                              ".")
        self.path = str(get_directory_path)
        self.filePathlineEdit.setText(str(get_directory_path))

    def get_path(self):
        print(1)
        return "haha"

    def gen_code(self):
        text = self.textEdit.toPlainText()
        qr = qrcode.QRCode(version=20, )
        qr.add_data(text)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(f'{self.path}/qrcode.jpg')