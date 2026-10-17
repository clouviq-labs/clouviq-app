"""clouviq-app: the tiny web app every GitHub Masterclass demo builds, tests, releases and deploys."""
import os

from flask import Flask

app = Flask(__name__)
VERSION = os.environ.get("APP_VERSION", "dev")


@app.get("/")
def home():
    return f"<h1>ClouViQ App</h1><p>version {VERSION}</p>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "8080")))
