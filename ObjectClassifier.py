from sklearn.ensemble import RandomForestClassifier
from skimage import img_as_uint
from skimage import morphology
from scipy import ndimage
import cPickle, os, cv2

class ObjectClassifier(object):
    def __init__(self, rfc=None, classifier_file=None):
        self.rfc = None
        if rfc is not None:
            self.rfc = rfc
        elif classifier_file is not None:
            self.rfc = cPickle.load(open(classifier_file, "rb"))

        self.training_features = []
        self.training_responses = []
        self.trained = False

    def runTrainingRoutine(self, training_image_dir):
        # Open and store all training images
        image_set = []
        for fn in os.listdir(training_image_dir):
            img = cv2.imread(os.path.join(training_image_dir, fn))
            if img is not None:
                image_set.append(img)


        for image in image_set:
            gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
            contours = self.getImageContours(gray)

            ### -------------------- LEFT OFF HERE ----------------------- ###

            

    def getImageContours(self, gray):
        ret, thresh = cv2.threshold(gray, 220, 255, cv2.THRESH_TOZERO)
        fill = ndimage.binary_fill_holes(thresh)

        clean = morphology.remove_small_objects(fill, 12)
        clean = img_as_uint(clean).astype(np.dtype('uint8'))
        contour_image = clean.copy()

        contours, hierarchy = cv2.findContours(contour_image, cv2.RETR_LIST, cv2.CHAIN_APPROX_TC89_KCOS)
        return contours
