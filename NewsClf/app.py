from flask import Flask

from NewsClf import app
from flask_swagger_ui import get_swaggerui_blueprint
from NewsClf import routes


### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Credit-Card-Fraud-Detection-ML"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###

if __name__ == "__main__":
    app.run(debug=True)