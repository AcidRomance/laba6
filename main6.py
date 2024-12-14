import tkinter as tk
from tkinter import messagebox
import sqlite3

# Создание базы данных
conn = sqlite3.connect('users.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)''')
conn.commit()


def register_user():
    username = entry_new_username.get()
    password = entry_new_password.get()

    if username and password:
        c.execute("INSERT INTO users VALUES (?, ?)", (username, password))
        conn.commit()
        messagebox.showinfo("Успех", "Пользователь зарегистрирован!")
        register_window.destroy()  # Закрыть окно регистрации после успешной регистрации
    else:
        messagebox.showwarning("Ошибка", "Пожалуйста, введите логин и пароль.")


def open_register_window():
    global register_window, entry_new_username, entry_new_password
    register_window = tk.Toplevel(root)
    register_window.title("Регистрация")

    # Задний фон окна регистрации
    register_window.configure(bg='lightblue')

    tk.Label(register_window, text="Регистрация", font=("Ink Free", 20), bg='lightblue').pack(pady=10)

    tk.Label(register_window, text="Введите логин:", bg='lightblue').pack(pady=5)
    entry_new_username = tk.Entry(register_window)
    entry_new_username.pack(pady=5)

    tk.Label(register_window, text="Введите пароль:", bg='lightblue').pack(pady=5)
    entry_new_password = tk.Entry(register_window, show='*')
    entry_new_password.pack(pady=5)

    btn_register = tk.Button(register_window, text="Зарегистрироваться", command=register_user, bg='purple', fg='white')
    btn_register.pack(pady=20)


def authorize_user():
    username = entry_username.get()
    password = entry_password.get()

    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    if c.fetchone():
        messagebox.showinfo("Успех", "Авторизация прошла успешно!")
    else:
        messagebox.showwarning("Ошибка", "Неправильный логин или пароль.")


# Основное окно
root = tk.Tk()
root.title("Авторизация")
root.configure(bg='lightblue')  # Задний фон основного окна

tk.Label(root, text="Авторизация", font=("Ink Free", 20), bg='lightblue').pack(pady=10)

tk.Label(root, text="Введите логин:", bg='lightblue').pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

tk.Label(root, text="Введите пароль:", bg='lightblue').pack(pady=5)
entry_password = tk.Entry(root, show='*')
entry_password.pack(pady=5)

btn_login = tk.Button(root, text="Авторизоваться", command=authorize_user, bg='purple', fg='white')
btn_login.pack(pady=10)

btn_register = tk.Button(root, text="Зарегистрироваться", command=open_register_window, bg='purple', fg='white')
btn_register.pack(pady=5)

root.mainloop()