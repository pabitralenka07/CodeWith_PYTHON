import pyqrcode 
from PIL import Image 
link = input("Enter anything to generate qr :")
qr_code = pyqrcode.create(link)
qr_code.png("QRCode.png", scale=5)
Image.open("QRCode.png")
