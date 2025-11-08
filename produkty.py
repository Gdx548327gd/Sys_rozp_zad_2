from flask import Flask, jsonify, abort

app = Flask(__name__)

PRODUKTY = {
    1: {"id": 1, "nazwa": "Laptop", "cena": 5000.0},
    2: {"id": 2, "nazwa": "Monitor", "cena": 1200.0},
    3: {"id": 3, "nazwa": "Procesor", "cena": 2000.0},
    4: {"id": 4, "nazwa":"Karta_graficzna", "cena": 8000.0},
    5: {"id": 5, "nazwa": "Telefon", "cena": 900.0},
}

@app.get("/produkty/<int:produkt_id>")

def get_product(produkt_id):
    produkt = PRODUKTY.get(produkt_id)
    if produkt is None:
        abort(404, description="Nie znaleziono produktu")
    return jsonify(produkt)

if __name__ == "__main__":
    app.run(port=8001)