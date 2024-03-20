import base64
import numpy as np
import cv2
import time


class Utils:  
    def ConvertBase64ToImage(base64_string):
        image_bytes = base64.b64decode(base64_string)
        nparr = np.frombuffer(image_bytes, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        return image
    
   
