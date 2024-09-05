import tkinter as tk
from PIL import Image, ImageTk
import random

root = tk.Tk()
root.title ("Send Crush Me")
root.geometry("1200x800")

img = Image.open("img/bg.jpg")
bg_img = ImageTk.PhotoImage(img)

canvas = tk.Canvas(root,width=1200, height= 800)

canvas.pack(fill="both", expand=True)
canvas.create_image(0,0,ancho = "nw", image = bg_img)

canvas.create_text(600,100, text="Thật ra tớ thích cậu lâu rồi <33", fill = "#FF99FF", font = ("Helvetica", 24, "bold"))
canvas.create_text(600,140, text="Đôngf ý làm ny tớ nhé !!", fill = "#FF99FF", font = ("Helvetica", 24, "bold"))

def but1():
    nw = tk.Toplevel(root)
    nw.geometry("500x500")
    nw.title("Fb tớ nè ")
    image = Image.open("img/qr.png")
    image_tk = ImageTk.PhotoImage(image)
    image_label = tk.Label(nw, image = image_tk)
    image_label.image = image_tk
    image_label.pack(pady = 20)

def but2(event):
    nw_x = random.randint(0,1100)
    nw_y = random.randint(0,700)
    button2.place(x=nw_x, y = nw_y)

button1 = tk.Button(root,text = "ĐỒNG Ý", command = but1, font = ("Helvetica", 18), padx = 20, pady = 10)
button1.place(x = 450, y =200)

button2 = tk.Button(root,text = "ĐÉO", font = ("Helvetica", 18), padx = 20, pady = 10)
button2.place(x = 610, y =200)
button2.bind("<Enter>", but2)
root.mainloop()