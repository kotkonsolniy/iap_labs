import pandas as pd
import re
import tkinter as tk
from tkinter import ttk, messagebox

# Задание 1
def cheque(price_list, **purchases):
    cheque_data = []

    for product, number in purchases.items():
        price = price_list.get(product, 0)
        cost = price * number
        cheque_data.append([product, price, number, cost])

    cheque_df = pd.DataFrame(cheque_data, columns=["product", "price", "number", "cost"])
    cheque_df = cheque_df.sort_values(by="product")

    return cheque_df

# Задание 2
def discount(cheque_df):
    discounted_cheque_df = cheque_df.copy()
    mask = discounted_cheque_df["number"] > 2
    discounted_cheque_df.loc[mask, "cost"] = discounted_cheque_df.loc[mask, "cost"] * 0.5

    return discounted_cheque_df

# Задание 3
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    words = text.split()
    words.sort()

    return words

def length_stats(cheque_df):
    words_lengths = []

    for index, row in cheque_df.iterrows():
        product = row["product"]
        words = preprocess_text(product)
        for word in words:
            words_lengths.append((word, len(word)))

    words_lengths_series = pd.Series(dict(words_lengths))

    return words_lengths_series

# Задание 4
def get_long(cheque_df, min_length1=5, min_length2=5, min_length3=5, min_length4=5):
    filtered_cheque_df1 = cheque_df[cheque_df["product"].str.len() >= min_length1]
    filtered_cheque_df2 = cheque_df[cheque_df["product"].str.len() >= min_length2]
    filtered_cheque_df3 = cheque_df[cheque_df["product"].str.len() >= min_length3]
    filtered_cheque_df4 = cheque_df[cheque_df["product"].str.len() >= min_length4]

    return (filtered_cheque_df1, filtered_cheque_df2, filtered_cheque_df3, filtered_cheque_df4)

# Функция для отображения DataFrame в текстовом поле
def display_dataframe(df, text_widget):
    text_widget.delete(1.0, tk.END)
    text_widget.insert(tk.END, df.to_string())

# Функция для отображения Series в текстовом поле
def display_series(series, text_widget):
    text_widget.delete(1.0, tk.END)
    text_widget.insert(tk.END, series.to_string())

# Функция для обработки ввода и выполнения заданий
def process_input():
    try:
        price_list_input = price_list_entry.get()
        purchases_input = purchases_entry.get()

        price_list = eval(price_list_input)
        purchases = eval(purchases_input)

        cheque_df = cheque(pd.Series(price_list), **purchases)
        display_dataframe(cheque_df, cheque_text)

        discounted_cheque_df = discount(cheque_df)
        display_dataframe(discounted_cheque_df, discount_text)

        stats = length_stats(cheque_df)
        display_series(stats, stats_text)

        filtered_cheques = get_long(cheque_df, min_length1=5, min_length2=6, min_length3=7, min_length4=8)
        for i, filtered_cheque in enumerate(filtered_cheques, start=1):
            display_dataframe(filtered_cheque, filtered_texts[i-1])

    except Exception as e:
        messagebox.showerror("Ошибка", str(e))

# Создание главного окна
root = tk.Tk()
root.title("Анализ данных")

# Создание вкладок
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# Вкладка 1: Исходный чек
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Исходный чек")

price_list_label = ttk.Label(tab1, text="Прайс-лист (словарь):")
price_list_label.pack()
price_list_entry = ttk.Entry(tab1, width=50)
price_list_entry.pack()
price_list_entry.insert(0, "{'apple': 1.0, 'banana': 0.5, 'orange': 0.75}")

purchases_label = ttk.Label(tab1, text="Покупки (словарь):")
purchases_label.pack()
purchases_entry = ttk.Entry(tab1, width=50)
purchases_entry.pack()
purchases_entry.insert(0, "{'apple': 3, 'banana': 5, 'orange': 2}")

process_button = ttk.Button(tab1, text="Обработать", command=process_input)
process_button.pack()

cheque_text = tk.Text(tab1, height=10, width=50)
cheque_text.pack()

# Вкладка 2: Чек со скидкой
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Чек со скидкой")

discount_text = tk.Text(tab2, height=10, width=50)
discount_text.pack()

# Вкладка 3: Статистика по длинам слов
tab3 = ttk.Frame(notebook)
notebook.add(tab3, text="Статистика по длинам слов")

stats_text = tk.Text(tab3, height=10, width=50)
stats_text.pack()

# Вкладка 4: Фильтрованные чеки
tab4 = ttk.Frame(notebook)
notebook.add(tab4, text="Фильтрованные чеки")

filtered_texts = [tk.Text(tab4, height=10, width=50) for _ in range(4)]
for text_widget in filtered_texts:
    text_widget.pack()

# Запуск главного цикла
root.mainloop()