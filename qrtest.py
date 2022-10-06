import qrcode
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
# Top level window
root = Tk()
root.title("QR code generator")
root.geometry("700x700")

# text box
inputtxt = Text(root, height=5, width=20)
inputtxt.pack()


def GenQR():
    link = inputtxt.get(1.0, "end-1c")

    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(link)
    qr.make(fit=True)

    temp = qr.make_image(fillcolor='Black', back_color='White')
    temp.save('./qrcode.GIF')

    image = Image.open('./qrcode.GIF')
    resize_image = image.resize((300, 300))
    img = ImageTk.PhotoImage(resize_image)

    outCode.create_image(300, 300, image=img)


showCodeBtn = Button(root, text="Generate QR code", command=GenQR)
showCodeBtn.pack()

outCode = Canvas(root, width=500, height=500)
outCode.pack()
root.mainloop()
