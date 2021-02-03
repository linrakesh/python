import cv2

image = cv2.imread('walter.jpg',1)
cv2.imshow('windows',image)
cv2.waitKey(3000)
cv2.imwrite('walter-1.png',image)
cv2.destroyAllWindows() 