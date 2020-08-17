import cv2

img = cv2.imread("lena.png")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("gray_lena", gray_img)
cv2.imwrite("gray_lena.png", gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
