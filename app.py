from flask import Flask, render_template, request

app = Flask(__name__)

import requests
from colorama import Fore
import json

api_key = "a1fae6b7d2a2b889201b347f693c3940"

@app.route('/', methods=['GET', 'POST'])

def index ():
    city = request.form.get('city')

    if city:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            temp = data['main']['temp']
            desc = data['weather'][0]['description']

            icon = data['weather'][0]['icon']
            image_url = f'https://openweathermap.org/img/wn/{icon}@2x.png'

            temp_celsius = temp - 273.15
            temp_celsius_arredondado = round(temp_celsius)

            return render_template('index.html', cidade=city, temperatura=temp_celsius_arredondado, descricao=desc, imagem_url=image_url)
        else:
            return render_template('index.html', erro='Erro para conseguir os dados de clima')
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run()