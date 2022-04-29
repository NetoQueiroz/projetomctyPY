from os import sep
# from PyQt5 import *
from PyQt5 import uic,QtWidgets
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QLineEdit, QToolTip, QTextEdit, QFrame, QPlainTextEdit
from PyQt5.QtGui import QPixmap
import webbrowser


""" ------- Links SCRIPTS ------- """
def scriptusertemp():
    webbrowser.open('https://drive.google.com/file/d/1MlyG-tjftRzs8pr1FPhAcyPGOjkuIpkg/view?usp=sharing')

def pmwin7(self):
    webbrowser.open('https://drive.google.com/file/d/12FRMMB8uptB4DnRQY5CZBg0J3MUxqivt/view?usp=sharing')

def pmwin10(self):
    webbrowser.open('https://drive.google.com/file/d/1OkQ4hmaVCa0fQ-_BU5ClfILYJEQSDP2c/view?usp=sharing')

def sicredwin7(self):
    webbrowser.open('https://drive.google.com/file/d/1lBg-8fyXXXNEr-ImfpiGLnYrPAdXYpPB/view?usp=sharing')
    
def pifpafwin7(self):
    webbrowser.open('https://drive.google.com/file/d/12SI8O1Zz6DlmbHZWgiDIz7dCXR1-UFZC/view?usp=sharing')
    
def pifpafwin10(self):
    webbrowser.open('https://drive.google.com/file/d/1rSgl9EMtKYpBdS8wEkJ8yQoMjN-qKCRQ/view?usp=sharing')
    

""" ------- Links SCRIPTS ------- """


def telaimpre():
    telaimpressora.show()

def telanobre():
    telaNOBREAK.show()

def telaleit():
    telaLEITORES.show()

def telaswit():
    telaSWITCH.show()

def teladesk():
    telaDESKTOP.show()

def telanote():
    telaNOTEBOOK.show()

def telaso():
    telaSO.show()

def telamoni():
    telaMONITOR.show()

def telaini():
    telainicial.show()

def telatriag():
    telatriagem.show()

def telaacomp():
    telacompanhamento.show()

def telarelatoriotriag():
    relatoriotriagem.show()

def telascript():
    telascripts.show()

def telarelatorioacomp():
    relatorioacompanhamento.show()

   

def botao_gerar():
    conteudo = telatriagem.numloja.text()
    numloja = int(conteudo)
    telatriagem.numloja.setText("")
    

    def calcula():

            ip_loja = numloja            
            ip_final = 'XX'
            ip_padrao = 172

            if ip_loja >= 1:

                if ip_loja <= 255:
                    ip_fx = 17
                    ipfinal = str(f'{ip_padrao}.{ip_fx}.{ip_loja}.{ip_final}')
                    telatriagem.label_iploja.setText(ipfinal)

                elif ip_loja >= 256 and ip_loja <= 510:
                    ip_fx = 18
                    ip_loja = ip_loja - 255
                    ipfinal = str(f'{ip_padrao}.{ip_fx}.{ip_loja}.{ip_final}')
                    telatriagem.label_iploja.setText(ipfinal)
                    
                elif ip_loja >= 511 and ip_loja <= 765:
                    ip_fx = 19
                    ip_loja = ip_loja - 510
                    ipfinal = str(f'{ip_padrao}.{ip_fx}.{ip_loja}.{ip_final}')
                    telatriagem.label_iploja.setText(ipfinal)
                    

                elif ip_loja >= 766 and ip_loja <= 1020:
                    ip_fx = 20
                    ip_loja = ip_loja - 765
                    ipfinal = str(f'{ip_padrao}.{ip_fx}.{ip_loja}.{ip_final}')
                    telatriagem.label_iploja.setText(ipfinal)
                    

                elif ip_loja >= 1021 and ip_loja <= 1275:
                    ip_fx = 21
                    ip_loja = ip_loja - 1020
                    ipfinal = str(f'{ip_padrao}.{ip_fx}.{ip_loja}.{ip_final}')
                    telatriagem.label_iploja.setText(ipfinal)
                    

                elif ip_loja >= 1276 and ip_loja <= 1530:
                    ip_fx = 22
                    ip_loja = ip_loja - 1275
                    ipfinal = str(f'{ip_padrao}.{ip_fx}.{ip_loja}.{ip_final}')
                    telatriagem.label_iploja.setText(ipfinal)
                    

                elif ip_loja >= 1531 and ip_loja <= 1785:
                    ip_fx = 23
                    ip_loja = ip_loja - 1530
                    ipfinal = str(f'{ip_padrao}.{ip_fx}.{ip_loja}.{ip_final}')
                    telatriagem.label_iploja.setText(ipfinal)
                
                elif ip_loja >= 1786 and ip_loja <= 2040:
                    ip_fx = 24
                    ip_loja = ip_loja - 1785
                    ipfinal = str(f'{ip_padrao}.{ip_fx}.{ip_loja}.{ip_final}')
                    telatriagem.label_iploja.setText(ipfinal)
                
                else:
                    ipfinal = 'loja inválida'
                    telatriagem.label_iploja.setText(ipfinal)
                
                

    calcula() 


