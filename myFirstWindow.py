import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    window.resize(500, 350)
    window.move(500, 500)

    window.setWindowTitle('my first pyqt5 window')
    window.show()
    # 进入程序主循环，并通过exit函数确保主循环安全结束
    sys.exit(app.exec_())
