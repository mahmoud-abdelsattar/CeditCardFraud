from threading import Thread
import numpy as np
import pandas as pd
from flask import Flask, jsonify, request
from NewsClf.clf import run, load_model
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

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


@app.route("/")
def index():
    return "welcome to news clf"


@app.route("/train")
def train_new_model():
    trainer_job = Thread(target=run)
    trainer_job.start()
    return "training started !!"


@app.route("/load_model")
def load_new_model():
    cur_model = load_model()
    return "model updated !"


@app.route("/clf", methods=['POST'])  # for test use postman and in test tab put this [{"data":""}]
def classify():
    # load doc
    if  request.is_json:
        print("Valid Json")
    else:
        return jsonify({
            "Bad Request": "Not Valid Json Request , Please check the Keys and values numbers "
        })
    
    data = request.json['data']
    print(data)
    print(type(data))

    cur_model = load_model()
    data = pd.DataFrame.from_dict(data, orient='index')
    data = data.values.reshape(-1, 30)
    pred = cur_model.predict(data)
    conf = cur_model.predict_proba(data)
    print(type(pred))
    print(pred)

    # Replace every 0 with Valid and every 1 with Fraud in prediction
    mapping = {1: 'Fraud', 0: 'Valid'}
    map = lambda x: mapping.get(x, x)
    pred = np.vectorize(map)(pred)
    print(pred)

    # Converting the numpyArray to list so jsonify can convert it to json
    pred = pred.tolist()
    conf = conf.tolist()
    return jsonify({
        "transaction": pred[0],
        "Confidence":  conf[0]
    })
