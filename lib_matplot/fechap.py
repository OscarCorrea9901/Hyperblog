import datetime as datetime
from datetime import datetime,timedelta
import calendar

#fecha = datetime.date(2022, 10, 25)
fecha = datetime.now()
dias = ["domingo","lunes","martes","miercoles","jueves","viernes","sabado"]
fecha = int(fecha.strftime("%w"))
dia = dias[fecha]
print(dia)

mes = datetime.now().month
año = datetime.now().year
#aux = aux.strftime("%B")
#print(aux)
if (datetime.now().day <= 15):
    dueDate = "15 de " + datetime.now().strftime("%B")
else:
    dueDate = str(calendar.monthrange(año,mes)[1]) + " de " + datetime.now().strftime("%B")
#print(dueDate)

valor = 1050342
valor_en_peso_format = '{:1,d}'.format(valor)
valor_en_texto ="$" + str(valor_en_peso_format).replace(',','.').replace(" ","")

print(valor_en_texto[0:10])