from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Ścieżka do bazy danych SQLite
database_url = 'sqlite:///example.db'

# Tworzenie silnika bazy danych
engine = create_engine(database_url)

# Tworzenie sesji
Session = sessionmaker(bind=engine)
session = Session()

# Teraz możesz używać `session` do wykonywania zapytań na bazie danych

# Pamiętaj, aby zamknąć sesję po zakończeniu
session.close()
