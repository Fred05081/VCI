import cv2 as cv
import sys
img = cv.imread("shape.png") #lê a imagem para uma variavel
if img is None:
    sys.exit("Could not read the image.")
cv.imshow("Display window", img) #mostra a imagem
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("starry_night.png", img) #cria uma nova imagem com o nome stary_night