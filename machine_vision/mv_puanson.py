import cv2
import numpy as np
import matplotlib.pyplot as plt

print("Kon'")

# Load the image
img = cv2.imread("/home/konstantin/Documents/1096/manufacturing part/im3.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

marker = np.zeros_like(img[:,:,0]).astype(np.int32)

# Object
marker[200, 200] = 1
marker[267, 927] = 1
marker[404, 908] = 1
marker[228, 216] = 1

# Background
marker[100, 100] = 64
marker[86, 393]  = 64
marker[497, 704] = 64
marker[320, 905] = 64
marker[156, 837] = 64

cv2.watershed(img, marker)

#plt.imshow(marker, cmap='gray')
#plt.show()

# Load template

template = cv2.imread("/home/konstantin/Documents/1096/manufacturing part/temp3.jp2")

template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

marker_template = np.zeros_like(template[:,:,0]).astype(np.int32)

# Border
marker_template[123, 270] = 1

# Inside
marker_template[130, 270] = 64

# Outside
marker_template[115, 270] = 128


cv2.watershed(template_gray, marker_template)


plt.imshow(marker_template, cmap='gray')
plt.show()


# Overload template and the extracted part 









exit()


#for i, x in enumerate(template):
#    for j, y in enumerate(x):
#        if np.array_equal(y, [0, 0, 0]): template[i, j] = [255, 0, 0]
        

# plt.imshow(template)
# plt.show()

# Create three regions in the template


marker = np.zeros_like(img[:,:,0]).astype(np.int32)
marker[100, 100] = 1
marker[200, 200] = 64

marked = cv2.watershed(img, marker)

#plt.imshow(gray, cmap='gray')
#plt.show()


thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)

#ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

plt.imshow(thresh, cmap='gray')
plt.show()


# img[192][192] = [255,0,0]
# img[250][170] = [255,0,0]
# img[222][245] = [255,0,0]

#plt.imshow(img)
#plt.show()





# Create a blank image of zeros (same dimension as img)
# It should be grayscale (1 color channel)
marker = np.zeros_like(img[:,:,0]).astype(np.int32)

# This step is manual. The goal is to find the points
# which create the result we want. I suggest using a
# tool to get the pixel coordinates.

# Dictate the background and set the markers to 1
marker[193][192] = 1
marker[113][249] = 1

# Areas of interest
marker[222][245] = 64
marker[223][245] = 64
marker[222][246] = 64
marker[223][246] = 64

print(repr(marker))

marker32 = np.int32(marker)


#cv2.watershed(img,marker32)
#m = cv2.convertScaleAbs(marker32)

marked = cv2.watershed(img, marker32)

print(marked)

#plt.imshow(marked)
#plt.show()

'''

# Dictate the area of interest
# I used different values for each part of the car (for visibility)
marker[235][370] = 255    # car body
marker[135][294] = 64     # rooftop
marker[190][454] = 64     # rear light
marker[167][458] = 64     # rear wing
marker[205][103] = 128    # front bumper

# rear bumper
marker[225][456] = 128
marker[224][461] = 128
marker[216][461] = 128

# front wheel
marker[225][189] = 192
marker[240][147] = 192

# rear wheel
marker[258][409] = 192
marker[257][391] = 192
marker[254][421] = 192

# Now we have set the markers, we use the watershed
# algorithm to generate a marked image
marked = cv2.watershed(img, marker)

# Plot this one. If it does what we want, proceed;
# otherwise edit your markers and repeat
plt.imshow(marked, cmap='gray')
plt.show()

# Make the background black, and what we want to keep white
marked[marked == 1] = 0
marked[marked > 1] = 255

# Use a kernel to dilate the image, to not lose any detail on the outline
# I used a kernel of 3x3 pixels
kernel = np.ones((3,3),np.uint8)
dilation = cv2.dilate(marked.astype(np.float32), kernel, iterations = 1)

# Plot again to check whether the dilation is according to our needs
# If not, repeat by using a smaller/bigger kernel, or more/less iterations
plt.imshow(dilation, cmap='gray')
plt.show()

# Now apply the mask we created on the initial image
final_img = cv2.bitwise_and(img, img, mask=dilation.astype(np.uint8))

# cv2.imread reads the image as BGR, but matplotlib uses RGB
# BGR to RGB so we can plot the image with accurate colors
b, g, r = cv2.split(final_img)
final_img = cv2.merge([r, g, b])

# Plot the final result
plt.imshow(final_img)
plt.show()

'''


'''

1 - First we load our image, convert it to grayscale, and threshold it with a suitable value. I took Otsu's binarization, so it would find the best threshold value.

import cv2
import numpy as np

img = cv2.imread('sofwatershed.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
Below is the result I got:

enter image description here

( even that result is good, because great contrast between foreground and background images)

2 - Now we have to create the marker. Marker is the image with same size as that of original image which is 32SC1 (32 bit signed single channel).

Now there will be some regions in the original image where you are simply sure, that part belong to foreground. Mark such region with 255 in marker image. Now the region where you are sure to be the background are marked with 128. The region you are not sure are marked with 0. That is we are going to do next.

A - Foreground region:- We have already got a threshold image where pills are white color. We erode them a little, so that we are sure remaining region belongs to foreground.

fg = cv2.erode(thresh,None,iterations = 2)
fg :

enter image description here

B - Background region :- Here we dilate the thresholded image so that background region is reduced. But we are sure remaining black region is 100% background. We set it to 128.

bgt = cv2.dilate(thresh,None,iterations = 3)
ret,bg = cv2.threshold(bgt,1,128,1)
Now we get bg as follows :

enter image description here

C - Now we add both fg and bg :

marker = cv2.add(fg,bg)
Below is what we get :

enter image description here

Now we can clearly understand from above image, that white region is 100% foreground, gray region is 100% background, and black region we are not sure.

Then we convert it into 32SC1 :

marker32 = np.int32(marker)
3 - Finally we apply watershed and convert result back into uint8 image:

cv2.watershed(img,marker32)
m = cv2.convertScaleAbs(marker32)
m :

enter image description here

4 - We threshold it properly to get the mask and perform bitwise_and with the input image:

ret,thresh = cv2.threshold(m,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
res = cv2.bitwise_and(img,img,mask = thresh)
res :

'''