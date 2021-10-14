#A/B калькулятор

import tkinter as tk

#Закрытие программы
def do_close():
    root.destroy()

# Главное окно
root = tk.Tk()
root.geometry("280x300")
root.title("A/B калькулятор")

#Метка заголовка
lblTitle = tk.Label(text = "A/B калькулятор", font = ('Helvetica', 16, 'bold'), fg = '#0000cc')
lblTitle.place(x=55, y=20)

#Кнопка "Расчитать"
btnProcess = tk.Button(root, text="Рассчитать", font = ('Helvetica', 10, 'bold'), fg = '#0000cc')
btnProcess.place(x=25, y=250, width=90, height=30)

#Кнопка закрытия программы
btnClose = tk.Button(root, text="Закрыть", font = ('Helvetica', 10, 'bold'), command=do_close)
btnClose.place(x=160, y=250, width=90, height=30)

# mainloop
root.mainloop()
