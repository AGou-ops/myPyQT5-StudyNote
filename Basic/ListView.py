from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListView, QMessageBox
from PyQt5.QtCore import QStringListModel
import sys


class ListView(QWidget):
    def __init__(self):
        super(ListView, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("List View")
        layout = QVBoxLayout()
        listModel = QStringListModel()
        listview = QListView()

        self.list = ["List1", "List2", "List3", "List4"]
        listModel.setStringList(self.list)

        listview.setModel(listModel)
        listview.clicked.connect(self.clicked)
        layout.addWidget(listview)

        self.setLayout(layout)

    def clicked(self, item):
        QMessageBox.information(self, "QListView", "您选择了：" + self.list[item.row()])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ListView()
    win.show()
    sys.exit(app.exec_())
