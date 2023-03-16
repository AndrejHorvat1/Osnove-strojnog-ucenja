import numpy as np
import matplotlib . pyplot as plt

img = plt.imread ("road.jpg")
img = img [ :,:,0]. copy ()

#a
add_brightness = 150
light_img = np.where((255 - img) < add_brightness, 255, img+add_brightness) 
plt.figure()
plt.imshow(light_img, cmap="gray")
plt.show()

#b
quarters=np.hsplit(img,4)
plt.title("Druga cetvrtina")
plt.imshow(quarters[1], cmap="gray")
plt.show()

#c
rotated=np.rot90(img)
rotated=np.rot90(rotated)
rotated=np.rot90(rotated)
plt.imshow(rotated, cmap="gray")
plt.show()

#d
mirror=np.flip(img,axis=1)
plt.imshow(mirror, cmap="gray")
plt.show()

