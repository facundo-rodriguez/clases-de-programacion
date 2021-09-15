#Data una medida de tiempo expresada en horas, minutos y segundo con valores arbitrarios, 
#elabore un programa que transforme dicha medida en una expresión correcta. 
#Por ejemplo, dada la medida 3h 118m 195s, el programa deberá mostrar 5h 1m 15s.


horas_ingresados=int(input("ingrese la cantidad de horas"))
minutos_ingresados=int(input("ingrese la cantidad de minutos"))
segundos_ingresados=int(input("ingrese la cantidad de segundos"))



segundos_mostrar=segundos_ingresados%60 
#      15       =   196%60
minutos_ingresados= int(minutos_ingresados + ((segundos_ingresados-segundos_mostrar)/60))
#      121=                        118+     (( 195    -   15)/60)
minutos_mostrar=minutos_ingresados%60
#    1       =        121%60
horas_mostrar=int(horas_ingresados+((minutos_ingresados-minutos_mostrar)/60))
#   5   =         3           +   ((121-1)/60)


horas_resto=horas_mostrar%24

dias_mostrar=(horas_mostrar-horas_resto)/24

horas_mostrar=horas_mostrar

