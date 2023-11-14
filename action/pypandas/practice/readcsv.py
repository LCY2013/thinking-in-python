import pandas as pd

filename = 'action/pypandas/practice/book.csv'

with open(filename, 'r', encoding='utf-8') as f:
    for line in f:
        print(line)
