from flask import Flask, render_template, request
from api_handler import APIHandler  # Uvozimo APIHandler klasu iz vanjske datoteke

app = Flask(__name__)

# Route za početnu stranicu
@app.route("/home")
def home():
    return render_template("home.html")

# Route za vremenske podatke
@app.route("/weather", methods=["GET", "POST"])
def weather():
    data = None
    if request.method == "POST":
        # Kreiramo instancu APIHandler klase s gradom dobivenim iz obrasca
        api_class = APIHandler(request.form["cityName"])
        # Pozivamo metodu za dohvaćanje vremenskih podataka iz APIHandler klase
        data = api_class.get_weather_data()
    # Prikazujemo template "weather.html" s podacima
    return render_template("weather.html", data=data)

# Route za podatke o vjetru
@app.route("/wind", methods=["GET", "POST"])
def wind():
    data = None
    if request.method == "POST":
        # Kreiramo instancu APIHandler klase s gradom dobivenim iz obrasca
        api_class = APIHandler(request.form["cityName"])
        # Pozivamo metodu za dohvaćanje podataka o vjetru iz APIHandler klase
        data = api_class.get_wind_data()
    # Prikazujemo template "wind.html" s podacima
    return render_template("wind.html", data=data)

# Ako se aplikacija pokreće izravno, pokrećemo Flask aplikaciju
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
