from flask import Flask, render_template, jsonify
import random
from pokeneas import pokeneas
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/pokenea_json')
def get_random_pokenea():
    random_pokenea = random.choice(pokeneas)
    return jsonify({
        "id": random_pokenea["id"],
        "nombre": random_pokenea["nombre"],
        "altura": random_pokenea["altura"],
        "habilidad": random_pokenea["habilidad"],
        "id_contenedor": id(app)
    })

@app.route('/pokenea')
def get_random_pokenea_info():
    random_pokenea = random.choice(pokeneas)
    return render_template('home.html', pokenea=random_pokenea, id_contenedor=id(app))


if __name__ == '__main__':
    app.run(host='34.121.143.117', port=80)


