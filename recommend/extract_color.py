from PIL import Image
import cv2
import sklearn
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def extract_main_color(img_path, k_num):
  cv2_img = cv2.imread(img_path)
  cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
  cv2_img = cv2_img.reshape((cv2_img.shape[0] * cv2_img.shape[1], 3))
  cluster = KMeans(n_clusters=k_num)
  cluster.fit(X=cv2_img)
  KMeans(algorithm='auto', copy_x=True, init='k-means++', max_iter=300,
    n_clusters=5, n_init=10, n_jobs=1, precompute_distances='auto',
    random_state=None, tol=0.0001, verbose=0)
  hist = [0] * k_num
  result = cluster.fit_predict(cv2_img)
  for item in result:
    hist[item] += 1
  sorted_index = np.argsort(hist)
  print(sorted_index)
  hist = np.array(hist)[sorted_index[:-1]]
  hist = hist / hist.sum()
  color_list = cluster.cluster_centers_[sorted_index[:-1]]
  #plt.bar(np.arange(1,k_num), hist, color=cluster.cluster_centers_[sorted_index[:-1]]/256)
  #plt.show()
  res = [{"color": c, "percent": h} for c, h in zip(color_list, hist)]
  return res

hoge = extract_main_color('/home/sotaro/develop/hachathon/FK_1809/wearlog/app/assets/images/wear_images/20171201112823521_320.jpg', 4)

