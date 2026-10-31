from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title("Denomination Counter")
root.configure(bg="lightblue")
root.geometry("650x400")

upload = Image.open("cash tally.jpg")
upload = upload.resize((300,300))
image = ImageTk.PhotoImage(upload)

label = Label(root, image = image, bg="lightblue")
label.place(x = 180, y = 20)

label1 = Label(
    root,
    text = "Hey User! Welcome to the denomination Counter Application",
    bg = "lightblue"
)
label1.place(relx=0.5, y = 340, anchor=CENTER)

def msg():
    MsgBox = messagebox.showinfo(
        "Alert!",
        "Do you want to calculate the demoniation count?"
    )
    if MsgBox == "ok":
        topwin()

button1 = Button(
    root,
    text = "Let's get Started!",
    bg = "brown",
    fg = "white",
    command= msg
)
button1.place(x = 260, y = 360)

def topwin():
    top = Toplevel()
    top.title("Denomination calculator")
    top.configure(bg="light grey")
    top.geometry("600x350+50+50")

    label = Label(top, text="Enter the amount", bg="light grey")
    label.place(x = 230, y = 50)

    entry = Entry(top)
    entry.place(x = 210, y = 80)

    lbl = Label(top, text="Here are the number of notes for each denomimation", bg = "light grey")
    lbl.place(x = 140, y = 140)

    l1 = Label(top, text="2000", bg="light grey")
    l2 = Label(top, text="500", bg="light grey")
    l3 = Label(top, text="100", bg="light grey")

    l1.place(x = 180, y = 170)
    l2.place(x = 180, y = 200)
    l3.place(x = 180, y = 230)

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    t1.place(x = 250, y = 170)
    t2.place(x = 250, y = 200)
    t3.place(x = 250, y = 230)

    def calculator():
        try:

            amount = int(entry.get())

            note2000 = amount // 2000
            amount %= 2000

            note500 = amount // 500
            amount %= 500

            note100 = amount // 100

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(END, note2000)
            t2.insert(END, note500)
            t3.insert(END, note100)

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount")

    btn = Button(top, text = "calculate", bg = "brown", fg = "white", command=calculator)
    btn.place(x = 250, y = 110)



root.mainloop()