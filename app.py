from flask import Flask, jsonify, request
from flask_cors import CORS
# -
from data import datos
from procedure import setDate

app = Flask(__name__)
CORS(app)

@app.route('/date', methods=['GET'])
def getDate():
    return (jsonify(datos))

@app.route('/date', methods=['POST'])
def date():
    #1. Recibimos las fechas.
    dates = {
        "initDate": request.json['initDate'],
        "finalDate": request.json['finalDate'],
        "weekDate": request.json['weekDate']
    }
    
    #2. Limpiamos el objeto para no arrastrar datos.
    datos.clear()
    
    #3. Enviamos a procesar las fechas.
    setDate(dates['initDate'], dates['finalDate'], dates['weekDate'])

    #4. Enviamos el resultado.
    return jsonify(datos)
    

if __name__ == '__main__':
    app.run(debug=True)