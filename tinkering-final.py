import Game
import tkinter

root = tkinter.Tk()

root.title("Just Exercise")
root.geometry("500x500")

# Configure the rows and columns
tkinter.Grid.rowconfigure(root, 0, weight=1)
tkinter.Grid.rowconfigure(root, 1, weight=1)
tkinter.Grid.rowconfigure(root, 2, weight=1)
tkinter.Grid.rowconfigure(root, 3, weight=1)

tkinter.Grid.columnconfigure(root, 0, weight=1)
tkinter.Grid.columnconfigure(root, 1, weight=1)

# create name box and label
EnterName = tkinter.Label(root, text="ENTER YOUR NAME BELOW:")
EnterName.grid(sticky="nsew")
Name = tkinter.Entry(root)
Name.grid(sticky="nsew")


# funcs for buttons
def curlsCom():
    Leader = Game.TheCode(Name.get(), 1)
    Name.delete(0, tkinter.END)
    root2 = tkinter.Tk()
    root2.geometry("200x300")
    root2.title("Curls Leader Board")
    tkinter.Label(root2, text=Leader).pack()
    root2.mainloop()

def pushCom():
    Leader = Game.TheCode(Name.get(), 2)
    Name.delete(0, tkinter.END)
    root2 = tkinter.Tk()
    root2.geometry("200x300")
    root2.title("Push ups Leader Board")
    tkinter.Label(root2, text=Leader).pack()
    root2.mainloop()


def squartCom():
    Leader = Game.TheCode(Name.get(), 3)
    Name.delete(0, tkinter.END)
    root2 = tkinter.Tk()
    root2.geometry("200x300")
    root2.title("Squats Leader Board")
    tkinter.Label(root2, text=Leader).pack()
    root2.mainloop()


def lungeCom():
    Leader = Game.TheCode(Name.get(), 4)
    Name.delete(0, tkinter.END)
    root2 = tkinter.Tk()
    root2.geometry("200x250")
    root2.title("Lunges Leader Board")
    tkinter.Label(root2, text=Leader).pack()
    root2.mainloop()


# Enter 4 buttons
curls = tkinter.Button(root, text="CURLS COUNTER", command=curlsCom)
curls.grid(sticky="nsew")
push = tkinter.Button(root, text="PUSH UPS COUNTER", command=pushCom)
push.grid(sticky="nsew")
squats = tkinter.Button(root, text="SQUATS COUNTER", command=squartCom)
squats.grid(sticky="nsew")
lunges = tkinter.Button(root, text="LUNGES COUNTER", command=lungeCom)
lunges.grid(sticky="nsew")

# Grid the buttons onto the screen
EnterName.grid(row=0, column=0, columnspan=2)
Name.grid(row=1, column=0, columnspan=2)
curls.grid(row=2, column=0)
push.grid(row=2, column=1)
squats.grid(row=3, column=0)
lunges.grid(row=3, column=1)

root.mainloop()
