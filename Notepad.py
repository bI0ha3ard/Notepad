import tkinter as tk
from tkinter import filedialog
import os

class GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Графический блокнот")
        self.text = tk.Text(self.master, undo=True)
        self.text.pack(fill=tk.BOTH, expand=True)
        self.create_menu()

    def create_menu(self):
        self.menu = tk.Menu(self.master)
        self.master.config(menu=self.menu)

        file_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Файл", menu=file_menu)
        file_menu.add_command(label="Открыть", command=self.open_file)
        file_menu.add_command(label="Сохранить", command=self.save_file)

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "r") as f:
                file_contents = f.read()
                self.text.delete("1.0", tk.END)
                self.text.insert(tk.END, file_contents)

    def save_file(self):
        file_path = filedialog.asksaveasfilename()
        if file_path:
            with open(file_path, "w") as f:
                f.write(self.text.get("1.0", tk.END))

if __name__ == "__main__":
    root = tk.Tk()

    icon_path = os.path.abspath("assets/icon.ico")

    if os.path.exists(icon_path):
        root.iconbitmap(icon_path)

    gui = GUI(root)
    root.mainloop()
