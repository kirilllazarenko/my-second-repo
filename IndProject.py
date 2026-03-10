import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk



class SimpleWidgetManager:
    def __init__(self):
        self.widgets_to_keep = []

    def keep(self, widget):
        self.widgets_to_keep.append(widget)
        return widget

    def clear_all_except_kept(self, root):
        for widget in root.winfo_children():
            if widget not in self.widgets_to_keep:
                try:
                    widget.destroy()
                except:
                    pass

wm = SimpleWidgetManager()

root = tk.Tk()
root.title("Акинатор")
root.geometry("500x900")
root.resizable(False, False)
# фон
image = Image.open("akinator.jpg")
image = image.resize((500, 700))
photo = ImageTk.PhotoImage(image)
root.photo = photo
background_label = tk.Label(root, image=photo)
background_label.place(x=1, y=80, relwidth=1, relheight=1)
wm.keep(background_label)
def win():
    global background_label
    wm.clear_all_except_kept(root)
    try:
        background_label.destroy()
    except:
        pass
    question_label = tk.Label(root, text="Я отгадал Вас, Олег Игоревич!", font=("Arial", 14))
    question_label.pack(pady=20)
    image2 = Image.open("Oleg.jpg")
    image2 = image2.resize((500, 700))
    photo2 = ImageTk.PhotoImage(image2)
    background_label = tk.Label(root, image=photo2)
    background_label.place(x=1, y=50, relwidth=1, relheight=1)
    wm.keep(background_label)
    root.photo2 = photo2
def y():
    wm.clear_all_except_kept(root)
    question_label = tk.Label(root, text="Вас зовут Олег?", font=("Arial", 14))
    question_label.pack(pady=20)
    button_frame = tk.Frame(root)
    button_frame.pack()
    btn1 = tk.Button(button_frame, text="ДА", bg="lightgreen",
                            font=("Arial", 12), width=10, command=win)
    btn1.pack(side="left", padx=10)
    btn2 = tk.Button(button_frame, text="НЕТ", bg="lightcoral",
                            font=("Arial", 12), width=10, command=no)
    btn2.pack(side="left", padx=10)
def ye():
    wm.clear_all_except_kept(root)
    question_label = tk.Label(root, text="Вы преподаватель?", font=("Arial", 14))
    question_label.pack(pady=20)
    button_frame = tk.Frame(root)
    button_frame.pack()
    btn1 = tk.Button(button_frame, text="ДА", bg="lightgreen",
                            font=("Arial", 12), width=10, command=y)
    btn1.pack(side="left", padx=10)
    btn2 = tk.Button(button_frame, text="НЕТ", bg="lightcoral",
                            font=("Arial", 12), width=10, command=no)
    btn2.pack(side="left", padx=10)
def yes():
    wm.clear_all_except_kept(root)
    question_label = tk.Label(root, text="Вы мужского пола?", font=("Arial", 14))
    question_label.pack(pady=20)
    button_frame = tk.Frame(root)
    button_frame.pack()
    btn1 = tk.Button(button_frame, text="ДА", bg="lightgreen",
                            font=("Arial", 12), width=10, command=ye)
    btn1.pack(side="left", padx=10)
    btn2 = tk.Button(button_frame, text="НЕТ", bg="lightcoral",
                            font=("Arial", 12), width=10, command=no)
    btn2.pack(side="left", padx=10)
def no():
    wm.clear_all_except_kept(root)
    question_label = tk.Label(root, text="Ты обманул меня, начинаем заново! Готов?", font=("Arial", 14))
    question_label.pack(pady=20)
    button_frame = tk.Frame(root)
    button_frame.pack()
    btn1 = tk.Button(button_frame, text="ДА", bg="lightgreen",
                            font=("Arial", 12), width=10, command=main)
    btn1.pack(side="left", padx=10)
def main():
    question_label = tk.Label(root, text="Вы человек?", font=("Arial", 14))
    question_label.pack(pady=20)
    button_frame = tk.Frame(root)
    button_frame.pack()
    btn1 = tk.Button(button_frame, text="ДА", bg="lightgreen",
                            font=("Arial", 12), width=10, command=yes)
    btn1.pack(side="left", padx=10)
    btn2 = tk.Button(button_frame, text="НЕТ", bg="lightcoral",
                            font=("Arial", 12), width=10, command=no)
    btn2.pack(side="left", padx=10)

main()
root.mainloop()
