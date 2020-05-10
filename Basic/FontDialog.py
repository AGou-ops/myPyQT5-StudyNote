from PyQt5.QtWidgets import *
import sys

class FontDialog(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle('Show Font Dialog')
        layout = QVBoxLayout()
        self.fontBtn  = QPushButton('Choose Font')
        self.fontBtn.clicked.connect(self.getFont)

        self.fontLabel = QLabel('TEST Font !')

        layout.addWidget(self.fontBtn)
        layout.addWidget(self.fontLabel)
        self.setLayout(layout)
        self.show()

    def getFont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.fontLabel.setFont(font)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FontDialog()
    sys.exit(app.exec_())