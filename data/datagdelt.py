import pandas as pd
import requests, zipfile, io
from datetime import datetime
from utils.constants import start_date  

def download_gdelt_day(date):
    """
    Télécharge un fichier GDELT quotidien et retourne un DataFrame filtré
    pour les keywords macro US.
    """
    url = f"http://data.gdeltproject.org/gdeltv2/{date.strftime('%Y%m%d')}.export.CSV.zip"
    r = requests.get(url)
    if r.status_code != 200:
        print(f"Pas de fichier pour {date}")
        return None

    # Lire le zip directement en mémoire
    z = zipfile.ZipFile(io.BytesIO(r.content))
    file_name = z.namelist()[0]
    df = pd.read_csv(z.open(file_name), sep="\t", header=None, low_memory=False)

    # Filtrer par mots-clés
    keywords = ["Fed", "inflation", "unemployment", "interest rate", "bond"]
    df_filtered = df[df[7].str.contains("|".join(keywords), case=False, na=False)]

    # Optionnel : filtrer USA
    df_filtered = df_filtered[df_filtered[0].str.contains("USA", na=False)]

    # Ajouter une colonne date
    df_filtered['date'] = date
    return df_filtered

# Exemple
date=datetime.strptime(start_date, '%Y-%m-%d')
df_day = download_gdelt_day(date)
print(df_day.shape)
print(df_day.head())