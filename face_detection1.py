import cv2

img = cv2.imread("lena.png")

cv2.imshow("lena", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
