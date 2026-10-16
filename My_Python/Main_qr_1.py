import qrcode

url = input("Enter the URL: ").strip()
file_path = "/Users/pabitra/Desktop/QRCode.png"

qr = qrcode.QRCode()
qr.add_data(url)
qr.make()

img = qr.make_image()
img.save(file_path)

print("QR code generated and saved to", file_path)
