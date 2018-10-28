import cv2
import argparse
import json
label_name = ("tops", "bottoms")

def crop_img(input_img, bbox):
  croped_img = input_img[:, bbox[0]:bbox[2], bbox[1]:bbox[3]]
  return croped_img

def main():
  parser = argparse.ArgumentParser(description='create ann model')
  parser.add_argument('--imgdir', '-d', type=str, default="D:/GitHub/FK_1809/wearlog/app/assets/images/wear_images",
                        help='image directry')
  parser.add_argument('--genre', '-g', type=str, default="tops",
                        help='genre')
  args = parser.parse_args()
  genre = args.genre

  data_dir = args.imgdir
  if data_dir == "":
    raise ""
  with open("wear_info.json", "r") as f:
    json_data = json.load(f)
  
  data_path = glob.glob("{}/*".format(data_dir))
  with open("img_list.txt", "w") as f:
    f.write("\n".join(data_path))
  annoy_model = AnnoyIndex(256)
  for i, path in enumerate(data_path):
    img = utils.read_image(path, color=True)
    croped_img = crop_img(img, genre)
    comparing_hist = cv2.calcHist([croped_img], [0], None, [256], [0, 256])
    annoy_model.add_item(i, comparing_hist[:, 0])
  annoy_model.build(256)
  annoy_model.save('{}.ann'.format(genre))

if __name__=='__main__':
  main()
