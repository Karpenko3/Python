from tkinter import *
wood_count = 0
money_count = 1500
axe_level = 1

workers_inventory = []
workers_labels = []


def add_worker():
   worker_label = Label(text="👷", font=("Arial", 25))
   worker_label.pack()
   worker_label.place(x=300, y=250)
   workers_inventory.append(0)
   workers_labels.append(worker_label)


def move_worker(worker_label, destination):
   if worker_label.winfo_x() > destination.winfo_x():
       worker_label.place(x=worker_label.winfo_x() - 5, y=worker_label.winfo_y())

   if worker_label.winfo_x() < destination.winfo_x():
       worker_label.place(x=worker_label.winfo_x() + 5, y=worker_label.winfo_y())

   if worker_label.winfo_y() > destination.winfo_y():
       worker_label.place(x=worker_label.winfo_x(), y=worker_label.winfo_y() - 5)

   if worker_label.winfo_y() < destination.winfo_y():
       worker_label.place(x=worker_label.winfo_x(), y=worker_label.winfo_y() + 5)


def update_game():
   workers_count = len(workers_inventory)
   for i in range(workers_count):
       if workers_inventory[i] == 0:
           move_worker(workers_labels[i], forest)
       else:
           move_worker(workers_labels[i], factory)
       if collision(workers_labels[i], forest) and workers_inventory[i] == 0:
           workers_inventory[i] = 1
       if collision(workers_labels[i], factory) and workers_inventory[i] == 1:
           workers_inventory[i] = 0
           set_money(5)
   update_stats()
   root.after(80, update_game)


def update_stats():
   wood.config(text="Wood: " + str(wood_count))
   money.config(text="Money: " + str(money_count))
   axe.config(text="Axe Level: " + str(axe_level))


def set_wood(amount):
   global wood_count
   wood_count += amount


def set_money(amount):
   global money_count
   money_count += amount


def set_axe_level(amount):
   global axe_level
   axe_level += amount


def onKeyPress(event):
   player_x = player.winfo_x()
   player_y = player.winfo_y()
   key = event.keysym

   if key == "Right" and player_x < 580:
       player.place(x=player_x + 10, y=player_y)

   if key == "Left" and player_x > 0:
       player.place(x=player_x - 10, y=player_y)

   if key == "Up" and player_y > 50:
       player.place(x=player_x, y=player_y - 10)

   if key == "Down" and player_y < 280:
       player.place(x=player_x, y=player_y + 10)


def onKeyRelease(event):
   key = event.keysym
   if key == "e":
       chop_trees(player)
       sell_wood(player)
       upgrade_axe(player)
       buy_worker(player)
   update_stats()


def collision(object_1, object_2):
   if (object_1.winfo_x() - 20) < object_2.winfo_x() < (object_1.winfo_x() + 40):
       if (object_1.winfo_y() - 10) < object_2.winfo_y() < (object_1.winfo_y() + 50):
           return True
   return False


def chop_trees(obj):
   if collision(forest, obj):
       set_wood(axe_level)


def sell_wood(obj):
   if collision(factory, obj):
       set_money(wood_count * 0.5)
       set_wood(-wood_count)


def upgrade_axe(obj):
   if collision(axe_upgrade, obj):
       if money_count >= 50:
           set_money(-50)
           set_axe_level(1)


def buy_worker(obj):
   if collision(worker_house, obj):
       if money_count >= 150:
           add_worker()
           set_money(-150)


root = Tk()
root.geometry('600x300')
root.title('WoodChopper')
root.resizable(False, False)

wood = Label(root, text="Wood: 0")
wood.pack()

money = Label(root, text="Money: 0")
money.pack()

axe = Label(root, text="Axe Level: 1")
axe.pack()

forest = Label(root, text="🌲", font=("Arial", 40))
forest.pack()
forest.place(x=50, y=50)

factory = Label(root, text="🏭", font=("Arial", 30))
factory.pack()
factory.place(x=550, y=150)

axe_upgrade = Label(root, text="⏫", font=("Arial", 30))
axe_upgrade.pack()
axe_upgrade.place(x=50, y=250)

worker_house = Label(root, text="🏠", font=("Arial", 40))
worker_house.pack()
worker_house.place(x=300, y=235)

player = Label(root, text="🪓", font=("Arial", 30, "bold"))
player.pack()
player.place(x=150, y=150)

root.bind('<KeyPress>', onKeyPress)
root.bind('<KeyRelease>', onKeyRelease)


add_worker()
update_game()
root.mainloop()

