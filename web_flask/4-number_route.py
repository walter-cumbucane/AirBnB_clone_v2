#!/usr/bin/python3
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello():
    """
        Defines a simple GET route
    """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """
        Defines a simple GET route
    """
    return "HBNB"


@app.route("/c/<text>")
def c(text):
    """
        Defines a GET route that takes a parameter
    """
    new = text.replace('_', ' ')
    return "C " + new


@app.route("/python/<text>")
@app.route('/python', defaults={'text': 'is cool'})
def python(text):
    new = text.replace('_', ' ')
    return "Python " + new


@app.route("/number/<int:n>")
def number(n):
    return str(n) + " is a number"


def main():
    """
        Setups the application's listening process
    """
    app.run(host="0.0.0.0", port=5000)


if __name__ == "__main__":
    main()
