import cv2
import sys
from chainercv.links import SSD300
from chainercv.visualizations import vis_bbox
from chainercv.datasets import voc_bbox_label_names
model = SSD300(n_fg_class=len(voc_bbox_label_names), pretrained_model="voc0712")
cap = cv2.VideoCapture(0)

if cap.isOpened() is False:
  print("can not open camera")
  sys.exit()

def crop_human(img, bbox):
  # bbox = [int(i) for i in bbox*10]
  croped_img = img[bbox[0]:bbox[2], bbox[1]:bbox[3], :]
  return croped_img

def main():
  while True:
    # VideoCaptureから1フレーム読み込む
    ret, frame = cap.read()
    print(frame.shape)
    resized_frame = cv2.resize(frame, (int(frame.shape[1]*0.1), int(frame.shape[0]*0.1)))
    bboxes, labels, scores = model.predict([resized_frame.transpose(2,0,1)])
    bbox = [int(i) for i in bboxes[0][0] * 10]
    if bbox[2] - bbox[0] > bbox[3] - bbox[1] * 2.5:
      croped_frame = crop_human(frame, bbox)
      print(croped_frame.shape)
      cv2.imshow('frame', croped_frame)
    # キー入力を1ms待って、k が27（ESC）だったらBreakする
    k = cv2.waitKey(1)
    if k == 27:
      break

# キャプチャをリリースして、ウィンドウをすべて閉じる
  cap.release()
  cv2.destroyAllWindows()
if __name__ == '__main__':
    # 定数定義
  main()
