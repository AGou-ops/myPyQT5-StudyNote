from PyQt5.QtWidgets import *
import sys


class TextEdit(QWidget):
    def __init__(self):
        super(TextEdit, self).__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle('QTextEdit')

        self.textEdit = QTextEdit('Hit below Button')
        btnText = QPushButton('Show Text', self)
        btnHTML = QPushButton('Show HTML', self)

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(btnText)
        layout.addWidget(btnHTML)

        btnText.clicked.connect(self.btnText_clicked)
        btnHTML.clicked.connect(self.btnHTML_clicked)

        self.setLayout(layout)

    def btnText_clicked(self):
        self.textEdit.setPlainText('Show Plain Text Here.')
        print(self.textEdit.toPlainText())

    def btnHTML_clicked(self):
        self.textEdit.setHtml('<font color="red" size="5">Show HTML.</font>')
        print(self.textEdit.toHtml())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TextEdit()
    window.show()
    sys.exit(app.exec_())