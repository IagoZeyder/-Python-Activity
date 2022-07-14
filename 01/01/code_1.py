from PyQt5 import uic, QtWidgets

def maiorNum ():  
    numero1 = int(formAtv1.lineEdit1.text())     
    numero2 = int(formAtv1.lineEdit2.text())
    if numero1 > numero2:
        print("O maior númeero é o: ", numero1)
        formAtv1.maiorNum.setText(str(numero1))
    elif numero2 > numero1:        
        print("O maior número é o: ", numero2)
        formAtv1.maiorNum.setText(str(numero2))

app=QtWidgets.QApplication([])
formAtv1=uic.loadUi("interface.ui")
formAtv1.mostrar.clicked.connect(maiorNum)
formAtv1.show()
app.exec()
