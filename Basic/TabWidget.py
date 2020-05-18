import sys
from PyQt5.QtWidgets import *


class TabWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Tab Widget')
        self.setGeometry(300, 300, 250, 180)
        # Create Three Different Widget
        self.tab1 = QWidget()
        self.tab3 = QWidget()
        self.tab2 = QWidget()

        self.addTab(self.tab1, 'Tab1')
        self.addTab(self.tab2, 'Tab2')
        self.addTab(self.tab3, 'Tab3')

        self.tab1UI()
        self.tab2UI()
        self.tab3UI()

    def tab1UI(self):
        layout = QFormLayout()
        layout.addRow('name: ', QLineEdit())
        layout.addRow('passwd: ', QLineEdit())
        self.setTabText(0, 'Login')
        self.tab1.setLayout(layout)

    def tab2UI(self):
        layout = QVBoxLayout()
        previewBtn = QPushButton('Preview')
        layout.addWidget(previewBtn)
        textEdit = QTextEdit()
        layout.addWidget(textEdit)
        self.setTabText(1, 'Preview')
        self.tab2.setLayout(layout)

    def tab3UI(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TabWidget()
    window.show()
    sys.exit(app.exec_())
