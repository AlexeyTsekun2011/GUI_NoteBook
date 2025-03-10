import os
import tkinter as tk
from tkinter import messagebox, simpledialog

wnd = tk.Tk()
frame = tk.Frame(wnd)
listbox = tk.Listbox(frame, width=30, height=20)
ARTICLES_DIR = "articles"
os.makedirs(ARTICLES_DIR, exist_ok=True)
current_file_path = None  # Глобальная переменная для хранения пути текущей статьи
text = tk.Text(wnd, wrap=tk.WORD)



def load_articles():
    """Загружает список статей из папки"""
    listbox.delete(0, tk.END)
    for filename in os.listdir(ARTICLES_DIR):
        if filename.endswith(".txt"):
            listbox.insert(tk.END, filename[:-4])


def read_article():
    """Читает и редактирует выбранную статью"""
    global current_file_path
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Error", "Choose entry to read")
        return

    article_name = listbox.get(selected[0])
    current_file_path = os.path.join(ARTICLES_DIR, article_name + ".txt")

    with open(current_file_path, "r", encoding="utf-8") as file:
        text.delete("1.0", tk.END)
        text.insert(tk.END, file.read())


def save_article():
    """Сохраняет изменения в статье"""
    if current_file_path:
        with open(current_file_path, "w", encoding="utf-8") as file:
            file.write(text.get("1.0", tk.END))
        messagebox.showinfo("Success", "Entry saved")
    else:
        messagebox.showwarning("Error", "There is no open entry to save")


def create_article():
    """Создает новую статью"""
    article_name = simpledialog.askstring("New entry", "Enter a new entry")
    if not article_name:
        return

    file_path = os.path.join(ARTICLES_DIR, article_name + ".txt")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("Write here...")

    load_articles()


def delete_article():
    """Удаляет выбранную статью"""
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Error", "Choose entry to delete")
        return

    article_name = listbox.get(selected[0])
    file_path = os.path.join(ARTICLES_DIR, article_name + ".txt")
    os.remove(file_path)
    load_articles()