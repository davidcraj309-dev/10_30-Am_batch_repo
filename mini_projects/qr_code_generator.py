import qrcode
print()
print("---------QR-CODE GENERATOR----------")
print()
data = input("Enter the Text or Url: ").strip()
filename = input("Enter the filename: ").strip()


qr =  qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill_color ='black',back_color="white")
image.save(filename)
print(f"QR  code saved as {filename}")







