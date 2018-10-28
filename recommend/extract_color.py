from PIL import Image
import cv2
import sklearn
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
cv2_img = cv2.imread('/home/sotaro/develop/hachathon/FK_1809/wearlog/app/assets/images/wear_images/20171201112823521_320.jpg')
cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
cv2_img = cv2_img.reshape((cv2_img.shape[0] * cv2_img.shape[1], 3))
cluster = KMeans(n_clusters=4)
cluster.fit(X=cv2_img)
KMeans(algorithm='auto', copy_x=True, init='k-means++', max_iter=300,
  n_clusters=5, n_init=10, n_jobs=1, precompute_distances='auto',
  random_state=None, tol=0.0001, verbose=0)
hist = [0] * 4
result = cluster.fit_predict(cv2_img)
for item in result:
  hist[item] += 1
print(cluster.cluster_centers_/255)
plt.bar([1,2,3, 4], hist, color=cluster.cluster_centers_/256)
plt.show()