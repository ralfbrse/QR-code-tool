import qrcode
from PIL import Image, ImageTk


link = "sso.microsoftlog.net"

qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(link)
qr.make(fit=True)

temp = qr.make_image(fillcolor='Black', back_color='White')
temp.save('./qrcode.GIF')


