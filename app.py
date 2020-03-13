from flask import Flask

from NewsClf.routes import app
from NewsClf import routes


if __name__ == "__main__":
    app.run(debug=True)
