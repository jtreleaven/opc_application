from multiprocessing.pool import ThreadPool
from collections import deque
from skimage.morphology import remove_small_objects
import cPickle
import cv2
import numpy as np


if __name__=='__main__':
    import sys

    def loadNextFrame(img, rf, mask):
        
        

        for cnt in contours:
            area = cv2.contourArea(cnt)
            x, y, w, h = cv2.boundingRect(cnt)
            

        return img

    try:
        fn = sys.argv[1]
    except:
        fn = 'data/demo_video/UpdatedIR.mp4'
    

    rfClassifier = cPickle.load(open('data/classifiers/AnimalSpecificClassifier.pkl', "rb"))
    
    cap = cv2.VideoCapture(fn)

    source_imgs = deque()
    for i in range(10):
        ret, frame = cap.read()
        source_imgs.append(cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY))      

    threadn = cv2.getNumberOfCPUs()
    pool = ThreadPool(processes = threadn)
    pending = deque()

    while True:
        while len(pending) > 0:
            res = pending.popleft().get()
            cv2.imshow('OPC Demo', res)

        if len(pending) < threadn:
            ret, frame = cap.read()
            if frame == None:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

            mask = np.zeros_like(gray)
            mask[gray > 230] = 1
            
            task = pool.apply_async(loadNextFrame, (frame, rfClassifier, mask.copy()))
            pending.append(task)

        if cv2.waitKey(30) & 0xFF == 27:
            break

    cv2.destroyAllWindows()
    cap.release()
    
