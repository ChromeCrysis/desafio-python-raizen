from flask import Flask, jsonify
import requests
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

# Configurar a chave da API OpenWeatherMap
API_KEY = "5fd9ec63b1865d1bfa1f41bb1c0f1d9e"

# Configurar o cliente MongoDB
client = MongoClient('localhost', 27017)
db = client['weather_history']

@app.route('/weather/<city>', methods=['GET'])
def get_weather(city):
    # Verifica se os dados já estão no MongoDB
    weather_data = db.weather.find_one({'city': city})
    if weather_data:
        return jsonify(weather_data['forecast'])

    # Se não estiver, obter dados da API OpenWeatherMap
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&lang=pt_br"
    response = requests.get(url)
    data = response.json()

    # Salvar no MongoDB para consulta posterior
    if 'list' in data:
        forecast = data['list']
        db.weather.insert_one({'city': city, 'forecast': forecast, 'timestamp': datetime.utcnow()})

        return jsonify(forecast)
    else:
        return jsonify({'error': 'Não foi possível obter a previsão do tempo.'}), 500
    
@app.route('/weather/history', methods=['GET'])
def get_weather_history():
    history_data = list(db.weather.find({}, {'_id': 0}))

    return jsonify({'history': history_data})

@app.route('/weather/history/<city>', methods=['GET'])
def get_weather_history_city(city):
        weather_data = db.weather.find_one({'city': city})
        if weather_data:
            return jsonify(weather_data['forecast'])
        else:
            return jsonify({'error': 'Não foi possível obter a previsão do tempo.'}), 500

if __name__ == '__main__':
    app.run(debug=True)