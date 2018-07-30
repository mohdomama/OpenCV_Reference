import cv2
import numpy as np

text_palm = 'Palm'
text_fist = 'Fist'
fist_cas = cv2.CascadeClassifier('cascades/harrcascade_fist2.xml')
palm_cas = cv2.CascadeClassifier('cascades/harrcascade_palm.xml')

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    fists = fist_cas.detectMultiScale(
        frame, scaleFactor=1.3, minNeighbors=4, minSize=(80, 80))
    palms = palm_cas.detectMultiScale(
        frame, scaleFactor=1.2, minNeighbors=4, minSize=(120, 120))

    for (x, y, w, h) in fists:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(
            frame,
            text_fist,
            (x, y + h + 30), 
            cv2.FONT_HERSHEY_DUPLEX, 
            1.3, 
            (0, 0, 0), 
            lineType=cv2.LINE_AA)

        print('Fist coordinates: {} and {}'.format(x, y))

    for (x, y, w, h) in palms:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(
            frame,
            text_palm,
            (x, y + h + 30), 
            cv2.FONT_HERSHEY_DUPLEX, 
            1.3, 
            (0, 0, 0), 
            lineType=cv2.LINE_AA)

        print('Palm coordinates: {} and {}'.format(x, y)) 

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    

cap.release()
cv2.destroyAllWindows() 