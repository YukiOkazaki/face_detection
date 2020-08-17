import cv2

cascade_path = "haarcascade_frontalface_default.xml"

img = cv2.imread("lena.png")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cascade = cv2.CascadeClassifier(cascade_path)

faces = cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=2, minSize=(30, 30))

for x, y, w, h in faces:
    center = (int(x + w / 2), int(y + h / 2))
    radius = int((w + h) / 4)
    cv2.circle(img, center, radius, (0, 255, 255), thickness=-1)

cv2.imshow("fill", img)
cv2.imwrite("fill.png", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
