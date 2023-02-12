import cv2 
# for reading images and videos 
import numpy as np
# for mathematical operations and array manipulation on images

img = cv2.imread('Fox-PNG-File.png')
# read the image file and store it into img variable

grey= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# turns the image into grey color
grey=cv2.medianBlur(grey,5)

cv2.imshow("GREY IMAGE",grey)

edges = cv2.Canny(grey,10, 90)
cv2.imshow(" EDGES ",edges)

mask = np.zeros_like(edges)
#np.zeros_like is used to create a matrix of zeros with the same shape as the edges matrix
mask[edges== 0] = 1
# mask[edges==0]=1 is used to make the edges white

mask = mask.astype(np.uint8)
# mask is used to remove the noise from the image and to smoothen the image

#cartoonization
color=cv2.bilateralFilter(img,9,250,250)
cv2.imshow("COLOR IMAGE",color)
 
#bilateral filter is used to reduce the noise and smoothen the image
cartoon=cv2.bitwise_or(color,color,mask = mask)
# bitwise_or is used to combine the two images with or operation mixing color and mask image 
# mask has black edges and color has the colored image so combing them both in one leaves out the edges making them go black

#bitwise and is used to combine the two images
cv2.imshow("CARTOONIZED IMAGE",cartoon)
cv2.imwrite("cartoonized_image.png",cartoon)

cv2.waitKey(0)
# waitkey is used to display the image for infinite time
cv2.destroyAllWindows()
# destroyAllWindows is used to destroy all the windows created