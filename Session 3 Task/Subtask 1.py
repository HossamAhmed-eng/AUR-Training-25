import numpy as np
import matplotlib
matplotlib.use("Qt5Agg")
import matplotlib.pyplot as plt
import cv2



def convolution(image,kernel):
    flipped=np.flip(kernel)
    image_rows = image.shape[0]
    image_columns = image.shape[1]
    kernelcol=kernel.shape[1]
    kernelrow=kernel.shape[0]
    padh = kernelrow//2
    padw = kernelcol//2
    image=np.pad(image,((padh, padh),(padw, padw)))
    #arr = image[0:3]
    #print(image[0:3,0:3])
    result = image.copy()
    for i in range(image_rows):
        for j in range(image_columns):
            arr = image[i:i+kernelrow,j:j+kernelcol]
            #print(np.dot(arr.flatten(),flipped.flatten()))
            result[i][j] = abs(np.dot(arr.flatten(),flipped.flatten()))
    return result




img = cv2.imread('/home/hossam/Desktop/image.png', cv2.IMREAD_GRAYSCALE)
fig, axes = plt.subplots(2, 2, figsize=(8, 8))
axes[0, 0].imshow(img, cmap='gray')
axes[0, 0].set_title('Original Image')
axes[0, 0].axis('off')
axes[0, 1].imshow(convolution(img, np.ones((5, 5)) / 25), cmap='gray')
axes[0, 1].set_title('Box Filter')
axes[0, 1].axis('off')
axes[1, 0].imshow(convolution(img, np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])),
cmap='gray')
axes[1, 0].set_title('Horizontal Sobel Filter')
axes[1, 0].axis('off')
axes[1, 1].imshow(convolution(img, np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])),
cmap='gray')
axes[1, 1].set_title('Vertical Sobel Filter')
axes[1, 1].axis('off')
plt.show()