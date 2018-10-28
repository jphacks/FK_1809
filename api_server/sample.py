from flask import Flask, jsonify, request
import os
import json
import getGameScore
from chainercv import utils
from chainercv.links import SSD300

label_name = ("tops", "bottoms")
model = SSD300(n_fg_class=len(label_name), pretrained_model='via_model')

app = Flask(__name__)

@app.route("/test/", methods=['GET'])
def ok():
    return "ok!!?"

@app.route("/callback", methods=['POST'])
def callback():

    # get request body as text
    body = request.get_data()
    clum = {}
    bboxes, labels, scores = model.predict([body])
    for bbox, label in zip(bboxes[0], labels[0]):
      label_index = label_name[label]
      clum[label_index] = [int(item) for item in bbox]
  
    return json.dumps(clum)


if __name__ == "__main__":
    app.run(ssl_context='adhoc')