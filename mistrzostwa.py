import pandas as pd

# Dane z zwycięzcami Mistrzostw Świata w piłce nożnej
data = {
    'Rok': [2002, 2006, 2010],
    'Zwycięzca': ['Brazylia', 'Włochy', 'Hiszpania'],
    'Król strzelców': ['Ronaldo (8 goli)', 'Klose (5 goli)', 'Forlan (5 goli)'],
    'Cena biletu': ['100 USD', '120 USD', '150 USD'],
}

# Tworzenie tabeli
df = pd.DataFrame(data)

# Wyświetlanie tabeli
print(df)