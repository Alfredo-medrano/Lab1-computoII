import sys
from PyQt5.QtWidgets import*
from PyQt5.QtCore import *

class Vcontra(QWidget):
    def __init__(self):
        super().__init__()
        self.InicioV()
    def InicioV(self):
        self.setGeometry(100,100,300,150)
        self.setWindowTitle("Ejercicio-2")
        #campos para ingresar la contraseña 
        self.Icontra = QLabel("Ingrese la contraseña: ", self)
        self.Ccontraseña = QLineEdit(self)
        self.Ccontraseña.setEchoMode(QLineEdit.Password)
        #para que se pueda ver la contraseña 
        self.Mostrarc = QCheckBox("Mostrar contraseña", self)
        self.Mostrarc.stateChanged.connect(self.MostrarC)
        ventanaC = QVBoxLayout()
        ventanaC.addWidget(self.Icontra)
        ventanaC.addWidget(self.Ccontraseña)
        ventanaC.addWidget(self.Mostrarc)
        self.setLayout(ventanaC)
        self.show()
    def MostrarC(self,Contra):
        #Cambia el modo de la contraseañ segun como este el checkbox
        if Contra == Qt.Checked:
            self.Ccontraseña.setEchoMode(QLineEdit.Normal)
        else:
            self.Ccontraseña.setEchoMode(QLineEdit.Password)
            
    
        
if __name__ == '__main__':
    App =  QApplication(sys.argv)
    ventana = Vcontra()
    sys.exit(App.exec())
    
        