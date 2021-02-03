import cv2
image = cv2.imread('walter.jpg',1)
cv2.line(image,(0,0),(400,400),(255,0,0),5)
cv2.rectangle(image,(100,200),(400,400),(0,255,0),10)
cv2.circle(image,(200,200),100,(0,0,255),-8)
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(image,'Hello rakesh',(150,250),font,2,(255,255,0),cv2.LINE_8)
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()