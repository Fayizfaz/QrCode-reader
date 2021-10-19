import cv2
import numpy as np
from pyzbar.pyzbar import decode


img = cv2.imread("QR.png")
code = decode(img)
for qrcode in code:
    myText = qrcode.data.decode("utf-8")
    print(myText)
