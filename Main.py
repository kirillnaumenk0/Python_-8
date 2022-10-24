from CSV_creating import creating_cap as cс
from os import path


def check(text="data1.csv"):
    if path.exists(text):
        with open("data1.csv") as file:
            print('The file exists!')
    else:
        cс()
        print('File created!')
