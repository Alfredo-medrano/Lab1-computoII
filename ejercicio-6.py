import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class CalculadorPrecio:
    #se define la cantidad,tarifa y transacciones
    def __init__(self):
        self.tarifa_diaria = 0
        self.cantidad = 0
        self.transaccion = ""

    def precioNase(self, modelo):
        #tarifa diaria y precio de compra 
        if modelo == "Sedán":
            self.tarifaDiaria = 30
            self.precioCompra = 20000
        elif modelo == "SUV":
            self.tarifaDiaria = 35
            self.precioCompra = 30000
        elif modelo == "Camioneta":
            self.tarifaDiaria = 40
            self.precioCompra = 50000
        else:
            raise ValueError("Modelo no válido.")

    def Acantidad(self, cantidad):
        #verifica que la cantidad de vehiculos sea correcta
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva.")
        self.cantidad = cantidad

    def Atransaccion(self, transaccion):
        #verifica si se selecciona alquilar o comprar
        if transaccion not in ["Alquilar", "Comprar"]:
            raise ValueError("Tipo de transacción no válido.")
        self.transaccion = transaccion

    def calcularPrecio(self):
        #calcula el precio de la transaccion y calcula dependiendo si es alquiler o renta
        if self.transaccion == "Alquilar":
            precioTotal = self.tarifaDiaria * self.cantidad * 30
            return f"Precio total de alquiler: ${precioTotal:.2f} por mes."
        elif self.transaccion == "Comprar":
            precioTotal = self.precioCompra * self.cantidad
            return f"Precio total de compra: ${precioTotal:.2f}."
        else:
            raise ValueError("Tipo de transacción no válido.")

class Concesionario(QWidget):
    #se llaman las instancias de precio y de la interfaz grafica
    def __init__(self):
        super().__init__()
        self.calculador = CalculadorPrecio()
        self.VentanaCS()

    def VentanaCS(self):
        self.setWindowTitle("Concesionario de Autos")
        self.setGeometry(100, 100, 400, 400)
        #Para seleccionar si alquilar o comprar
        ventanaC = QVBoxLayout()
        self.pagoT = QLabel("Selecciona tipo de transacción:")
        ventanaC.addWidget(self.pagoT)
        self.alquilar = QRadioButton("Alquilar", self)
        self.comprar = QRadioButton("Comprar", self)
        self.alquilar.toggled.connect(self.Atransaccion)
        self.comprar.toggled.connect(self.Atransaccion)
        ventanaC.addWidget(self.alquilar)
        ventanaC.addWidget(self.comprar)
        #seleccionar entre los tipos de veiculos 
        self.modelo = QLabel("Selecciona el modelo de automóvil:")
        ventanaC.addWidget(self.modelo)
        self.sedan = QRadioButton("Sedán - $30 por día", self)
        self.suv = QRadioButton("SUV - $35 por día", self)
        self.camioneta = QRadioButton("Camioneta - $40 por día", self)
        ventanaC.addWidget(self.sedan)
        ventanaC.addWidget(self.suv)
        ventanaC.addWidget(self.camioneta)
        #seleccionar color del automovil
        self.colorA = QLabel("Selecciona el color del automóvil:")
        ventanaC.addWidget(self.colorA)
        self.color = QComboBox(self)
        self.color.addItems(["Rojo", "Azul", "Negro", "Blanco", "Gris"])
        ventanaC.addWidget(self.color)
        #cantidad de automoviles que se pueden elegir max 10 
        self.cantidad = QLabel("Selecciona la cantidad:")
        ventanaC.addWidget(self.cantidad)
        self.cantidadA = QSpinBox(self)
        self.cantidadA.setRange(1, 10)  
        ventanaC.addWidget(self.cantidadA)
        #el boton para calcular, donde se llama a la funcion calcular precio
        self.btnCalcular = QPushButton("Calcular Precio", self)
        self.btnCalcular.clicked.connect(self.calcularPrecio)
        ventanaC.addWidget(self.btnCalcular)
        #se muestra el resultdado 
        self.resultado = QLabel("", self)
        ventanaC.addWidget(self.resultado)
        self.setLayout(ventanaC)

    def Atransaccion(self):
        #si se selecciona alquilar o comprar
        if self.alquilar.isChecked():
            self.calculador.Atransaccion("Alquilar")
        elif self.comprar.isChecked():
            self.calculador.Atransaccion("Comprar")

    def calcularPrecio(self):
        #calcula y muestra el precio basado en la seleccion hecha
        try:
            modelo = ""
            if self.sedan.isChecked():
                modelo = "Sedán"
            elif self.suv.isChecked():
                modelo = "SUV"
            elif self.camioneta.isChecked():
                modelo = "Camioneta"
            else:
                self.resultado.setText("Error: Selecciona un modelo de automóvil.")
                return

            cantidad = self.cantidadA.value()
            self.calculador.precioNase(modelo)
            self.calculador.Acantidad(cantidad)

            resultado = self.calculador.calcularPrecio()
            self.resultado.setText(resultado)
        except ValueError as e:
            self.resultado.setText(f"Error: {str(e)}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Concesionario()
    ventana.show()
    sys.exit(app.exec_())
