from flask import Flask, jsonify, abort
import requests

app = Flask(__name__)

SERWIS_PRODUKTY_URL = "http://localhost:8001/produkty/"

ZAPAS = {
    1: 15,
    2: 40,
    3: 100,
    4: 25,
    5: 14,
}

@app.get("/zapas/<int:produkt_id>")
def podaj_zapas(produkt_id):
    odp = requests.get(SERWIS_PRODUKTY_URL + str(produkt_id))

    if odp.status_code == 404:
        abort(404, description="Nie znaleziono produktu")

    ilosc = ZAPAS.get(produkt_id, 0)

    return jsonify({
        "produktId": produkt_id,
        "ilosc": ilosc
    })

if __name__ == "__main__":
    app.run(port=8002)