from PyQt5 import uic, QtWidgets

def teste():
    print("OLA MUNDO")


app = QtWidgets.QApplication([])
projeto = uic.loadUi("projetoo.ui")


projeto.show()
app.exec()