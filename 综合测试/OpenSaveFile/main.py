from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog
import sys


class TextEditor(QtWidgets.QMainWindow):
    def __init__(self):
        super(TextEditor, self).__init__()
        uic.loadUi('main.ui', self)
        self.actionopen.triggered.connect(self.openFile)
        self.actionsave.triggered.connect(self.saveFile)
        self.actionexit.triggered.connect(self.exitFile)

    def exitFile(self):
        QtWidgets.QApplication.quit()

    def saveFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "", "All files(*);; Text "
                                                                                             "Files(*.txt)",
                                                  options=options)
        try:
            fobj = open(fileName, 'w')
            data = self.textEdit.toPlainText()
            fobj.write(data)
            fobj.close()
        except IOError:
            self.setStatusTip("未选择文件")

    def openFile(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)

            fobj = open(fileName, 'r')
            data = fobj.read()
            fobj.close()
            self.textEdit.setText(data)


app = QtWidgets.QApplication([])
win = TextEditor()
win.show()
sys.exit(app.exec())
