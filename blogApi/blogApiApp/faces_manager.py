
import cv2
import time

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
    
    def Detect(image, id):
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        # Convert the image to grayscale (face detection works on grayscale images)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Detect faces in the image
        faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        # Iterate over detected faces and crop them
        for i, (x, y, w, h) in enumerate(faces):
             # Crop the face region from the image
            cropped_face = image[y:y+h, x:x+w]
    
             # Convert the cropped face to grayscale
            cropped_face_gray = cv2.cvtColor(cropped_face, cv2.COLOR_BGR2GRAY)
    
             # Save the cropped face as a new image
            timestamp = int(time.time()*1000.0)
            cv2.imwrite("faces/" + str(timestamp) +  ".jpg", cropped_face_gray)

            # Draw rectangle around the detected face on the original image
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)


    def Detect2(id):
        # Load the pre-trained face cascade classifier
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        # Load the image
        image = cv2.imread('khang.jpg')

# Convert the image to grayscale (face detection works on grayscale images)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
        faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Iterate over detected faces and crop them
        for i, (x, y, w, h) in enumerate(faces):
    # Crop the face region from the image
            cropped_face = image[y:y+h, x:x+w]

            cropped_face_gray = cv2.cvtColor(cropped_face, cv2.COLOR_BGR2GRAY)
    
    # Save the cropped face as a new image
            cv2.imwrite('faces/' + id +  "/" +   f'face_{i}.jpg', cropped_face_gray)

    # Draw rectangle around the detected face on the original image
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

            break

