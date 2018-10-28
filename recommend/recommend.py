import json
import cv2
import argparse
import numpy as np
from chainercv import utils
from annoy import AnnoyIndex
label_name = ("tops", "bottoms")

def crop_img(input_img, bbox):
  croped_img = input_img[:, bbox[0]:bbox[2], bbox[1]:bbox[3]]
  return croped_img

def main():
  parser = argparse.ArgumentParser(description='recommend system')
  parser.add_argument('--query', '-q', type=str, default="",
                        help='query image path')
  parser.add_argument('--bbox', '-b', type=str, default="",
                        help='bbox image')
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
  bbox = [int(item) for item in args.bbox.split(",")]

  query_img = utils.read_image(query_path, color=True)
  croped_query_img = crop_img(query_img, bbox)
  comparing_hist = cv2.calcHist([croped_query_img], [0], None, [256], [0, 256])
  predict_indexes = annoy_model.get_nns_by_vector(comparing_hist, 5, search_k=-1)
  predict_indexes = [data_path[idx].split("\\")[-1] for idx in predict_indexes]
  #with open("recommend_image.json", "w") as f:
  json_data =  json.dumps(predict_indexes)
  print(json_data)
          
if __name__=='__main__':
  main()
