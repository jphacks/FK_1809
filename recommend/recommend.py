import json
import cv2
import argparse
import numpy as np
from annoy import AnnoyIndex
from chainercv import utils
from chainercv.links import SSD300
label_name = ("tops", "bottoms")
model = SSD300(n_fg_class=len(label_name), pretrained_model='via_model')

def crop_img(input_img, query_label="tops"):
  bboxes, labels, scores = model.predict([input_img])
  query_index = label_name.index(query_label)
  if query_index in labels[0]:
    bbox = [int(i) for i in bboxes[0][0]]
    croped_img = input_img[:, bbox[0]:bbox[2], bbox[1]:bbox[3]]
    return croped_img

def main():
  parser = argparse.ArgumentParser(description='recommend system')
  parser.add_argument('--query', '-q', type=str, default="",
                        help='query image path')
  parser.add_argument('--genre', '-g', type=str, default="tops",
                        help='genre')
  args = parser.parse_args()
  
  if args.query == "":
    raise("")
  genre = args.genre
  
  data_path = []
  with open("img_list.txt", "r") as f:
    for line in f.readlines():
      data_path.append(line.rstrip())
  annoy_model = AnnoyIndex(256)
  annoy_model.load("{}.ann".format(genre))
  query_path = args.query
  query_img = utils.read_image(query_path, color=True)
  croped_query_img = crop_img(query_img, genre)
  comparing_hist = cv2.calcHist([croped_query_img], [0], None, [256], [0, 256])
  predict_indexes = annoy_model.get_nns_by_vector(comparing_hist, 5, search_k=-1)
  predict_indexes = [data_path[idx].split("\\")[-1] for idx in predict_indexes]
  #with open("recommend_image.json", "w") as f:
  json_data =  json.dumps(predict_indexes)
  print(json_data)
          
if __name__=='__main__':
  main()
