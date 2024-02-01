import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/home')
def home():

    # api_key = "2ca5630c7892ba8104791e904382120d"
    # city = "Zadar"
    # url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&lang=hr&appid={api_key}"
    #
    # return requests.get(url).json()

    return render_template("home.html")


if __name__ == '__main__':
    app.run()
