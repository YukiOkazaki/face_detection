import cv2

cascade_path = "haarcascade_frontalface_default.xml"

img = cv2.imread("lena.png")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cascade = cv2.CascadeClassifier(cascade_path)

faces = cascade.detectMultiScale(
    gray_img, scaleFactor=1.1, minNeighbors=2, minSize=(30, 30))

for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), thickness=2)

cv2.imshow("face_detection", img)
cv2.imwrite("face_detection.png", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
