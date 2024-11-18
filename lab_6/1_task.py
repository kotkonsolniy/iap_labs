import pandas as pd
import re

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

# Пример использования
price_list = pd.Series({"apple": 1.0, "banana": 0.5, "orange": 0.75})
purchases = {"apple": 3, "banana": 5, "orange": 2}

cheque_df = cheque(price_list, **purchases)
print("Исходный чек:")
print(cheque_df)

discounted_cheque_df = discount(cheque_df)
print("\nЧек со скидкой:")
print(discounted_cheque_df)

stats = length_stats(cheque_df)
print("\nСтатистика по длинам слов:")
print(stats)

filtered_cheques = get_long(cheque_df, min_length1=5, min_length2=6, min_length3=7, min_length4=8)

for i, filtered_cheque in enumerate(filtered_cheques, start=1):
    print(f"\nФильтрованный чек {i}:")
    print(filtered_cheque)