import tkinter as tk
from tkinter import ttk, messagebox, filedialog

# Создаем главное окно
root = tk.Tk()
root.title("Агеев Даниил Валерьевич")  # Замените на ваше ФИО
root.geometry("500x400")

# Создаем Notebook (вкладки)
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True, padx=10, pady=10)

# === ВКЛАДКА 1: КАЛЬКУЛЯТОР ===
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text='Калькулятор')

# Поля для чисел
tk.Label(tab1, text="Число 1:").grid(row=0, column=0, padx=5, pady=5, sticky='w')
entry1 = tk.Entry(tab1)
entry1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(tab1, text="Число 2:").grid(row=1, column=0, padx=5, pady=5, sticky='w')
entry2 = tk.Entry(tab1)
entry2.grid(row=1, column=1, padx=5, pady=5)

# Выпадающий список операций
tk.Label(tab1, text="Что делаем: ").grid(row=2, column=0, padx=5, pady=5, sticky='w')
operation_var = tk.StringVar(value='+')
operations = ['+', '-', '*', '/']
operation_combo = ttk.Combobox(tab1, textvariable=operation_var, values=operations, state='readonly')
operation_combo.grid(row=2, column=1, padx=5, pady=5)

# Кнопка вычисления
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        op = operation_var.get()
        
        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                messagebox.showerror("Ошибка", "На ноль не делится")
                return
            result = num1 / num2
        
        result_label.config(text=f"Результат: {result}")
    except ValueError:
        messagebox.showerror("Ошибка", "Некорректные числа")

calc_btn = tk.Button(tab1, text="Вычислить", command=calculate)
calc_btn.grid(row=3, column=0, columnspan=2, pady=10)

# Метка для результата
result_label = tk.Label(tab1, text="Результат: ")
result_label.grid(row=4, column=0, columnspan=2, pady=5)

# === ВКЛАДКА 2: ЧЕКБОКСЫ ===
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text='Чекбоксы')

# Переменные для чекбоксов
checkbox_vars = {
    'Первый': tk.BooleanVar(),
    'Второй': tk.BooleanVar(),
    'Третий': tk.BooleanVar()
}

# Создаем чекбоксы
for i, (text, var) in enumerate(checkbox_vars.items()):
    cb = tk.Checkbutton(tab2, text=text, variable=var)
    cb.pack(anchor='w', padx=20, pady=10)

# Функция для кнопки
def show_selection():
    selected = []
    for text, var in checkbox_vars.items():
        if var.get():
            selected.append(text.lower())
    
    if selected:
        message = f"Вы выбрали: {', '.join(selected)}"
    else:
        message = "Вы ничего не выбрали"
    
    messagebox.showinfo("Ваш выбор", message)

# Кнопка показа выбора
show_btn = tk.Button(tab2, text="Показать выбор", command=show_selection)
show_btn.pack(pady=20)

# === ВКЛАДКА 3: РАБОТА С ТЕКСТОМ ===
tab3 = ttk.Frame(notebook)
notebook.add(tab3, text='Текст')

# Создаем меню
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)

# Текстовое поле
text_widget = tk.Text(tab3, wrap='word')
text_widget.pack(fill='both', expand=True, padx=10, pady=10)

# Функция загрузки файла
def load_file():
    file_path = filedialog.askopenfilename(
        title="Выберите файл",
        filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
    )
    
    if file_path:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                text_widget.delete(1.0, tk.END)
                text_widget.insert(1.0, content)
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить файл: {e}")

file_menu.add_command(label="Загрузить файл", command=load_file)


root.mainloop()







