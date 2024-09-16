import sys
from PyQt5.QtWidgets import*

class MAscotas(QWidget):
    def __init__(self):
        super().__init__()
        self.VentanaM()

    def VentanaM(self):
        self.setGeometry(200, 200, 300, 200)
        self.setWindowTitle("Ejerecicio-4")
        VM = QVBoxLayout()
        #lista que donde se almacena la entrda de datos
        self.mascotas = [] 
        #se crean las entradas 
        for i in range(3):
            VM.addWidget(QLabel(f"Mascota {i+1}:"))
            
            nombre = QLineEdit(self)
            nombre.setPlaceholderText("Nombre")
            VM.addWidget(nombre)
            edad = QLineEdit(self)
            edad.setPlaceholderText("Edad")
            VM.addWidget(edad)
            tipo = QLineEdit(self)
            tipo.setPlaceholderText("Tipo (Ej: Perro, Gato)")
            VM.addWidget(tipo)
            #agregar datos a la lista
            self.mascotas.append((nombre, edad, tipo))

        #Boton para ver los datos ingresados 
        self.btnmostrar= QPushButton("Mostrar Dato", self)
        self.btnmostrar.clicked.connect(self.mostrarDatos)
        VM.addWidget(self.btnmostrar)
        self.setLayout(VM)


    def mostrarDatos(self):
        #se crea un recuadreo paramostrar los datos iingresados anteriormente
        mosDT = QMessageBox(self)
        mosDT.setWindowTitle("Datos ingresadsos")
        for i, mascota in self.mascotas:
            nombre = mascota[0].text()
            edad = mascota[1].text()
            tipo = mascota[2].text()
            mosDT.setText(mosDT.text() + f"Mascota {i+1}:\nNombre: {nombre}\nEdad: {edad}\nTipo: {tipo}\n\n")
            #muestra el cuadro del mensaje
            mosDT.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = MAscotas()
    ventana.show()
    sys.exit(app.exec_())

    