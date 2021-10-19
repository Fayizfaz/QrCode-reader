import cv2
import numpy as np
from pyzbar.pyzbar import decode


cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:
    success,img = cap.read()
    
    code = decode(img)
    for qrcode in code:
        myText = qrcode.data.decode("utf-8")
        pts = np.array([qrCode.polygon],np.int32)
        cv2.polylines(img,[pts],True,(0,255,0),3)
        print(myText)

    cv2.imshow("Result image", img)
    cv2.waitKey(2)
