# import sqlalchemy as db

# # Bağlantı dizesini oluşturun
# conn_str = (
#     "mssql+pyodbc://DESKTOP-SVNS2I9/Aygaz_Staj"
#     "?driver=SQL+Server+Native+Client+11.0"
#     "&Trusted_Connection=yes"
# )

# try:
#     # Veritabanına bağlanın
#     engine = db.create_engine(conn_str)
#     connection = engine.connect()
#     print("Bağlantı başarılı")
# except db.exc.SQLAlchemyError as ex:
#     print("Bağlantı başarısız: " + str(ex))
#||||||||||||||||||||||||||||||||||||||||||||||
# main.py

from repository_baglan import connect_to_github

repo = connect_to_github()

# GitHub bağlantısını kullanarak işlemler yapabilirsiniz
# ...

import os
import sqlalchemy as sa
import dotenv
dotenv.load_dotenv()

SQL_SERVER = os.getenv("SQL_SERVER")
DB_NAME = os.getenv("DB_NAME")

def baglanti_sql_v2():
    conn_str = (
        f"mssql+pyodbc://{SQL_SERVER}/{DB_NAME}"
        "?driver=SQL+Server+Native+Client+11.0"
        "&Trusted_Connection=yes"
    )

    try:
        engine = sa.create_engine(conn_str)
        connection = engine.connect()
        print("Bağlantı başarılı")
    except sa.exc.SQLAlchemyError as ex:
        print("Bağlantı başarısız: " + str(ex))

    return engine

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||<
# def baglanti_sql():
#     driver = '{SQL Server Native Client 11.0}'
#     server_name = 'DESKTOP-SVNS2I9'
#     database_name = 'Aygaz_Staj'
#     trusted_connection = 'yes'

#     params = f"DRIVER={driver};SERVER={server_name};DATABASE={database_name};Trusted_Connection={trusted_connection};"
#     return params
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||<


