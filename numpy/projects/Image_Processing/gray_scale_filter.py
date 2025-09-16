import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread("C:/PYHTON_FRESH/NUMPY/projects/Image_Processing/bg.jpg")
print("Original shape:", img.shape)

if img.ndim == 3:  # RGB image
    gray_img = np.mean(img, axis=2)  
else:
    gray_img = img  

plt.imshow(gray_img, cmap="gray") #cmap is used to change the color of an image[png,jpg]
plt.title("Grayscale Image")
plt.axis("off")
plt.show()

#brightness
bright_image = gray_img + 200

bright_image = np.clip(bright_image,0,255)
plt.imshow(bright_image, cmap = "gray")
plt.title("BRIGHT IMAGE")
plt.axis("off")
plt.show()






#contrast

contrast_img = gray_img * 3


contrast_img = np.clip(contrast_img,0,255)
plt.imshow(contrast_img,cmap = "gray")
plt.title("IMAGE WITH CONTRAST")
plt.axis("off")
plt.show()



