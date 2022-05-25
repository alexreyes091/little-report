from dbfread import DBF

def readDBF(ruta):

    try:
        table = DBF(ruta)
        salesTotal2PM = 0
        transTotal2PM = 0
        salesTotal6PM = 0
        transTotal6PM = 0
        salesTotal = 0
        transTotal = 0

        for record in table:
            if(record['TYPE'] == 31):
                if(record['OPENHOUR'] < 14):
                    salesTotal2PM += record['AMOUNT']
                    transTotal2PM += 1
                elif(record['OPENHOUR'] < 18):
                    salesTotal6PM += record['AMOUNT']
                    transTotal6PM += 1
                else:
                    salesTotal += record['AMOUNT']
                    transTotal += 1

        # Validamos la distribucion de venta en horas.
        salesTotal6PM += salesTotal2PM if salesTotal6PM !=0 else salesTotal6PM
        transTotal6PM += transTotal2PM if transTotal6PM !=0 else transTotal6PM
        
        # Validamos la distribucion de venta en horas.
        salesTotal += salesTotal6PM if salesTotal !=0 else salesTotal
        transTotal += transTotal6PM if transTotal !=0 else transTotal

        result = {
            "sales2PM":     salesTotal2PM,
            "sales6PM":     salesTotal6PM,
            "salesTotal":   salesTotal,
            "trans2PM":     transTotal2PM,
            "trans6PM":     transTotal6PM,  
            "transTotal":   transTotal,  
        }

        return result
    except:
        return {}