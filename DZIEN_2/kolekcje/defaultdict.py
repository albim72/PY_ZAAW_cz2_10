from collections import defaultdict

# Tworzenie defaultdict z domyślną wartością jako lista
word_count = defaultdict(int)

# Przykładowy tekst
text = "python jest super python jest fajny python jest łatwy"

# Zliczanie wystąpień słów
for word in text.split():
    word_count[word] += 1

# Wyświetlanie wyników
for word, count in word_count.items():
    print(f'{word}: {count}')
