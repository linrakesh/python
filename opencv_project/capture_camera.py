import cv2
capture = cv2.VideoCapture(1)

while True:
  ret, frame = capture.read(1)
  cv2.imshow('image',frame)
  if cv2.waitKey(1) & 0xFF==ord('q'):
    break
capture.release()