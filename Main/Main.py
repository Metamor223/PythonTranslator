import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program'

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    cv2.putText(frame, text, (10,50), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,255,255), 2)
    cv2.imshow('Real-Time Text Recognition', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()