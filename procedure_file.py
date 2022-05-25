from dbfread import DBF

def readDBF(hour, ruta):

    try:
        table = DBF(ruta)
        salesTotal = 0
        transTotal = 0

        for record in table:
            if(record['TYPE'] == 31):
                if(record['OPENHOUR'] < int(hour)):
                    salesTotal += record['AMOUNT']
                    transTotal += 1

        result = {
            "salesTotal":   salesTotal, 
            "transTotal":   transTotal,  
        }

        return result
    except:
        return {}