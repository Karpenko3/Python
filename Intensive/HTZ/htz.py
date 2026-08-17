from tkinter import *

# === ГЛОБАЛЬНІ ЗМІННІ (Наші рюкзаки) ===
wood_count = 0
money_count = 0
axe_level = 1

# === НАЛАШТУВАННЯ ВІКНА ===
root = Tk()
root.title("WoodChopper")
root.geometry("400x300")


# === МЕТОДИ-ПОМІЧНИКИ ===
def set_wood(amount):
    global wood_count
    wood_count += amount


def set_money(amount):
    global money_count
    money_count += amount


def set_axe_level(amount):
    global axe_level
    axe_level += amount


# === ІГРОВА ЛОГІКА (Перевірка зіткнень) ===
def chop_trees(player_x, player_y):
    if (forest.winfo_x() - 20) < player_x < (forest.winfo_x() + 40):
        if (forest.winfo_y() - 10) < player_y < (forest.winfo_y() + 50):
            set_wood(axe_level)


def sell_wood(player_x, player_y):
    if factory.winfo_x() - 20 < player_x < factory.winfo_x() + 40:
        if factory.winfo_y() - 10 < player_y < factory.winfo_y() + 50:
            set_money(wood_count * 0.5)
            set_wood(-wood_count)


def upgrade_axe(player_x, player_y):
    if axe_upgrade.winfo_x() - 20 < player_x < axe_upgrade.winfo_x() + 40:
        if axe_upgrade.winfo_y() - 10 < player_y < axe_upgrade.winfo_y() + 50:
            if money_count >= 50:
                set_money(-50)
                set_axe_level(1)


# === КЕРУВАННЯ ===
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


def onKeyRelease(event):
    key = event.keysym
    if key == "e" or key == "E":  # Додав "E" велику на випадок включеного CapsLock
        chop_trees(player.winfo_x(), player.winfo_y())
        wood.config(text="Wood: " + str(wood_count))

        sell_wood(player.winfo_x(), player.winfo_y())
        money.config(text="Money: " + str(money_count))

        upgrade_axe(player.winfo_x(), player.winfo_y())
        axe.config(text="Axe Level: " + str(axe_level))


# === ІНТЕРФЕЙС ТА ОБ'ЄКТИ ===
# Тексти зверху
wood = Label(root, text="Wood: 0")
wood.pack()

money = Label(root, text="Money: 0")  # Додано для коректної роботи
money.pack()

axe = Label(root, text="Axe Level: 1")  # Додано для коректної роботи
axe.pack()

# Ігрові об'єкти на полі
forest = Label(root, text="🌲", font=("Arial", 30))
forest.pack()
forest.place(x=50, y=50)

factory = Label(root, text="🏭", font=("Arial", 30))
factory.pack()
factory.place(x=300, y=150)

axe_upgrade = Label(root, text="UP!", font=("Arial", 30))
axe_upgrade.pack()
axe_upgrade.place(x=50, y=250)

# Гравець (створюється останнім, щоб бути зверху)
player = Label(root, text="🪓", font=("Arial", 20, "bold"))
player.pack()
player.place(x=150, y=150)

# === ПРИВ'ЯЗКА КЛАВІШ ТА ЗАПУСК ===
root.bind('<KeyPress>', onKeyPress)
root.bind('<KeyRelease>', onKeyRelease)

root.mainloop()  # Завжди в самому кінці!
