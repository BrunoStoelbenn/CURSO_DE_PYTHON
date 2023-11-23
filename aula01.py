import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

cap = cv.VideoCapture(0)  # cv.VideoCapture("video.avi")

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    # Capture frame
    ret, frame = cap.read()

    # Se o frame for lido corretamente, ret é True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Convertemos o quadro para escala de cinza
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Aplicamos o operador de detecção de bordas (Canny, neste caso)
    edges = cv.Canny(gray, 50, 150)

    # Exibimos o resultado
    cv.imshow('Detecção de Bordas', edges)

    if cv.waitKey(1) == ord('q'):
        break

# Quando tudo estiver feito, liberamos a captura
cap.release()
cv.destroyAllWindows()
