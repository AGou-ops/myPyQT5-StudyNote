'''

扩展的表格控件（QTableWidget）
QTableView

每一个Cell（单元格）是一个QTableWidgetItem

'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QBrush, QColor, QFont, QIcon
from PyQt5.QtCore import *


class TableWidgetDemo(QWidget):
    def __init__(self):
        super(TableWidgetDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QTableWidget演示")
        self.resize(430, 230);
        self.setGeometry(500, 300, 450, 280)
        layout = QHBoxLayout()
        tablewidget = QTableWidget()
        tablewidget.setRowCount(4)
        tablewidget.setColumnCount(4)

        layout.addWidget(tablewidget)

        tablewidget.setHorizontalHeaderLabels(['id', 'name', 'age', 'image'])
        nameItem = QTableWidgetItem("1")
        nameItem.setFont(QFont('Times', 14, QFont.Black))
        nameItem.setForeground(QBrush(QColor(255, 0, 0)))
        tablewidget.setItem(0, 0, nameItem)

        ageItem = QTableWidgetItem("Tom")
        # 设置文本在单元格中的位置
        ageItem.setTextAlignment(Qt.AlignLeft | Qt.AlignCenter)
        # 合并单元格，参数分别是行列位置，合并行的行数，列数
        tablewidget.setSpan(0, 0, 3, 1)
        # 改变单元格的宽度和高度，参数分别是行数和所要改变的宽度和高度
        tablewidget.setRowHeight(1, 300)
        tablewidget.setColumnWidth(2, 200)

        ageItem.setForeground(QBrush(QColor(255, 255, 0)))
        ageItem.setBackground(QBrush(QColor(0, 0, 255)))
        tablewidget.setItem(0, 1, ageItem)

        jgItem = QTableWidgetItem("21")
        # jgItem.setTextAlignment(Qt.AlignRight)
        jgItem.setTextAlignment(Qt.AlignRight | Qt.AlignBottom)
        jgItem.setFont(QFont('Times', 20, QFont.Black))
        jgItem.setForeground(QBrush(QColor(0, 0, 255)))
        tablewidget.setItem(0, 2, jgItem)

        imgItem = QTableWidgetItem(QIcon('/home/agou-ops/PycharmProjects/myPyQT5-StudyNote/imgs/test.jpg'), 'logo')
        imgItem.setFont(QFont('Times', 14, QFont.Black))
        imgItem.setForeground(QBrush(QColor(0, 0, 0)))
        tablewidget.setItem(0, 3, imgItem)

        newItem = QTableWidgetItem("2")
        tablewidget.setItem(3, 0, newItem)
        newItem = QTableWidgetItem("Tim")
        tablewidget.setItem(3, 1, newItem)
        newItem = QTableWidgetItem("23")
        tablewidget.setItem(3, 2, newItem)
        """
        tablewidget.setContextMenuPolicy(Qt.CustomContextMenu)
        tablewidget.customContextMenuRequested.connect(self.generateMenu)
        """
        # 禁止编辑
        # tablewidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 整行选择
        tablewidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        # 调整列和行
        tablewidget.resizeColumnsToContents()
        tablewidget.resizeRowsToContents()

        tablewidget.horizontalHeader().setVisible(True)
        #   tablewidget.verticalHeader().setVisible(False)

        tablewidget.setVerticalHeaderLabels(['1'])
        # 隐藏表格线
        tablewidget.setShowGrid(False)

        self.setLayout(layout)
"""
    def generateMenu(self, pos):
        print(pos)
        for i in self.tablewidget.selectionModel().selection().indexes():
            rowNum = i.row()
        # 如果选择的行索引小于2，弹出上下文菜单
        if rowNum < 2:
            menu = QMenu()
            item1 = menu.addAction("菜单项1")
            item2 = menu.addAction("菜单项2")
            item3 = menu.addAction("菜单项3")
            screenPos = self.tablewidget.mapToGlobal(pos)
            print(screenPos)
            # 被阻塞
            action = menu.exec(screenPos)
            if action == item1:
                print('选择了第1个菜单项',self.tablewidget.item(rowNum,0).text(),
                                        self.tablewidget.item(rowNum,1).text(),
                                        self.tablewidget.item(rowNum, 2).text())
            elif action == item2:
                print('选择了第2个菜单项',self.tablewidget.item(rowNum,0).text(),
                                        self.tablewidget.item(rowNum,1).text(),
                                        self.tablewidget.item(rowNum, 2).text())
            elif action == item3:
                print('选择了第3个菜单项',self.tablewidget.item(rowNum,0).text(),
                                        self.tablewidget.item(rowNum,1).text(),
                                        self.tablewidget.item(rowNum, 2).text())
            else:
                return
"""

if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = TableWidgetDemo()
    example.show()
    sys.exit(app.exec_())
