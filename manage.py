import sys
from core.gen import CodeWidget
from PyQt5 import QtWidgets

if __name__ == "__main__":
  app = QtWidgets.QApplication(sys.argv) # 创建一个QApplication，也就是你要开发的软件app
  code_widget = CodeWidget()
  code_widget.show()            # 执行QMainWindow的show()方法，显示这个QMainWindow
  sys.exit(app.exec_())          # 使用exit()或者点击关闭按钮退出QApplicat