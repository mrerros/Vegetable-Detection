import cv2

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    cv2.imshow("CAM", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite("all/model.jpg", frame)
        print("Fotoğraf Çekildi")
    
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()

