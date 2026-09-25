from flask import Flask, request, redirect, render_template, jsonify
import sqlite3
import string
import random

app = Flask(__name__)

DATABASE = "urls.db"


def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original_url TEXT NOT NULL,
            short_code TEXT UNIQUE NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def generate_code(length=6):
    characters = string.ascii_letters + string.digits

    while True:
        code = "".join(random.choice(characters) for _ in range(length))

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id FROM urls WHERE short_code = ?",
            (code,)
        )
        existing = cursor.fetchone()
        conn.close()

        if not existing:
            return code


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/shorten", methods=["POST"])
def shorten_url():
    original_url = request.form.get("url")

    if not original_url:
        return jsonify({"error": "Please enter a URL"}), 400

    if not original_url.startswith(("http://", "https://")):
        original_url = "https://" + original_url

    short_code = generate_code()

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO urls (original_url, short_code) VALUES (?, ?)",
        (original_url, short_code)
    )

    conn.commit()
    conn.close()

    short_url = request.host_url + short_code

    return render_template(
        "index.html",
        short_url=short_url
    )


@app.route("/<short_code>")
def redirect_url(short_code):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT original_url FROM urls WHERE short_code = ?",
        (short_code,)
    )

    result = cursor.fetchone()
    conn.close()

    if result:
        return redirect(result[0])

    return "URL not found", 404


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
