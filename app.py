from flask import Flask, render_template, request, redirect
from api_handler import APIHandler  # Uvozimo APIHandler klasu iz vanjske datoteke

app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/weather", methods=["GET", "POST"])
def weather():
    data = None
    if request.method == "POST":
        api_class = APIHandler(request.form["cityName"])
        data = api_class.get_weather_data()
    return render_template("weather.html", data=data)

# Route za podatke o vjetru
@app.route("/wind", methods=["GET", "POST"])
def wind():
    data = None
    if request.method == "POST":
        api_class = APIHandler(request.form["cityName"])
        data = api_class.get_wind_data()
    return render_template("wind.html", data=data)

@app.route('/')
def redirectToHome():
    return redirect("/home")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
