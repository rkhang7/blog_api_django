import base64
import numpy as np
import cv2
import time
import os
import glob


class Utils:  
    def ConvertBase64ToImage(base64_string):
        image_bytes = base64.b64decode(base64_string)
        nparr = np.frombuffer(image_bytes, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
 
        return image
    def CountFilesById(folder_path, id):
        if not os.path.isdir(folder_path):
            return "Invalid folder path"

        # This is our counter
        count = 0
        for file in os.listdir(folder_path):
            if(file.startswith(id)):
                count += 1
        return count
    
   
