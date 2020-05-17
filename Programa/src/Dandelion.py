import cv2 as cv
import numpy as np

def DandelionStatus(img):
    ############################################# Clustering

    Z = img.reshape((-1, 3))
    # convert to np.float32
    Z = np.float32(Z)
    # define criteria, number of clusters(K) and apply kmeans()
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    K = 2
    ret, label, center = cv.kmeans(Z, K, None, criteria, 10, cv.KMEANS_RANDOM_CENTERS)
    # Now convert back into uint8, and make original image
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((img.shape))

    ############################################# Threshold parameters, colour of a petal

    lower = 150
    upper = 255

    ############################################# Kernels

    kernel = np.ones((3, 3), np.uint8)
    kernelo = cv.getStructuringElement(cv.MORPH_ELLIPSE, (4, 4))
    kerneld = cv.getStructuringElement(cv.MORPH_DILATE, (3, 3))
    kernelc = np.ones((4, 4), np.uint8)

    ############################################# Thresholding petals

    gray = cv.cvtColor(res2, cv.COLOR_BGR2GRAY)
    mask = cv.inRange(gray, lower, upper)
    # cv.imwrite('mask.jpg', mask)
    # White circle on the center
    """center = (round(mask.shape[1] / 2), round(mask.shape[0] / 2))
    radius = round(mask.shape[1] * 1 / 5)  # 6
    color = (255, 255, 255)
    cv.circle(mask, center, radius, color, thickness=-1, lineType=8, shift=0)"""

    # Opening
    mask_op = cv.morphologyEx(mask, cv.MORPH_OPEN, kernelo)

    # Closing
    mask_cl = cv.morphologyEx(mask_op, cv.MORPH_CLOSE, kernelc)
    fixed = mask_op
    # mask_hsv = cv.cvtColor(mask, cv.COLOR_GRAY2BGR)
    # hsv_Threshold = hsv & mask_hsv
    # img_Threshold = cv.cvtColor(hsv_Threshold, cv.COLOR_HSV2BGR)

    ############################################# Gray image

    # gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    fixed_f32 = np.float32(fixed)

    ############################################# Convex Hull

    # Finding Contours
    contours, hierarchy = cv.findContours(fixed, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]

    # Convex Hull
    hull = cv.convexHull(cnt, returnPoints=False)

    # Defects
    defects = cv.convexityDefects(cnt, hull)
    list_def = []

    # Painting Convex Hull
    for i in range(defects.shape[0]):
        s, e, f, d = defects[i, 0]
        start = tuple(cnt[s][0])
        end = tuple(cnt[e][0])
        far = tuple(cnt[f][0])
        list_def.append(far)
        cv.line(img, start, end, [0, 255, 0], 1)
        cv.circle(img, far, 3, [255, 100, 0], -1)

    ############################################# Harris Corner Detector

    """dst = cv.cornerHarris(fixed_f32, 2, 3, 0.08)  # (fixed_f32, 2, 3, 0.07)

    # result is dilated for marking the corners
    dst = cv.dilate(dst, None)

    # Threshold for an optimal value, it may vary depending on the image.
    img[dst > 0.01 * dst.max()] = [0, 0, 255]
    corners = []

    for i in range(img.shape[1]):
        for j in range(img.shape[0]):
            if (img.item(j, i, 2) == 255):
                corners.append([i, j])"""

    ############################################# Properties

    # Area of contour
    area = cv.contourArea(cnt)

    # Perimeter of contour
    perimeter = cv.arcLength(cnt, True)

    # Aspect Ratio
    x, y, w, h = cv.boundingRect(cnt)

    if h > w:
        aspect_ratio = float(w) / h
    else:
        if h < w:
            aspect_ratio = float(h) / w
        else:
            aspect_ratio = 0

    # Extent
    rect_area = w * h
    extent = float(area) / rect_area

    # Solidity
    hull = cv.convexHull(cnt)
    hull_area = cv.contourArea(hull)
    solidity = float(area) / hull_area
    perfect_extent = 0.7853981633975
    #print('Extent', extent)
    #print('aspect_ratio', aspect_ratio)
    #print('Solidity', solidity)
    factor = 25
    Health = (extent / perfect_extent) * 0.3 + aspect_ratio * 0.5 + solidity * 0.2
    #print('Health', Health)

    # Leaf Density: number of petals per 90º
    leafDens = solidity
    #leafNum = round((len(list_def)) * 1 + (len(corners) / factor) * 0)
    #leafDens = round(leafNum / (2 * 3.14159265359))
    #print('leafNum', leafNum)
    #print('leafDens per Radian', leafDens)

    ############################################# Show the image

    """cv.imshow("img", img)
    cv.imshow("res2", res2)
    cv.imshow("mask", mask)
    cv.imshow("mask_op", mask_op)
    cv.imshow("closing", mask_cl)
    k = cv.waitKey(0)
    cv.imwrite('DandelionProc.jpg', img)"""

    return int(Health*100), leafDens