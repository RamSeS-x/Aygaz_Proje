

from repository_baglan import connect_to_github

repo = connect_to_github()
from commit import git_push 
import os
import json
import pandas as pd
import sqlalchemy as sa
import dotenv
from baglanti_sql_v2 import baglanti_sql_v2
# .env dosyasındaki bilgileri yükle
dotenv.load_dotenv()

# Veritabanı tablo ismini alma
table_name = os.getenv("my_table")

# Veritabanı bağlantısı
engine = baglanti_sql_v2()

# JSON dosyasının adını ve yolu belirleme
file_name = "veri_4.json"
json_path = os.path.join(os.getcwd(), file_name)

# JSON dosyasını yükleme
with open(json_path, "r", encoding="utf-8-sig") as f:
    data = json.load(f)

# Pandas DataFrame oluşturma
df = pd.DataFrame(data)

# Veritabanında tablo yoksa, yeni tablo oluşturma ve verileri yükleme
if table_name not in pd.read_sql("SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE'", engine)["TABLE_NAME"].tolist():
    df.to_sql(name=table_name, con=engine, if_exists="fail", index=False)
    print(f"{table_name} tablosu başarıyla oluşturuldu ve veriler yüklendi.")
else:
    # Veritabanındaki tablonun mevcut verileri ile yeni verileri karşılaştırma
    existing_df = pd.read_sql(f"SELECT * FROM {table_name}", engine)
    if not existing_df.equals(df):
        # Verilerde değişiklik varsa, tabloyu güncelleme
        df.to_sql(name=table_name, con=engine, if_exists="replace", index=False)
        print(f"{table_name} tablosu başarıyla güncellendi.")
    else:
        # Veriler aynı ise işlemi sonlandırma
        print(f"{table_name} tablosu zaten güncel. İşlem sonlandırıldı.")

# Veritabanı bağlantısını kapatma
engine.dispose()
