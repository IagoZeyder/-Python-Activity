from PyQt5 import uic, QtWidgets

def verificarNum():
    num = int(formAtv.lineEdit1.text())
    if num > 0 :
        formAtv.mostrar_2.setText(str(num))
    else:
        formAtv.mostrar_2.setText('É um número negativo')

app=QtWidgets.QApplication([])
formAtv=uic.loadUi("interface_2.ui")
formAtv.mostrar.clicked.connect(verificarNum)
formAtv.show()
app.exec()