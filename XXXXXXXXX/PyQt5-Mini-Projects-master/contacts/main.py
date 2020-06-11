import os
import json

from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication([])
dlg = uic.loadUi('main.ui')


def addContacts():
    while dlg.name.text() and dlg.num.text() == "":
        # name = str(dlg.name.text())
        # number = str(dlg.num.text())
        dlg.results.addItem(str(dlg.name.text()))
        # dlg.result.addItem(str(dlg.num.text()))

        # dlg.num.setText("")
        #
    with open('data.json', 'r') as file:
        data = json.load(file)

    data['items'] = [dlg.name.text()]
    with open('data.json', 'w') as file:
        json.dump(data, file)

    dlg.name.setText("")


def read():
    with open('data.json', 'r') as file:
        data = json.load(file)

    for items in data['items']:
        print(items)
        dlg.results.addItem(items)


if __name__ == '__main__':
    read()

dlg.pushButton.clicked.connect(addContacts)

dlg.show()
app.exec()

os._exit()
