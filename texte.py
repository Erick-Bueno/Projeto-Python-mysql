from PyQt5 import QtWidgets
from PyQt5 import uic   



app = QtWidgets.QApplication([])
projetoo = uic.loadUi("untitled.ui")

app.exec()
projetoo.show()