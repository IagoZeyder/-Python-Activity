import sys
import time
from tkinter.ttk import Progressbar
from PyQt5 import uic, QtWidgets

explicar = True
def explicacao():
    global explicar
    if explicar == True:
        explicar = False                         
        formAtv_3.textBrowser.setStyleSheet("background-color: white; border-radius: 40px; font-size: 18pt; opacity: 100%;")                           
        formAtv_3.textBrowser.setText('Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.')                    
        formAtv_3.textBrowser.resize(500, 200)                                                                      
        explicar = False
    else:             
        limpar_Brower() 
        explicar = True
        formAtv_3.textBrowser.resize(0, 0)         
def limpar_Brower():
    formAtv_3.textBrowser.clear()

def comecar():    
    contador = int(0)
    while contador < 10:
        formAtv_3.close()
        loading.show()
        loading.progressBar.setValue(1)
        contador += 1
    else:
        formAtv_3_1.show()
        loading.close()

def voltar_3():
    formAtv_3_1.close()
    formAtv_3.show()

def verificar():
    sexo = formAtv_3_1.digitaVerificar.text()
    print('ola ')
    if sexo.upper() == 'F':
        formAtv_3_1.resposta.setStyleSheet("font-size: 25px; color:white; text-align: center;")
        formAtv_3_1.resposta.setText('Você escolheu o sexo feminino') 
    elif sexo.upper() == 'M':
        formAtv_3_1.resposta.setStyleSheet("font-size: 25px; color:white; text-align: center;")
        formAtv_3_1.resposta.setText('Você escolheu o sexo masculino') 
    else:
        formAtv_3_1.resposta.setStyleSheet("font-size: 25px; color:white;")
        formAtv_3_1.resposta.setText('              
        valor invalido')
        formAtv_3_1.digitaVerificar.clear()


app=QtWidgets.QApplication([])
formAtv_3=uic.loadUi("interface_3.ui")
formAtv_3_1=uic.loadUi("interface_3.1.ui")
loading=uic.loadUi("loading.ui")
formAtv_3.btnExplicacao.clicked.connect(explicacao)
formAtv_3_1.btnVoltar.clicked.connect(voltar_3)
formAtv_3_1.btnVerificar.clicked.connect(verificar)
formAtv_3.btnComecar.clicked.connect(comecar)
formAtv_3.show()
app.exec()