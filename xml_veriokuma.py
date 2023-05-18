import os
import pandas as pd
import sqlalchemy as sa
import dotenv
from baglanti_sql_v2 import baglanti_sql_v2
import xml.etree.ElementTree as ET

dotenv.load_dotenv()

table_name = os.getenv("my_table")

from repository_baglan import connect_to_github

repo = connect_to_github()
engine = baglanti_sql_v2()
file_name = "uygulama_v2.xml"
xml_path = os.path.join(os.getcwd(), file_name)

# XML dosyasını oku
tree = ET.parse(xml_path)
root = tree.getroot()

# Verileri bir DataFrame'e dönüştür
data = []
for child in root:
    row = {}
    for subchild in child:
        row[subchild.tag] = subchild.text
    data.append(row)
df = pd.DataFrame(data)

if table_name not in pd.read_sql("SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE'", engine)['TABLE_NAME'].tolist():
    df.to_sql(name=table_name, con=engine, if_exists='fail', index=False)
    print(f"{table_name} tablosu başarıyla oluşturuldu ve veriler yüklendi.")
else:
    existing_df = pd.read_sql(f'SELECT * FROM {table_name}', engine)
    if not existing_df.equals(df):
        df.to_sql(name=table_name, con=engine, if_exists='replace', index=False)
        print(f"{table_name} tablosu başarıyla güncellendi.")
    else:
        print(f"{table_name} tablosu zaten güncel. İşlem sonlandırıldı.")

engine.dispose()
