import cv2

img = cv2.imread("lena.png")

cv2.line(img, (10, 0), (90, 70), (0, 255, 255), thickness=4)
cv2.rectangle(img, (50, 150), (125, 200), (255, 255, 0), thickness=2)
cv2.circle(img, (190, 35), 30, (0, 255, 0), thickness=-1)

cv2.imshow("drawing", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
