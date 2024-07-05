from tkinter import *
window = Tk()
def draw_rectangle(Canvas,rectangle):
    mycan= Canvas
    mycan.pack(pady=20)

window.title("Canvas")
window.geometry("500x500")
mycan = Canvas(window,width="300",height="200",bg="blue")
x= mycan.create_rectangle(50,50,250,200,fill="red")

draw_rectangle(mycan,x)
window.mainloop()