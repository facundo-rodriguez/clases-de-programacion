


class vehiculos():

    color=""
    largo=""
    motorizacion=""


    def __init__(self):
        
        self.ruedas=4
        self.prendido=False


    def arrancar(self):
        self.prendido=True

    def apagar(self):
        self.prendido=False


#el self reempleza el nombre del objeto

Auto1=vehiculos()
Auto1.color="Amarillo"

Auto2=vehiculos()
Auto2.color="Rojo"


Auto1.__ruedas=9

print(Auto1.prendido)

print(Auto1.__ruedas)





