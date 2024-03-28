import base64
import numpy as np
import cv2
import time
import os
import glob
from PIL import Image
detector= cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


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
    
    def getImagesAndLabels(path):
        # Lấy tất cả các file trong thư mục
        try:
            imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
        except OSError as e:
             print("Đã xảy ra lỗi khi cố gắng truy cập thư mục:", e)
        #create empth face list
        faceSamples=[]
        #create empty ID list
        Ids=[]
        #now looping through all the image paths and loading the Ids and the images
        for imagePath in imagePaths:
            if (imagePath[-3:]=="jpg"):
                print(imagePath[-3:])
            #loading the image and converting it to gray scale
                pilImage=Image.open(imagePath).convert('L')
            #Now we are converting the PIL image into numpy array
                imageNp=np.array(pilImage,'uint8')
            #getting the Id from the image
                Id=int(os.path.split(imagePath)[-1].split(".")[1])
            # extract the face from the training image sample
                faces=detector.detectMultiScale(imageNp)
            #If a face is there then append that in the list as well as Id of it
                for (x,y,w,h) in faces:
                    faceSamples.append(imageNp[y:y+h,x:x+w])
                    Ids.append(Id)
        return faceSamples,Ids
    
   
