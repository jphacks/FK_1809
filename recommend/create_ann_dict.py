import cv2
import argparse
import json
from chainercv import utils
from annoy import AnnoyIndex
label_name = ("tops", "bottoms")

def crop_img(input_img, bbox):
  croped_img = input_img[:, bbox[0]:bbox[2], bbox[1]:bbox[3]]
  return croped_img

def main():
  parser = argparse.ArgumentParser(description='create ann model')
  parser.add_argument('--imgdir', '-d', type=str, default="../wearlog/app/assets/images/wear_images/",
                        help='image directry')
  parser.add_argument('--bbox', '-b', type=str, default="",
                        help='bbox image')
  parser.add_argument('--genre', '-g', type=str, default="tops",
                        help='genre')
  args = parser.parse_args()
  genre = args.genre
  
  data_dir = args.imgdir
  # bbox = [int(item) for item in args.bbox.split(",")]
  if data_dir == "":
    raise ValueError("directry is empty")

  with open("wear_info.json", "r") as f:
    json_data = json.load(f)
  
  annoy_model = AnnoyIndex(256)
  for idx, item in enumerate(json_data):
    path = item["img_path"]
    bbox = item[genre]
    img = utils.read_image(data_dir+path, color=True)
    croped_img = crop_img(img, bbox)
    comparing_hist = cv2.calcHist([croped_img], [0], None, [256], [0, 256])
    annoy_model.add_item(idx, comparing_hist[:, 0])
  annoy_model.build(256)
  annoy_model.save('{}.ann'.format(genre))

if __name__=='__main__':
  main()
