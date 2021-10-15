

class personas:

    def __init__(self,nombre,apellido,dni):
        
        self.nombre=nombre
        self.apellido=apellido
        self.dni=dni
        self.mayor=False
        self.trabajo=False

    
    def definir_mayor(self):
        
        edad=int(input("ingrese la edad de la persona"))

        if(edad>=18):
            self.mayor=True
        
        else:
            self.mayor=False

    
    def estado(self):

        if(self.mayor==True):
            print("la persona es mayor de edad")


        else:
            print("la persona es menor de edad")


    def definir_trabajo(self):

        if(self.trabajo==True):
            print("lanpersona tiene trabajo")

        else:
            print("la persona no tiene trabajo")






ing_nombre=input("ingrese el nombre: ")
ing_apellido=input("ingrese el apellido: ")
ing_dni=input("ingrese el dni: ")

#si el constructor tiene parametros si o is al momento de crear
#el objeto le tengo que pasar los valores.
objeto1=personas(ing_nombre, ing_apellido, ing_dni)
objeto1.definir_mayor()

objeto1.estado()