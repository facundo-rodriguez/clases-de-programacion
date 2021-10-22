'''
escribir una clase llamada persona que tenga los atributos de nombre, 
apellido, dni, año de nacimiento.

La clase disponga de un metodo que informe si es mayor de edad

generar una clase alumno, hija de la clase persona. 
Como atributos debe tener al menos matricula, año de ingreso, 
carrera y porcentaje de materias aprobadas.
Debe informar cantidad de años de cursada.
Si el alumno termino la carrera, y un atributo de todos sus atributos


'''


class persona():

    nombre=""
    apellido=""
    dni=""
    nacimiento=""

    def mayor_edad(self):
        
        edad=int(input("ingrese su edad: "))

        if edad >= 18:
            print("es mayor de edad")

        else:
            print("es menor de edad")



class alumno(persona):
    pass

    matricula=""
    año_ingreso=""
    carrera=""
    porcentaje=""

    
    def años_cursada(self,años):
        
        print("el alumno lleva cursando ",años," años")





persona1=alumno()
persona1.años_cursada(2)
persona1.mayor_edad()
