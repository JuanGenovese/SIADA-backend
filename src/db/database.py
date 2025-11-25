from datetime import date, datetime, time
from sqlalchemy import create_engine
from sqlalchemy import create_engine, Column, DateTime, func, text
from sqlalchemy.orm import sessionmaker, Session
import math
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv 

load_dotenv()

DB_CONNECTION = os.getenv("DB_CONNECTION")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")

DATABASE_URL = f"{DB_CONNECTION}://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"

engine = create_engine(
    DATABASE_URL,
    connect_args={
        "options": "-c timezone=America/Argentina/Buenos_Aires"
    }
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class TimestampMixin:
    fecha_creacion = Column(DateTime, server_default=func.now(), index=True)
    fecha_modificacion = Column(
        DateTime, server_default=func.now(), onupdate=func.now(), index=True
)
    
def get_db():
    db = SessionLocal()
    try:
        db.execute(text("SET TIME ZONE 'America/Argentina/Buenos_Aires'"))
        yield db
    finally:
        db.close()

async def connection(
    proc_name: str,
    proc_params: dict,
    db: Session,
    keep: bool = False,
    timezone: str = "America/Argentina/Buenos_Aires"
):
    if db is None:
        raise Exception("La sesión de la base de datos no es válida")

    try:
        db.execute(text(f"SET TIME ZONE '{timezone}'"))
    except Exception as e:
        raise Exception(f"Error al configurar zona horaria: {str(e)}")

    def convert_row_to_dict(rows, column_names):
        """Convierte una fila de SQLAlchemy a un diccionario."""
        try:
            dict_rows = []

            for row in rows:
                row_dict = {}
                cantidad_paginas = None

                for index, column in enumerate(column_names):
                    value = row[index]

                    if column == "total_registros" and cantidad_paginas is None:
                        cantidad_paginas = math.ceil(
                            value / proc_params["cantidad_filas"]
                        )

                        continue

                    if isinstance(value, list):
                        value = [v for v in value]

                    elif isinstance(value, datetime):
                        value = value.strftime("%d/%m/%Y %H:%M:%S")

                    elif isinstance(value, date):
                        value = value.strftime("%d/%m/%Y")

                    elif isinstance(value, time):
                        value = value.strftime("%H:%M:%S")

                    row_dict[column] = value

                dict_rows.append(row_dict)

            return dict_rows, cantidad_paginas

        except Exception as e:
            raise Exception(f"Error al convertir la fila: {str(e)}")

    try:
        if proc_params:
            if proc_params.get("pagina"):
                proc_params["cantidad_skip"] = (
                    proc_params["pagina"] - 1
                ) * proc_params["cantidad_filas"]

                del proc_params["pagina"]

            query = f"SELECT * FROM {proc_name}(:{', :'.join(proc_params.keys())})"
            result = db.execute(text(query), proc_params)

        else:
            query = f"SELECT * FROM {proc_name}()"

            result = db.execute(text(query))

        if not keep:
            db.commit()

        rows = result.fetchall()
        column_names = result.keys()

        if len(rows) > 0:
            dict_rows, cantidad_paginas = convert_row_to_dict(rows, column_names)

            return {
                "rows": dict_rows,
                "pages": cantidad_paginas,
            }

        else:
            return {"rows": [], "pages": None}

    except Exception as e:
        db.rollback()
        print("Error en la obtención:", e)
        raise e

    finally:
        if not keep:
            db.close()