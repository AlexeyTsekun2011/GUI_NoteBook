import os
import tkinter as tk
from tkinter import messagebox, simpledialog
from functions import *


os.makedirs(ARTICLES_DIR, exist_ok=True)

# Создание главного окна
wnd.title("Notebook")
wnd.geometry("600x400")
wnd.iconbitmap("icon (1) (1).ico")

frame.pack(side=tk.LEFT, fill=tk.Y)


listbox.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

btn_read = tk.Button(frame, text="Read", command=read_article)
btn_read.pack(fill=tk.X)

btn_create = tk.Button(frame, text="Create", command=create_article)
btn_create.pack(fill=tk.X)

btn_delete = tk.Button(frame, text="Delete", command=delete_article)
btn_delete.pack(fill=tk.X)

btn_save = tk.Button(wnd, text="Save", command=save_article)
btn_save.pack(fill=tk.X)


text.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

load_articles()
wnd.mainloop()
