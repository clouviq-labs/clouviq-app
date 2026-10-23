"""clouviq-app: the tiny web app every GitHub Masterclass demo builds, tests, releases and deploys."""
import os
from datetime import UTC, datetime

from flask import Flask, jsonify, request

app = Flask(__name__)
VERSION = os.environ.get("APP_VERSION", "dev").strip()
GREETINGS = {"en": "Hello", "de": "Hallo", "fr": "Bonjour"}


def feature_on(name):
    return os.environ.get(f"FEATURE_{name.upper()}", "false").lower() == "true"


@app.get("/")
def home():
    title = "ClouViQ App · new look" if feature_on("new_ui") else "ClouViQ App"
    lang = request.headers.get("Accept-Language", "en")
    return f"<h1>{title}</h1><p>{GREETINGS[lang]}!</p><p>version {VERSION}</p>"


@app.get("/health")
def health():
    return jsonify(status="ok", version=VERSION)


@app.get("/ping")
def ping():
    return jsonify(ping="pong")


@app.get("/time")
def time():
    return jsonify(utc=datetime.now(UTC).isoformat())


def add(a, b):
    return a + b


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "8080")))
