from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Тестовое приложение")
icon = PhotoImage(file="phone.png")  # photo
root.iconphoto(False, icon)
root.geometry("500x500")  # размеры


def theend():
    root.destroy()
    print("Приложение закрыто.")


label = Label(text="Вы попали в окно пройдите ригестрацию")
btn = ttk.Button(text="Click")
btn["text"]="Продожить"
# получаем значение параметра text
btnText = btn["text"]
print(btnText)
root.protocol("WM_DELETE_WINDOW",theend)
label.pack()
btn.pack()
root.mainloop()
