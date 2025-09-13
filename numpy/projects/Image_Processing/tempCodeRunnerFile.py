if img.ndim == 3:  # RGB image
    gray_img = np.mean(img, axis=2)  
else:
    gray_img = img 