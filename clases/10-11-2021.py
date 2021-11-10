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
    carrera=[ ["sistemas",3,10], ["comunicacion",4,15], ["derecho",5,20], ["medicina",6,25] ]
    porcentaje=""

    
    def años_cursada(self):

        opcion=input("seleccionar carrera: ")
        
        for i in range(len(self.carrera)):
          
          if(opcion==self.carrera[i][0]):
            
            print("la cantidad de años de cursada de la carrera ", opcion, " son ",self.carrera[i][1], "años")


    def terminar_carrera(self,carrera,materias):

        for i in range(len(self.carrera)):
            if(carrera==self.carrera[i][0]):
                materias_cursada=self.carrera[i][2]

        
        if(materias==materias_cursada):
            print("el alumno termino la carrera")
        
        else:

            if(materias<materias_cursada):

                materias_faltantes=materias_cursada-materias_cursada

                print("al alumno le faltan ",materias_faltantes," materias para terminar la carrera.")
            
            else:
                print("imposible")


        

objeto=alumno()

print(objeto.años_cursada())

