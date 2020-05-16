'''

扩展的表格控件（QTableWidget）
QTableView

每一个Cell（单元格）是一个QTableWidgetItem

'''

import sys
from PyQt5.QtWidgets import (QWidget, QTableWidget, QHBoxLayout, QApplication, QTableWidgetItem, QAbstractItemView)
from PyQt5.QtGui import QBrush, QColor, QFont

class TableWidgetDemo(QWidget):
    def __init__(self):
        super(TableWidgetDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QTableWidget演示")
        self.resize(430, 230);
        layout = QHBoxLayout()
        tablewidget = QTableWidget()
        tablewidget.setRowCount(4)
        tablewidget.setColumnCount(3)

        layout.addWidget(tablewidget)

        tablewidget.setHorizontalHeaderLabels(['id', 'name', 'age'])
        nameItem = QTableWidgetItem("1")
        nameItem.setFont(QFont('Times',14,QFont.Black))
        nameItem.setForeground(QBrush(QColor(255,0,0)))
        tablewidget.setItem(0, 0, nameItem)

        ageItem = QTableWidgetItem("Tom")
        ageItem.setForeground(QBrush(QColor(255,255,0)))
        ageItem.setBackground(QBrush(QColor(0,0,255)))
        tablewidget.setItem(0, 1, ageItem)

        jgItem = QTableWidgetItem("21")
        jgItem.setFont(QFont('Times',20,QFont.Black))
        jgItem.setForeground(QBrush(QColor(0,0,255)))
        tablewidget.setItem(0, 2, jgItem)

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = TableWidgetDemo()
    example.show()
    sys.exit(app.exec_())
