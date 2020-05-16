from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

'''

显示二维表数据（QTableView控件）

数据源

Model

需要创建QTableView实例和一个数据源（Model），然后将两者关联

MVC：Model   Viewer   Controller

MVC的目的是将后端的数据和前端页面的耦合度降低



'''

class TableView(QWidget):

    def __init__(self):
        super(TableView, self).__init__()
        self.initUI()


    def initUI(self):
        self.setWindowTitle('show tables')
        self.model = QStandardItemModel(4, 3)
        self.model.setHorizontalHeaderLabels(['id', 'name', 'age'])
        self.tableview = QTableView()
        self.tableview.setModel(self.model)

        item11 = QStandardItem('10')
        item12 = QStandardItem('雷神')
        item13 = QStandardItem('2000')
        self.model.setItem(0, 0, item11)
        self.model.setItem(0, 1, item12)
        self.model.setItem(0, 2, item13)

        item31 = QStandardItem('30')
        item32 = QStandardItem('死亡女神')
        item33 = QStandardItem('3000')
        self.model.setItem(2, 0, item31)
        self.model.setItem(2, 1, item32)
        self.model.setItem(2, 2, item33)

        layout = QVBoxLayout()
        layout.addWidget(self.tableview)
        self.setLayout(layout)

        self.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	table = TableView()
	sys.exit(app.exec_())
