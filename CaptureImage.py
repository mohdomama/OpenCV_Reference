import cv2

cap = cv2.VideoCapture(0)
count = 4
while True:
	_, frame = cap.read()
	cv2.rectangle(frame, (20,20), (320,320), (255,0,0), 2)

	cv2.imshow("frame", frame)

	if cv2.waitKey(20) & 0xFF == ord('c'):
	    cv2.imwrite("samples/{}.jpg".format(count), frame[20:320, 20:320])
	    print("clicked")
	    count += 1

	if cv2.waitKey(20) & 0xFF == ord('q'):
	    break

cap.release()
cv2.destroyAllWindows()