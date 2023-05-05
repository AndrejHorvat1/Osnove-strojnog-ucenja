import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as Image
from sklearn.cluster import KMeans

# ucitaj sliku
img = Image.imread("imgs\\test_2.jpg")

# prikazi originalnu sliku
plt.figure()
plt.title("Originalna slika")
plt.imshow(img)
plt.tight_layout()
plt.show()

# pretvori vrijednosti elemenata slike u raspon 0 do 1
img = img.astype(np.float64) / 255

# transfromiraj sliku u 2D numpy polje (jedan red su RGB komponente elementa slike)
w, h, d = img.shape
img_array = np.reshape(img, (w*h, d))

# rezultatna slika
img_array_aprox = img_array.copy()

diff_colors = len(np.unique(img_array_aprox, axis=0))

print(diff_colors)

k = [1, 3, 5, 7, 10]

for j in range(len(k)):

img_array_aprox = img_array.copy()

if j == 4:
img_array_aprox = img_array_aprox[:, :3]

km = KMeans(n_clusters=k[j], init='k-means++', n_init=5, random_state=0)

km.fit(img_array_aprox)

for z in np.unique(km.labels_):
img_array_aprox[km.labels_ == z, :] = km.cluster_centers_[z]

img2 = img_array_aprox.reshape(img.shape)

plt.subplot(3, 2, j+1)
plt.title('k = ' + str(k[j]))
plt.imshow(img2)
plt.tight_layout()

plt.show()