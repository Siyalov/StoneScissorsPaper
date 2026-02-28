from tkinter import *
from PIL import Image, ImageTk
import random

window = Tk()
window.geometry("880x600")
window.title("ROCK-PAPER-SCISSORS")

frame = Frame(window)
frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

name = Label(frame, text="Rock Paper Scissors - Player vs Computer", font=("Arial", 20, "bold"))
name.place(x=250, y=20)

label1 = Label(frame, text= "Player", font="normal 15")

label2= Label(frame, text= "VS", font="normal 15")

label3 = Label(frame, text= "Computer", font="normal 15")

def load_image(path):
    img = Image.open(path)
    img = img.resize((180, 180))   
    return ImageTk.PhotoImage(img)

rock_png = load_image("rock.png")
paper_png = load_image("paper.png")
scissors_png = load_image("scissors.png")

user_image = Label(frame, image=rock_png)
user_image.place(x=80, y=100)

comp_image = Label(frame, image=rock_png)
comp_image.place(x=600, y=100)

label4 = Label(frame, text="", font=("Arial", 18, "bold"), width=18, borderwidth=3, relief="solid")
label4.place(x=275, y=250,)

def Rock():
    user = "Rock"
    computer = random.choice(["Rock", "Paper", "Scissors"])
    user_image.config(image=rock_png)

    if user == computer:
        label4.config(text="TIE !!")
        comp_image.config(image=rock_png)
    elif computer == "Paper": 
       label4.config(text="PC WINS !!!")
       comp_image.config(image=paper_png)
    else : 
       label4.config(text="YOU WINS !!!")
       comp_image.config(image=scissors_png)

b1 = Button(frame, text="Rock", font="10", width=17, command=Rock)
b1.place(x=150, y=380)

def Paper():
    user = "Paper"
    computer = random.choice(["Rock", "Paper", "Scissors"])    
    user_image.config(image=paper_png)

    if user == computer:
        label4.config(text="TIE !!")
        comp_image.config(image=paper_png)
    elif computer == "Scissors": 
       label4.config(text="PC WINS !!!")
       comp_image.config(image=scissors_png)
    else : 
       label4.config(text="YOU WINS !!!")
       comp_image.config(image=rock_png)

b2 = Button(frame, text="Paper", font="10", width=17, command=Paper,)
b2.place(x=350, y=380)

def Scissors():
    user = "Scissors"
    computer = random.choice(["Rock", "Paper", "Scissors"])
    user_image.config(image=scissors_png)

    if user == computer:
        label4.config(text="TIE !!")
        comp_image.config(image=scissors_png)
    elif computer == "Rock": 
       label4.config(text="PC WINS !!!")
       comp_image.config(image=rock_png)
    else : 
       label4.config(text="YOU WINS !!!")
       comp_image.config(image=paper_png)

b3 = Button(frame, text="Scissors", font="10", width=17, command=Scissors )
b3.place(x=550, y=380 )

window.mainloop()