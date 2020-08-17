import cv2

cascade_path = "haarcascade_frontalface_default.xml"

img = cv2.imread("lena.png")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

overlay = cv2.imread("smile.png", cv2.IMREAD_UNCHANGED)
overlay = cv2.cvtColor(overlay, cv2.COLOR_RGB2RGBA)

cascade = cv2.CascadeClassifier(cascade_path)

faces = cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=2, minSize=(30, 30))

for x, y, w, h in faces:
    resize_overlay = cv2.resize(overlay, (w, h), interpolation=cv2.INTER_NEAREST)
    alpha = resize_overlay[:, :, 3:] / 255
    img[y: y + h, x: x + w] = img[y: y + h, x: x + w] * (1 - alpha) + resize_overlay[:, :, :3] * alpha

cv2.imshow("overlay", img)
cv2.imwrite("overlay.png", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
