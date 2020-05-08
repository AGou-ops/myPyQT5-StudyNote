import sys

from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class LineEditValueLimit(QWidget):
    def __init__(self):
        super(LineEditValueLimit, self).__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle('Limit LineTextBox Value')

        formLayout = QFormLayout()

        intLineEdit = QLineEdit()
        doubleLineEdit = QLineEdit()
        numAndLetterLineEdit = QLineEdit()

        # 定义校验器
        intValidator = QIntValidator(self)
        intValidator.setRange(1, 99)

        doubleValidator = QDoubleValidator(self)
        doubleValidator.setRange(-100, 99)
        # 设置浮点数的精度
        doubleValidator.setNotation(QDoubleValidator.StandardNotation)
        doubleValidator.setDecimals(2)

        reg = QRegExp('[a-zA-Z0-9]+')
        validator = QRegExpValidator(self)
        validator.setRegExp(reg)

        intLineEdit.setValidator(intValidator)
        doubleLineEdit.setValidator(doubleValidator)
        numAndLetterLineEdit.setValidator(validator)

        formLayout.addRow('Type INT', intLineEdit)
        formLayout.addRow('Type double', doubleLineEdit)
        formLayout.addRow('Num and Letter', numAndLetterLineEdit)

        self.setLayout(formLayout)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = LineEditValueLimit()
    sys.exit(app.exec_())
