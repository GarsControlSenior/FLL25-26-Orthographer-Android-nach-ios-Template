import cv2
import numpy as np

class OpenCVProcessor:

    def remove_shadows(self, image_path):
        img = cv2.imread(image_path)
        rgb_planes = cv2.split(img)

        result_planes = []
        for plane in rgb_planes:
            dilated = cv2.dilate(plane, np.ones((7,7), np.uint8))
            bg = cv2.medianBlur(dilated, 21)
            diff = 255 - cv2.absdiff(plane, bg)
            result_planes.append(diff)

        result = cv2.merge(result_planes)
        cv2.imwrite("processed.jpg", result)
        return "processed.jpg"