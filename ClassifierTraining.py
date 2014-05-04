#!/usr/bin/env python

import cv2
import os, sys
import numpy as np
from scipy import ndimage
from skimage import morphology, img_as_uint
import cPickle
from sklearn.ensemble import RandomForestClassifier


def getObjectFeatures(img, contour):
    x, y, w, h = cv2.boundingRect(contour)
    area = cv2.contourArea(contour)
    extent = float(area) / (h*w)

    hull = cv2.convexHull(contour)
    hull_area = cv2.contourArea(hull)

    solidity = float(area) / hull_area
    (x, y), (major_axis, minor_axis), angle = cv2.fitEllipse(contour)

    mask = np.zeros(img.shape, np.uint8)
    cv2.drawContours(mask, [contour], 0, 255, -1)
    val_min, val_max, loc_min, loc_max = cv2.minMaxLoc(img, mask=mask)
    mean_val = cv2.mean(img, mask=mask)

    return [float(area), extent, solidity, float(major_axis), float(minor_axis), val_min, val_max]

def run(XPOS, YPOS):
    features = []
    responses = []
    for fname in os.listdir('Training/image_set'):
        fn = os.path.join('Training/image_set', fname)
        # Read in image as grayscale
        img = cv2.imread(fn)

        gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        ret, thresh = cv2.threshold(gray_img, 220, 255, cv2.THRESH_TOZERO)
        fill = ndimage.binary_fill_holes(thresh)
        
        clean = morphology.remove_small_objects(fill, 12)
        clean = img_as_uint(clean).astype(np.dtype('uint8'))
        contour_image = clean.copy()

        contours, hierarchy = cv2.findContours(contour_image, cv2.RETR_LIST, cv2.CHAIN_APPROX_TC89_KCOS)

        for cnt in contours:
            if len(cnt) < 5:
                continue
            
            gray_copy = gray_img.copy()
            img_copy = img.copy()
            feats = getObjectFeatures(gray_copy, cnt)
            x, y, w, h = cv2.boundingRect(cnt)
            if x > 10:
                x = x - 10
            if y > 10:
                y = y - 10
            if (x + w + 20) < 640:
                w = w + 20
            if (y + h + 20) < 480:
                h = h + 20
            cv2.rectangle(img_copy, (x, y), (x+w, y+h), (255,0,0), 2)

            features.append(feats)

            cv2.imshow('Training Demo', img_copy)
            cv2.moveWindow('Training Demo', XPOS, YPOS)
            key = cv2.waitKey(0) & 0xFF

            if key == ord('0') or key == 176:
                responses.append(0)
            elif key == ord('1') or key == 177:
                responses.append(1)
            elif key == ord('2') or key == 178:
                responses.append(2)
            elif key == ord('3') or key == 179:
                responses.append(3)
            elif key == ord('4') or key == 180:
                responses.append(4)
            elif key == ord('5') or key == 181:
                responses.append(5)
            elif key == 27:
                return None, None

            del(gray_copy)
            del(img_copy)
            
            cv2.destroyAllWindows()

    return features, responses


if __name__=='__main__':
    XPOS = 640
    YPOS = 300

    features, responses = run(XPOS, YPOS)

    if features == None and responses == None:
        sys.exit()

    rf = RandomForestClassifier(n_jobs=-1)
    rf.fit(features, responses)
    print "Classifier Score after Training: %f" % rf.score(features, responses)
    
    cPickle.dump(rf, open('Training/RFClassifier.pkl', 'wb'))

    sys.exit()
    

