from flask import Flask, jsonify, request, make_response
import cv2
import os
import numpy as np
import json
from chainercv import utils
from chainercv.links import SSD300


app = Flask(__name__)

@app.route("/test/", methods=['GET'])
def ok():
    return "ok!!?"
@app.route("/callback", methods=['POST'])
def callback():
    label_name = ("tops", "bottoms")
    model = SSD300(n_fg_class=len(label_name), pretrained_model='via_model')
    # get request body as text
    stream = request.files["imageFile"].stream
    # return make_response(jsonify({'result': stream}))
    img = np.asarray(bytearray(stream.read()), dtype=np.uint8)
    img = cv2.imdecode(img, 1)
    clum = {}
    bboxes, labels, scores = model.predict([img.transpose(2,0,1)])
    for bbox, label in zip(bboxes[0], labels[0]):
      label_index = label_name[label]
      clum[label_index] = [int(item) for item in bbox]

    return json.dumps(clum)

if __name__ == "__main__":
    app.run(ssl_context='adhoc')