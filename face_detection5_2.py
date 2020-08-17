import cv2

cascade_path = "haarcascade_frontalface_default.xml"

img = cv2.imread("lena.png")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cascade = cv2.CascadeClassifier(cascade_path)

faces = cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=2, minSize=(30, 30))

for x, y, w, h in faces:
    ratio = 0.1
    mosaic = cv2.resize(img[y: y + h, x:x + w], None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    img[y: y + h, x: x + w] = cv2.resize(mosaic, (w, h), interpolation=cv2.INTER_NEAREST)

cv2.imshow("mosaic", img)
cv2.imwrite("mosaic.png", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
