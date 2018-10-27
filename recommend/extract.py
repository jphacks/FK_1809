
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
for path in path_list[:1]:
    clum = {"img_path": path}
    img = utils.read_image(path)
    bboxes, labels, scores = model.predict([img])
    for bbox, label in zip(bbox, label):
        label_index = label_name.index(label)
        clum[label_name[label_index]] = bbox
with open("wear_info.json", "w") as f:
    json.dump(clum, f)
