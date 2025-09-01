import numpy as np
import matplotlib #for ubuntu
matplotlib.use("Qt5Agg") #for ubuntu
import matplotlib.pyplot as plt
import cv2
# Take notice that OpenCV handles the image as a numpy array when opening it 
img = cv2.imread('/home/hossam/Desktop/session 3 opencv+ml/shapes.jpg')

# Make a mask for each color (red, blue, black)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # Take care that the default colorspace that OpenCV opens an image in is BGR not RGB

blue_mask  = (img_rgb[...,2] > 150) & (img_rgb[...,0] < 80)  & (img_rgb[...,1] < 80)   # Blue
red_mask   = (img_rgb[...,0] > 150) & (img_rgb[...,1] < 80)  & (img_rgb[...,2] < 80)#red
black_mask = (np.max(img_rgb, axis=2) < 50) #black
out = img_rgb.copy()
out[blue_mask]=[0,0,0]
out[red_mask]=[0,0,255]
out[black_mask]=[255,0,0]

fig, axes = plt.subplots(1, 2)
axes[0].imshow(img)
axes[0].set_title('Original Image')
axes[0].axis('off')

axes[1].imshow(out)
axes[1].set_title('Processed Image')
axes[1].axis('off')

plt.show()