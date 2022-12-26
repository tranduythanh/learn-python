import os
import cv2 
import json
import numpy as np
import matplotlib.pyplot as plt

MIN_MATCH_COUNT = 10000

# read images
orgImg1 = cv2.imread('01.png')  
orgImg2 = cv2.imread('02.png') 
print("imread done", orgImg1.shape)

img1 = cv2.cvtColor(orgImg1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(orgImg2, cv2.COLOR_BGR2GRAY)
print("convert-color done")

#sift
sift = cv2.SIFT_create()

print("convert-color done")

kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)

# resultimage = cv2.drawKeypoints(img1, kp1, 0, (0, 255, 0), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# plt.imshow(resultimage)
# plt.show()

print("angle\tclass_id\t\tpt.x\tpt.y\tresp\tsize")
for x in kp1:
    print("{:.2f}\t\t{:d}\t\t{:.2f}\t{:.2f}\t{:.2f}\t{:.2f}".format(x.angle,x.class_id,x.pt[0],x.pt[1],x.response,x.size))

print(des1[1])

os._exit(1)

#feature matching
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks = 50)
flann = cv2.FlannBasedMatcher(index_params, search_params)
matches = flann.knnMatch(des1,des2,k=2)

# store all the good matches as per Lowe's ratio test.
good = []
for m,n in matches:
    if m.distance < 0.7*n.distance:
        good.append(m)

print(len(good))

good = sorted(good, key = lambda x:x.distance)



if len(good)>MIN_MATCH_COUNT:
    src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
    dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)
    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
    matchesMask = mask.ravel().tolist()
    h,w = img1.shape
    pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
    dst = cv2.perspectiveTransform(pts,M)
    img2 = cv2.polylines(img2,[np.int32(dst)],True,255,3, cv2.LINE_AA)
else:
    print( "Not enough matches are found - {}/{}".format(len(good), MIN_MATCH_COUNT) )
    matchesMask = None

draw_params = dict(matchColor = (0,255,0), # draw matches in green color
                   singlePointColor = None,
                   matchesMask = matchesMask, # draw only inliers
                   flags = 2)
img3 = cv2.drawMatches(orgImg1,kp1,orgImg2,kp2,good,None,**draw_params)
plt.imshow(img3, 'gray')
plt.show()