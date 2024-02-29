import base64
import numpy as np
import cv2
import time


class Utils:  
    def SaveImage(base64_string):
        image_bytes = base64.b64decode(base64_string)
        nparr = np.frombuffer(image_bytes, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        timestamp = int(time.time()*1000.0)
        cv2.imwrite("faces/" + str(timestamp) +  ".jpg", image)
        return image
   
