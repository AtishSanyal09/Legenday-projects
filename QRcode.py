import qrcode
import image
qr = qrcode.QRCode (
    version=30,
    box_size=10,
    border= 5
)
data = "https://www.figma.com/files/recent?fuid=1110221694093296974"
qr.add_data(data)
qr.make(fit= True)
img =qr.make_image(fill="black",black_colour="white")
img.save("test.png")