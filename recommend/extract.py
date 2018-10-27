
import cv2
import glob
import argparse
import json
from chainercv import utils
from chainercv.links import SSD300


json_data = []

label_name = ("tops", "bottoms")
model = SSD300(n_fg_class=len(label_name), pretrained_model='via_model')

dara_dir = "D:/GitHub/FK_1809/wearlog/app/assets/images/wear_images"
print(dara_dir)

path_list = glob.glob("{}/*".format(dara_dir))
for path in path_list:
    print(path)
    clum = {"img_path": path.split("\\")[-1]}
    img = utils.read_image(path)
    bboxes, labels, scores = model.predict([img])
    for bbox, label in zip(bboxes[0], labels[0]):
        label_index = label_name[label]
        clum[label_index] = [int(item) for item in bbox]
    json_data.append(clum)
with open("wear_info.json", "w") as f:
    json.dump(json_data, f)
