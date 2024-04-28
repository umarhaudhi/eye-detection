import cv2

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
cap = cv2.VideoCapture(0)

# atur size video
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

while True: 
  
    _, img = cap.read()

    # ubah mata ke hitam putih agar bisa dibaca dengan program haarcascade
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # haarcascade, detect eye gray
    eyes = eye_cascade.detectMultiScale(gray, 1.1, 4)

    # kotak
    for (x, y, w, h) in faces:
        cv2.rectangle(img, 
                      (x, y), 
                      (x+w, y+h), 
                      (0, 255, 0), 
                      2)
    img = cv2.resize(img,(1280,720)) # atur size
    cv2.imshow('img', img)

    # close camera
    if cv2.waitKey(30) & 0xFF == ord(' '):
        break

cap.release() # stop camera/ program
cv2.destroyAllWindows() # untuk destroy all window





       


