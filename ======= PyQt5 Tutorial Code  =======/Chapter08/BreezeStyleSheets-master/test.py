from PyQt5 import QtWidgets
from PyQt5.QtCore import QFile, QTextStream
import breeze_resources,sys
import example



app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()
ui = example.Ui_MainWindow()
ui.setupUi(window)
# set stylesheet
file = QFile(":/light.qss")
file.open(QFile.ReadOnly | QFile.Text)
stream = QTextStream(file)
app.setStyleSheet(stream.readAll())

# code goes here
window.show()
app.exec_()