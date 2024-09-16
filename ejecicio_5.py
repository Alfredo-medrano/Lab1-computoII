import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import*

class VentanaPe(QWidget):
    def __init__(self):
        super().__init__()
        self.Personas()

    def Personas(self):
        self.setWindowTitle("Ejercicio-5")
        self.setGeometry(200,200, 350, 500)
        Vp = QVBoxLayout()
       #donde se van a almacenar las entradas
        self.datosPersona = []
        #lisat de datos personales
        campos = ["Nombre", "Apellido", "Edad", "Direccion", "Ciudad", 
                  "Pais", "Telefono", "Correo", "Ocupacion", "Fecha de Nacimiento"]
        #campos de entrada para los datos personales
        for campo in campos:
            Vp.addWidget(QLabel(campo))
            entrada = QLineEdit(self)
            entrada.setPlaceholderText(campo)
            #se valida si la longitud de los campos y que solo se permita de tipo entero
            if campo == "Edad":
                entrada.setValidator(QIntValidator())
                entrada.setMaxLength(3)
            elif campo == "Telefono":
                entrada.setValidator(QIntValidator())
                entrada.setMaxLength(8)
            Vp.addWidget(entrada)
            #guarda el campo en la lista
            self.datosPersona.append(entrada)
            #para mostra los datos al darle click
        self.boton = QPushButton("Mostrar Datos", self)
        self.boton.clicked.connect(self.DT)
        Vp.addWidget(self.boton)
        self.setLayout(Vp)
    #cuandro para mostar los datos ingresados
    def DT(self):
        perDT = QMessageBox(self)
        perDT.setWindowTitle("Datos ingresadsos")
        DtS = ""
        for campo in self.datosPersona:
            DtS+=f"{campo.placeholderText()}: {campo.text()}\n"
            """ print(f"{campo.placeholderText()}: {campo.text()}") """
            perDT.setText(DtS)
            perDT.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaPe()
    ventana.show()
    sys.exit(app.exec_())