import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class SpinBox(QWidget):
    def __init__(self):
        super(SpinBox, self).__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle('Spin Box')
        self.resize(300, 100)

        layout = QVBoxLayout()
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.label)

        self.spinbox = QSpinBox()
        self.spinbox.setValue(25)
        self.spinbox.setSingleStep(5)
        self.label.setText('Current Value is: ' + str(self.spinbox.value()))
        layout.addWidget(self.spinbox)
        self.spinbox.valueChanged.connect(self.valueChanged)

        self.setLayout(layout)
        self.show()

    def valueChanged(self):
        sender = self.sender()
        self.label.setText('Current Value is: ' + sender.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SpinBox()
    sys.exit(app.exec_())
