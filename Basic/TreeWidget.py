import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QBrush, QColor
from PyQt5.QtCore import Qt


class BasicTreeWidget(QMainWindow):
    def __init__(self, parent=None):
        super(BasicTreeWidget, self).__init__(parent)
        self.setWindowTitle('树控件（QTreeWidget）的基本用法')
        self.setGeometry(500, 300, 450, 280)

        self.tree = QTreeWidget()
        # 为树控件指定列数
        self.tree.setColumnCount(2)

        # 指定列标签
        self.tree.setHeaderLabels(['Key', 'Value'])

        root = QTreeWidgetItem(self.tree)
        root.setText(0, 'root')
        root.setIcon(0, QIcon('/home/agou-ops/PycharmProjects/myPyQT5-StudyNote/imgs/logo32_32.ico'))
        self.tree.setColumnWidth(0, 160)

        # 添加子节点1
        child1 = QTreeWidgetItem(root)
        child1.setText(0, 'child1')
        child1.setText(1, 'Value1')
        child1.setIcon(0, QIcon('/home/agou-ops/PycharmProjects/myPyQT5-StudyNote/imgs/logo32_32.ico'))
        child1.setCheckState(0, Qt.Checked)

        # 添加子节点2
        child2 = QTreeWidgetItem(root)
        child2.setText(0, 'child2')
        child2.setIcon(0, QIcon('/home/agou-ops/PycharmProjects/myPyQT5-StudyNote/imgs/test.jpg'))

        # 为child2添加一个子节点
        child3 = QTreeWidgetItem(child2)
        child3.setText(0, 'child2-1')
        child3.setText(1, 'Value2-1')
        child3.setIcon(0, QIcon('/home/agou-ops/PycharmProjects/myPyQT5-StudyNote/imgs/test.jpg'))

        child4 = QTreeWidgetItem(child2)
        child4.setText(0, 'child2-2')
        child4.setText(1, 'Value2-2')
        # 展开所有子项
        self.tree.expandAll()
        # 节点点击事件
        self.tree.clicked.connect(self.onTreeClicked)

        self.setCentralWidget(self.tree)

    def onTreeClicked(self, index):
        item = self.tree.currentItem()
        print(index.row())
        print('key=%s,value=%s' % (item.text(0), item.text(1)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tree = BasicTreeWidget()
    tree.show()
    sys.exit(app.exec_())
