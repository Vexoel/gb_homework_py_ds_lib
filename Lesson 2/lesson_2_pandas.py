# Lesson 2 “Работа с данными в Pandas”

# Task 1
print('Task 1')

import pandas as pd
import numpy as np

dic = {
    "author_id": [1, 2, 3],
    "author_name": ['Тургенев', 'Чехов', 'Островский']
}
authors = pd.DataFrame(dic)
print('authors')
print(authors)

print()

dic = {
    "author_id": [1, 1, 1, 2, 2, 3, 3],
    "book_title": ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
    "price": [450, 300, 350, 500, 450, 370, 290]
}
books = pd.DataFrame(dic)
print('books')
print(books)

print()

# Task 2
print('Task 2')
authors_price = authors.merge(books, on='author_id')
print('authors_price')
print(authors_price)

print()

# Task 3
print('Task 3')
top5 = authors_price.nlargest(5, "price")
print('top5')
print(top5)

print()

# Task 4
print('Task 4')
authors_stat = authors_price.groupby("author_name").agg(min_price=pd.NamedAgg(column='price', aggfunc='min'),
                                                        max_price=pd.NamedAgg(column='price', aggfunc='max'),
                                                        mean_price=pd.NamedAgg(column='price', aggfunc='mean'))
print('authors_stat')
print(authors_stat)

print()

# Task 5
print('Task 5')
authors_price["cover"] = ['твердая', 'мягкая', 'мягкая', 'твердая', 'твердая', 'мягкая', 'мягкая']
print('authors_price')
print(authors_price)

print()

book_info = pd.pivot_table(authors_price, values='price', index='author_name', columns=['cover'], aggfunc=np.sum, fill_value=0)
print('book_info')
print(book_info)

print()

book_info.to_pickle("book_info.pkl")
book_info2 = pd.read_pickle("book_info.pkl")
print('book_info2')
print(book_info2)

print()

merged = book_info.merge(book_info2, indicator=True, how='outer')
print('check')
print(merged[(merged['_merge'] == 'right_only') | (merged['_merge'] == 'left_only')])
