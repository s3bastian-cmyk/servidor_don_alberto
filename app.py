from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

# Base de datos en memoria
peritajes_db = [
    {"placa": "SCM-104", "estado": "cambio de aceite", "mecanico": "andres"},
    {"placa": "KJG-405", "estado": "ajuste de cadena", "mecanico": "carlos"}
]

@app.route('/api/repuestos', methods=['GET'])
def get_repuestos():
    return jsonify({
        "status": "online",
        "servidor": "Ubuntu de murcia",
        "repuestos_disponibles": ["Bujias de Iridio", "Filtro de aceite", "Aceite motul 7100"]
    })

@app.route('/api/registros', methods=['GET'])
def get_registros():
    inventario = ["Bujias de Iridio", "Filtro de aceite", "Aceite motul 7100"]
    hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return jsonify({
         "inventario": inventario,
         "servidor": "Ubuntu de murcia",
         "hora_servidor": hora_actual
    })

@app.route('/api/inventario', methods=['GET'])
def inventario():
    return jsonify({
        "repuestos": [
            "llantas",
            "baterias",
            "cascos"
        ]
    })

@app.route('/api/peritajes', methods=['GET', 'POST'])
def gestionar_peritajes():
    if request.method == 'POST':
         datos = request.get_json()
         if not datos or 'placa' not in datos:
             return jsonify({"error": "Falta la placa"}), 400
         
         nuevo_peritaje = {
             "placa": datos.get('placa').upper(),
             "estado": datos.get("estado", "ingresado"),
             "mecanico": datos.get("mecanico", "por asignar")
         }
         peritajes_db.append(nuevo_peritaje)
         return jsonify({"mensaje": "moto registrada con exito", "peritaje": nuevo_peritaje}), 201
    else:
         return jsonify(peritajes_db)

# El bloque de arranque SIEMPRE al final absoluto del archivo
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)