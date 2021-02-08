import cv2
for j in range(5):
    images = []
    #if j > 0:
    #    break
    for i in range(5):
        image = cv2.imread("./images/c%d_%d.tif"%(j, i))
        images.append(image)
    stitcher = cv2.Stitcher_create(1)
    print(len(images))
    (status, stitched) = stitcher.stitch(images)
    cv2.imwrite("test%d.png"%j, stitched)

images = []
images.append(cv2.imread("./images/c%d_%d.tif"%(1, 0)))
stitcher = cv2.Stitcher_create(1)
for j in range(5)[0:]:
    images.append(cv2.imread("./images/c%d_%d.tif"%(1, j)))
    #images.append(cv2.imread("./test.png"))
    (status, stitched) = stitcher.stitch(images)
    images = []
    images.append(stitched)
cv2.imwrite("test.png", stitched)
j = 1
images.append(cv2.imread("./images/c%d_%d.tif"%(j, 0)))
#stitcher = cv2.Stitcher_create(1)
(status, stitched) = stitcher.stitch(images)
images = []
images.append(stitched)
break