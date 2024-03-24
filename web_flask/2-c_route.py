#!/usr/bin/python3
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """
        Defines a simple GET route
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
        Defines a simple GET route
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """
        Defines a GET route that takes a parameter
    """
    new = text.replace('_', ' ')
    return "C " + new


def main():
    """
        Setups the application's listening process
    """
    app.run(host="0.0.0.0", port=5000)


if __name__ == "__main__":
    main()
