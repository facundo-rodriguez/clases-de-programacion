#3.- Sistema de estadísticas de votos.
#El partido de Tres de Febrero esta dividido en tres secciones: norte, sur y centro. 
#El sistema debe solicitar el total de personas que están habilitadas a votar para cada sección.  
#Una vez ingresados el total de votantes, se debe ingresar la cantidad de personas que realmente fueron a votar.
#El sistema debe mostrar por pantalla, la cantidad y el porcentaje de votantes asistentes por cada sector.
#Restricciones: La cantidad de personas que fueron a votar no puede ser negativo ni mayor a la cantidad habilitada

#entrada: 
        # N ingresar habilitados para votar en:norte
        # C ingresar habilitados para votar en:centro
        # S ingresar habilitados para votar en:sur

        #VN ingresar los que votaron en:norte
        #VC ingresar los que votaron en:centro
        #VS ingresar los que votaron en:sur

#proceso:
        #evaluar si lo ingresado es valido. NO PUEDEN SER NEGATIVOS.
        #N,C,S deben ser mayor o igual a 0, sino que se ingresen otra vez
        #VN,VC,VS deben ser menor o igual a N,C,S pero mayor o igual que 0, sino que lo ingrese otra vez
        #


bandera=True

HNor=int(input("ingrese el numero de habilitados para votar en Norte"))
HCen=int(input("ingrese el numero de habilitados para votar en Centro"))
HSur=int(input("ingrese el numero de habilitados para votar en Sur"))

while(HNor<0 or HCen<0 or HSur<0):
    
    print("lo ingresado esta mal, intente nuevamente")

    HNor=int(input("ingrese el numero de habilitados para votar en Norte"))
    HCen=int(input("ingrese el numero de habilitados para votar en Centro"))
    HSur=int(input("ingrese el numero de habilitados para votar en Sur"))


VotNor=int(input("ingrese cuantos votaron en Norte"))
VotCen=int(input("ingrese cuantos votaron en Centro"))
VotSur=int(input("ingrese cuantos votaron en HSur"))

while( (VotNor>HNor or VotNor<0) or (VotCen>HCen or VotCen<0) or (VotSur>HSur or VotSur<0)):
    
    print("lo ingresado esta mal, ingrese nuevamente cuantos votaron en cada zona")

    VotNor=int(input("ingrese cuantos votaron en Norte"))
    VotCen=int(input("ingrese cuantos votaron en Centro"))
    VotSur=int(input("ingrese cuantos votaron en Sur"))


PorcentajeNor=(VotNor*100)/HNor
PorcentajeCen=(VotCen*100)/HCen
PorcentajeSur=(VotSur*100)/HSur


print(f"En la zona Norte votaron {VotNor}, es decir el {PorcentajeNor}%")
print(f"En la zona Norte votaron {VotCen}, es decir el {PorcentajeCen}%")
print(f"En la zona Norte votaron {VotSur}, es decir el {PorcentajeSur}%")