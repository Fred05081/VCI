
import cv2 as cv
cap = cv.VideoCapture('unityvideo.mp4')
while cap.isOpened():
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame', gray)
    if cv.waitKey(2) == ord('q'): #alterar o valor x waitkey(x) para alterar a
                        # velocidade com que o video unityvideo.mp4 é reproduzido
        break
cap.release()
cv.destroyAllWindows()