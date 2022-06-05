import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

img = cv2.imread('captcha.jpg')
dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)

captcha = pytesseract.image_to_string(dst)
print(captcha)