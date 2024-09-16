import sys
from PyQt5.QtWidgets import*
from PyQt5.QtCore import*

class ventanaC(QWidget):
    def __init__(self):
        super().__init__()
        #lista qie se mostrara en la ventana
        self.Agregados = ["Cedula: 1243760 ", "Nombre: Alfredo Ezequiel Medrano Martinez" ]
        self.UI()
    def UI(self):
        self.setGeometry(100, 100, 300, 100)
        self.setWindowTitle("Ejercicio_3")
        #se crea el nombre para la lista
        self.Aggdos = QLabel("Agregados ", self)
        #se centran los elementos
        self.Aggdos.setAlignment(Qt.AlignCenter)
        self.lista = QListWidget(self)
        #para que este oculta 
        self.lista.hide()
        #se crea un boton para que al darle click se muestre la lsita
        self.btnmostrar = QPushButton("Mostrar", self)
        self.btnmostrar.clicked.connect(self.Mostrar)   
        
        VentanaCre = QVBoxLayout()
        VentanaCre.addWidget(self.Aggdos)
        VentanaCre.addWidget(self.lista)
        VentanaCre.addWidget(self.btnmostrar)
        self.setLayout(VentanaCre)
        
    def Mostrar(self):
        #para mostrar la lsta si esta no se ve
        if not self.lista.isVisible():
            for agregados in self.Agregados:
                self.lista.addItem(agregados)
            self.lista.show()

            
          

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = ventanaC()
    ventana.show()
    sys.exit(app.exec_())
    