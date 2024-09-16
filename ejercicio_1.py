import sys 
from PyQt5.QtWidgets import*
from PyQt5.QtCore import *

class VentanV(QWidget):
    def __init__(self):
        super().__init__()
        self.InicializarV()#inicializa la ventana
        
    def InicializarV(self):
        self.setGeometry(230, 230, 230, 230)
        self.setWindowTitle("Ejercicio-1")
        #para mostrar los datos 
        self.nombre = QLabel("Alfredo Ezequiel", self)
        self.apellido = QLabel("Medrano Martinez", self)
        self.edad = QLabel("18", self)
        #alinean al centro los datos
        self.nombre.setAlignment(Qt.AlignCenter)
        self.apellido.setAlignment(Qt.AlignCenter)
        self.edad.setAlignment(Qt.AlignCenter)
        ventana = QVBoxLayout()
       
        ventana.addWidget(self.nombre)
        ventana.addWidget(self.apellido)
        ventana.addWidget(self.edad)
        
        self.setLayout(ventana)
        
        self.show()
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanV()
    sys.exit(app.exec_())
    