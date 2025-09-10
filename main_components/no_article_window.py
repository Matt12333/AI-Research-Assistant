import tkinter as tk
from tkinter import Label

def no_article_window():
    window = tk.Tk()

    window.title("Article Update")
    window.geometry('350x200')

    label = Label(window,
                text='No articles today',
                fg='black',
                font=('Arial', 22, 'bold'))

    label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    window.mainloop()