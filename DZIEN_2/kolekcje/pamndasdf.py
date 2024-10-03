import pandas as pd

# Tworzenie DataFrame
data = {
    'Imię': ['Jan', 'Anna', 'Piotr', 'Kasia'],
    'Wiek': [28, 24, 35, 30],
    'Miasto': ['Warszawa', 'Kraków', 'Wrocław', 'Poznań']
}

df = pd.DataFrame(data)

# Wyświetlanie DataFrame
print(df)

# Przykład manipulacji: filtrowanie według wieku
filtered_df = df[df['Wiek'] > 30]
print(filtered_df)

# Obliczanie średniego wieku
mean_age = df['Wiek'].mean()
print(f'Średni wiek: {mean_age}')
