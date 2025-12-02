"""
from flask import Flask, jsonify
app = Flask(__name__)

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * n <= n * n:
        if n % i == 0:
            return False
        i += 2
    return True

@app.route("/prime_number/<int:number>", methods=["GET"])
def prime_number(number):
    result = {
        "Number": number,
        "isPrime": is_prime(number)
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)

"""

from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def get_airport_by_icao(icao):
    connection = sqlite3.connect('airports.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute("SELECT ident, name, municipality FROM airport WHERE ident = ?", (icao,))
    row = cursor.fetchone()

    connection.close()

    return row

@app.route("/airport/<string:icao>", methods=["GET"])
def airport(icao):
    result = get_airport_by_icao(icao.upper())

    if result is None:
        return jsonify({"error": "Airport not found!"}), 404

    response = {
        "ICAO": result["ident"],
        "Name": result["name"],
        "Location": result["municipality"],
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)