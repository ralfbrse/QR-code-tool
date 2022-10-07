
from turtle import color
import qrcode
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
# Top level window
root = Tk()
root.title("QR code generator")
root.geometry("400x250")


# label
inputLabel = Label(root, text="Insert link/message")
inputLabel.grid(column=0, row=0, pady=2, padx=2)

# text box
inputtxt = Text(root, height=3, width=20)
inputtxt.grid(column=0, row=1, pady=2, padx=2)


def GenQR():
    link = inputtxt.get(1.0, "end-1c")

    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(link)
    qr.make(fit=True)

    temp = qr.make_image(fillcolor='Black', back_color='White')
    temp.save('./qrcode.GIF')

    image = Image.open('./qrcode.GIF')
    resize_image = image.resize((200, 200))
    img = ImageTk.PhotoImage(resize_image)

    outCode.create_image(100, 100, image=img)


showCodeBtn = Button(root, text="Generate QR code", command=GenQR)
showCodeBtn.grid(column=0, row=2)

outCode = Canvas(root, width=200, height=200)
outCode.grid(column=1, row=0, columnspan=6, rowspan=6)
root.mainloop()
