import qrcode

data = input("Enter text or URL: ").strip()
filename = input("Enter filename: ").strip()

if not filename.endswith(".png"):
    filename += ".png"
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill_color='black', back_color='white')
image.save(filename)
print(f"Qrcode saved as {filename}")