def botao_gerar_acomp():
    conteudo = telacompanhamento.numloja.text()
    numloja = int(conteudo)
    telacompanhamento.numloja.setText("")
    

    def calcula():

            ip_loja = numloja            
            ip_final = 'XX'
            ip_padrao = 172

            if ip_loja >= 1:

                if ip_loja <= 255:
                    ip_fx = 17
                    ipfinal = str(f'{ip_padrao}.{ip_fx}.{ip_loja}.{ip_final}')
                    telacompanhamento.label_iploja.setText(ipfinal)

                elif ip_loja >= 256 and ip_loja <= 510:
                    ip_fx = 18
                    ip_loja = ip_loja - 255
                    ipfinal = str(f'{ip_padrao}.{ip_fx}.{ip_loja}.{ip_final}')
                    telacompanhamento.label_iploja.setText(ipfinal)
                    
                elif ip_loja >= 511 and ip_loja <= 765:
                    ip_fx = 19
                    ip_loja = ip_loja - 510
                    ipfinal = str(f'{ip_padrao}.{ip_fx}.{ip_loja}.{ip_final}')
                    telacompanhamento.label_iploja.setText(ipfinal)
                    

                elif ip_loja >= 766 and ip_loja <= 1020:
                    ip_fx = 20
                    ip_loja = ip_loja - 765
                    ipfinal = str(f'{ip_padrao}.{ip_fx}.{ip_loja}.{ip_final}')
                    telacompanhamento.label_iploja.setText(ipfinal)
                    

                elif ip_loja >= 1021 and ip_loja <= 1275:
                    ip_fx = 21
                    ip_loja = ip_loja - 1020
                    ipfinal = str(f'{ip_padrao}.{ip_fx}.{ip_loja}.{ip_final}')
                    telacompanhamento.label_iploja.setText(ipfinal)
                    

                elif ip_loja >= 1276 and ip_loja <= 1530:
                    ip_fx = 22
                    ip_loja = ip_loja - 1275
                    ipfinal = str(f'{ip_padrao}.{ip_fx}.{ip_loja}.{ip_final}')
                    telacompanhamento.label_iploja.setText(ipfinal)
                    

                elif ip_loja >= 1531 and ip_loja <= 1785:
                    ip_fx = 23
                    ip_loja = ip_loja - 1530
                    ipfinal = str(f'{ip_padrao}.{ip_fx}.{ip_loja}.{ip_final}')
                    telacompanhamento.label_iploja.setText(ipfinal)
                
                elif ip_loja >= 1786 and ip_loja <= 2040:
                    ip_fx = 24
                    ip_loja = ip_loja - 1785
                    ipfinal = str(f'{ip_padrao}.{ip_fx}.{ip_loja}.{ip_final}')
                    telacompanhamento.label_iploja.setText(ipfinal)
                
                else:
                    ipfinal = 'loja inválida'
                    telacompanhamento.label_iploja.setText(ipfinal)
                
                

    calcula() 






