import cv2

cap = cv2.VideoCapture(0)
count = 1
pre = input('Enter image prefix:')
while True:
    _, frame = cap.read()
    print('Number of pics: ', count)
    cv2.imshow("frame", frame)

    key = cv2.waitKey(20)

    if  key & 0xFF == ord('c'):
        cv2.imwrite("samples/{}{}.jpg".format(pre, count), frame)
        print("clicked")
        count += 1

    elif key & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
