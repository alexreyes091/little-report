import datetime
from data import datos, restaurantes, ruta
from procedure_ip import isIpActive
from procedure_file import readDBF 

def setDate(reportType, initDate, finalDate, weekDate):
    # Nombre de la tabla a leer
    nameDbf = '\GNDSALE.Dbf'
    # Control de fechas a formato de Aloha
    today = datetime.datetime.now()
    newMonth = today.month if today.month >= 10 else '0' + str(today.month)
    newToday = str(today.year) + str(newMonth) + str(today.day)
    initDate = 'DATA' if (newToday == initDate) else initDate

    #1. Crear ruta de busqueda
    for rest in restaurantes:
        isIpActive(rest, rest['ip'])
        if(rest['status'] == 1):
            rutaInitDate = '\\\\' + rest['ip'] + ruta['pathDate'] + initDate + nameDbf
            rutaFinalDate = '\\\\' + rest['ip'] + ruta['pathDate'] + finalDate + nameDbf
            rutaWeekDate = '\\\\' + rest['ip'] + ruta['pathDate'] + weekDate + nameDbf
                
            #2. Obtener datos de las fechas solicitadas.
            resultInitDate = readDBF(reportType, rutaInitDate)
            resultFinalDate = readDBF(reportType, rutaFinalDate)
            resultWeekDate = readDBF(reportType, rutaWeekDate)
            
            #3. Mandar datos al objeto
            result = {
                "rest": rest['rest'],
                "value": {
                    "initDate": resultInitDate,
                    "finalDate": resultFinalDate,
                    "weekDate": resultWeekDate
                }
            }
            datos.append(result)
        else: 
            #3. Mandar datos vacios al objeto cuando no detecta la IP
            result = {
                "rest": rest['rest'],
                "value": {
                    "initDate": {},
                    "finalDate": {},
                    "weekDate": {}
                }
            }
            datos.append(result)