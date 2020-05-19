import sys
from PyQt5.QtWidgets import *

if __name__ == "__main__":
    app = QApplication(sys.argv)

    model = QDirModel()
    tree = QTreeView()
    tree.setModel(model)
    tree.setWindowTitle('File Tree View')
    tree.resize(600, 400)
    tree.show()
    sys.exit(app.exec_())