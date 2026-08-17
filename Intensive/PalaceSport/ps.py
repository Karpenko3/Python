from tkinter import *
wood_count = 0
money_count = 0
axe_level = 1

def set_wood(amount):
    global wood_count
    wood_count += amount

def set_money(amount):
    global money_count
    money_count += amount

def set_axe_level(amount):
    global axe_level
    axe_level += amount

root = Tk()
root.geometry('400x300')
root.title('WoodChopper')
root.resizable(False, False)

def onKeyRelease(event):
    key = event.keysym
    if key == "e":
        chop_trees(player.winfo_x(), player.winfo_y())
        wood.config(text = "Wood: " +str(wood_count))

def onKeyPress(event):
   player_x = player.winfo_x()
   player_y = player.winfo_y()
   key = event.keysym

   if key == "Right" and player_x < 380:
       player.place(x=player_x + 10, y=player_y)

   if key == "Left" and player_x > 0:
       player.place(x=player_x - 10, y=player_y)

   if key == "Up" and player_y > 50:
       player.place(x=player_x, y=player_y - 10)

   if key == "Down" and player_y < 280:
       player.place(x=player_x, y=player_y + 10)

wood = Label(root, text="Wood: 0")
wood.pack()

money = Label(root, text="Money: 0")
money.pack()

axe = Label(root, text="Axe Level: 1")
axe.pack()

forest = Label(root, text="🌲", font= ("Arial", 30))
forest.pack()
forest.place(x=50, y=50)

factory = Label(root, text="🏪", font=("Arial", 30))
factory.pack()
factory.place(x=300, y=150)

axe_upgrade = Label(root, text="🆙", font=("Arial", 30))
axe_upgrade.pack()
axe_upgrade.place(x=50, y=250)

player = Label(root, text="🪓", font=("Arial", 20, "bold"))
player.pack()
player.place(x=150, y=150)

root.bind('<KeyPress>', onKeyPress)
root.bind('<KeyRelease>', onKeyRelease)
root.mainloop()
root.mainloop()

