#!/usr/bin/python3
"""
   Contains a flask application with a route that says 'Hello HBNB'
"""
from flask import Flask


app = Flask(__name__)
app.rul_map.strict_slashes = False


@app.route("/")
def hello():
    """
        Defines a simple GET route
    """
    return "Hello HBNB!"


def main():
    """
        Setups the application listening process
    """
    app.run(host="0.0.0.0", port=5000)


if __name__ == "__main__":
    main()
