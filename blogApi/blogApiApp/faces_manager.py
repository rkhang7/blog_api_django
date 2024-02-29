
import cv2

# faceDetect = None
# recognizer = None
class FacesManager:
  
    # def __init__(self):
        # Khởi tạo bộ phát hiện khuôn mặt
        # faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');

        # # Khởi tạo bộ nhận diện khuôn mặt
        # recognizer = cv2.face.LBPHFaceRecognizer_create()
        # recognizer.read('recognizer/trainner.yml')

    def Recognizer(img):
        faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
        # Khởi tạo bộ nhận diện khuôn mặt
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read('recognizer/trainner.yml')
         # Phát hiện các khuôn mặt trong ảnh camera
         # Chuyển ảnh về xám
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        # faces=faceDetect.detectMultiScale(gray,1.3,5);
        id,dist=recognizer.predict(gray)

        return id,dist