# Cool Weather Application

Cool Weather Application je Flask web aplikacija koja pruža informacije o trenutačnom vremenu na odabranim lokacijama diljem svijeta. Aplikacija koristi Python s Flask frameworkom, Jinja2 kao template engine, te Bootstrap za poboljšanje korisničkog sučelja. Također, za dohvaćanje podataka o temperaturi i vjetru koristi se OpenWeather API.

## Tehničke Specifikacije

### Tehnologije

- **Flask**: Web framework za Python koji omogućuje brzo i jednostavno razvijanje web aplikacija.
- **Jinja2**: Template engine za Python, korišten za dinamičko generiranje HTML-a.
- **Bootstrap**: Frontend framework za brzo oblikovanje sučelja web stranica.
- **OpenWeather API**: API za dobivanje trenutačnih meteoroloških podataka diljem svijeta.

### Postavljanje Aplikacije

1. Postavljanje OpenWeather API ključa:
    - Registrirajte se na [OpenWeather](https://openweathermap.org/) kako biste dobili svoj API ključ.
    - Postavite API ključ kao "enviroment" varijablu "WEATHERAPI".

2. Pokretanje aplikacije:
    ```bash
    flask run
    ```

Aplikacija će biti dostupna na [http://localhost:5000/](http://localhost:5000/).

## Kako koristiti

1. Posjetite početnu stranicu aplikacije, u navbar-u odaberite Weather ili Wind.
2. Unesite željenu lokaciju u tražilicu.
3. Pregledajte trenutačne informacije o temperaturi i vjetru na odabranoj lokaciji.

## Napomene

- Aplikacija zahtijeva OpenWeather API ključ za ispravan rad. Postavite ključ kao okolinjsku varijablu "WEATHERAPI" prije pokretanja.

---

**Autor:** Andrija Škontra
