from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Configura la URL de la base de datos (puedes cambiar esto según tu configuración)
DATABASE_URL = "sqlite:///database.db"  # Ejemplo para SQLite

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL)

# Crear una sesión local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Función para obtener una sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()