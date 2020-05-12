import sys
from PyQt5.QtWidgets import *


class ComboBox(QWidget):
    def __init__(self):
        super(ComboBox, self).__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle('Combo Box')
        layout = QVBoxLayout()

        self.label = QLabel('Please Choose')

        self.comboBox = QComboBox()
        self.comboBox.addItem('Java')
        self.comboBox.addItem('Python')
        self.comboBox.addItem('C++')
        self.comboBox.addItems(['C', 'GoLang', 'Ruby'])

        # self.comboBox.currentIndexChanged.connect(self.selectionChanged)
        self.comboBox.activated[str].connect(self.selectionChanged)

        layout.addWidget(self.comboBox)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def selectionChanged(self, i):
        # self.label.setText(self.comboBox.currentText())
        # self.label.adjustSize()
        self.label.setText(i)
        self.label.adjustSize()

        for count in range(self.comboBox.count()):
            print('item ' + str(count) + ' = ' + self.comboBox.itemText(count))

        print('current index', i, 'selection changed', self.comboBox.currentText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ComboBox()
    window.show()
    sys.exit(app.exec_())