app = QtWidgets.QApplication([])
telainicial = uic.loadUi("telainicial.ui")
telatriagem = uic.loadUi("telaTRIAGEM.ui")
telacompanhamento = uic.loadUi("telaACOMPANHAMENTO.ui")
relatoriotriagem = uic.loadUi("telarelatoriotriagem.ui")
relatorioacompanhamento = uic.loadUi("telarelatorioacompanhamento.ui")
telascripts = uic.loadUi("telascripts.ui")
telaimpressora = uic.loadUi("telaIMPRESSORA.ui")
telaMONITOR = uic.loadUi("telaMONITOR.ui")
telaNOBREAK = uic.loadUi("telaNOBREAK.ui")
telaLEITORES = uic.loadUi("telaLEITOR.ui")
telaSWITCH = uic.loadUi("telaSWITCH.ui")
telaDESKTOP = uic.loadUi("telaDESKTOP.ui")
telaNOTEBOOK = uic.loadUi("telaNOTEBOOK.ui")
telaSO = uic.loadUi("telaSO.ui")


#comandos botões da primeira tela
telainicial.btn_triagem.clicked.connect(telatriag)
telainicial.btn_triagem.clicked.connect(telainicial.close)
telainicial.btn_acompanhamento.clicked.connect(telaacomp)
telainicial.btn_acompanhamento.clicked.connect(telainicial.close)

#comandos da tela triagem
telatriagem.btn_relatorios.clicked.connect(telarelatoriotriag)
telatriagem.btn_relatorios.clicked.connect(telatriagem.close)
telatriagem.btn_voltar.clicked.connect(telatriagem.close)
telatriagem.btn_voltar.clicked.connect(telaini)
telatriagem.btn_gerar.clicked.connect(botao_gerar)
telatriagem.btn_script.clicked.connect(telascript)


#comandos da tela acompanhamento
telacompanhamento.btn_relatorios.clicked.connect(telarelatorioacomp)
telacompanhamento.btn_relatorios.clicked.connect(telacompanhamento.close)
telacompanhamento.btn_voltar.clicked.connect(telacompanhamento.close)
telacompanhamento.btn_voltar.clicked.connect(telaini)
telacompanhamento.btn_gerar.clicked.connect(botao_gerar_acomp)
telacompanhamento.btn_script.clicked.connect(telascript)


#comandos da tela de relatorios da triagem
relatoriotriagem.btn_voltar.clicked.connect(relatoriotriagem.close)
relatoriotriagem.btn_voltar.clicked.connect(telatriag)
relatoriotriagem.btn_usuariotemp.clicked.connect(scriptusertemp)
relatoriotriagem.btn_impressora.clicked.connect(telaimpre)
telaimpressora.btn_voltar.clicked.connect(telaimpressora.close)#btn voltar FALHAS
relatoriotriagem.btn_monitor.clicked.connect(telamoni)
telaMONITOR.btn_voltar.clicked.connect(telaMONITOR.close)#btn voltar FALHAS
relatoriotriagem.btn_nobreak.clicked.connect(telanobre)
telaNOBREAK.btn_voltar.clicked.connect(telaNOBREAK.close)#btn voltar FALHAS
relatoriotriagem.btn_leitores.clicked.connect(telaleit)
telaLEITORES.btn_voltar.clicked.connect(telaLEITORES.close)#btn voltar FALHAS
relatoriotriagem.btn_switch.clicked.connect(telaswit)
telaSWITCH.btn_voltar.clicked.connect(telaSWITCH.close)#btn voltar FALHAS
relatoriotriagem.btn_desktop.clicked.connect(teladesk)
telaDESKTOP.btn_voltar.clicked.connect(telaDESKTOP.close)#btn voltar FALHAS
relatoriotriagem.btn_notebook.clicked.connect(telanote)
telaNOTEBOOK.btn_voltar.clicked.connect(telaNOTEBOOK.close)#btn voltar FALHAS
relatoriotriagem.btn_so.clicked.connect(telaso)
telaSO.btn_voltar.clicked.connect(telaSO.close)#btn voltar FALHAS



#comandos da tela de relatorios acompanhamento
relatorioacompanhamento.btn_voltar.clicked.connect(relatorioacompanhamento.close)
relatorioacompanhamento.btn_voltar.clicked.connect(telaacomp)

#comandos telas scripts
telascripts.btn_voltar.clicked.connect(telascripts.close)
telascripts.btn_pmwin7.clicked.connect(pmwin7)
telascripts.btn_pmwin10.clicked.connect(pmwin10)
telascripts.btn_sicredwin7.clicked.connect(sicredwin7)
telascripts.btn_pifpafwin7.clicked.connect(pifpafwin7)
telascripts.btn_pifpafwin10.clicked.connect(pifpafwin10)

telainicial.show()
app.exec()