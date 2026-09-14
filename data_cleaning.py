import pandas as pd
import numpy as np
import os

#i only select the columns i deem interesting for the analysis i want to make
columns = [
    "id",
    "title",
    "release_date",
    "genres",
    "budget",
    "revenue",
    "runtime",
    "original_language",
    "vote_average",
    "vote_count"
]

movies = pd.read_csv("data/raw/movies_metadata.csv", usecols=columns)

movies["budget"] = pd.to_numeric(movies["budget"], errors="coerce")
movies["revenue"] = pd.to_numeric(movies["revenue"], errors="coerce")
movies["runtime"] = pd.to_numeric(movies["runtime"], errors="coerce")
movies["vote_average"] = pd.to_numeric(movies["vote_average"], errors="coerce")
movies["vote_count"] = pd.to_numeric(movies["vote_count"], errors="coerce")
movies["release_date"] = pd.to_datetime(movies["release_date"], errors="coerce")

print(movies.dtypes)
#stampe per controllare hce sia tutto a posto
print(movies.head())
print(movies.columns)
print(movies.shape)

print(movies.info())
print(movies.isna().sum())
print(movies.dtypes)

#controllo se ci sono duplicati
print("========================================")
print("controllo se ci sono duplicati: ")
print("duplicati:", movies.duplicated().sum())
print("id duplicati:", movies["id"].duplicated().sum())

#rimuovere righe duplicate
print("========================================")
print("rimuovo righe duplicate: ")
movies = movies.drop_duplicates()
print("Righe dopo la rimozione:", movies.shape)

#gestire gli id duplicati
print("========================================")
print("gestisco id duplicati: ")
duplicated_ids = movies[movies["id"].duplicated(keep=False)]
print(duplicated_ids.sort_values("id").to_string())
#viene fuori che semplicemente ci sono due film che sono duplicati perchè hanno 2 conti diversi di vote count, tengo quelli con vote count più alto
print("========================================")
print("rimuovo i duplicati con vote count più basso: ")
movies = movies.sort_values("vote_count", ascending=False)
movies = movies.drop_duplicates(subset="id", keep="first")
print("Righe dopo la rimozione:", movies.shape)
print("ID duplicati:", movies["id"].duplicated().sum())

print("========================================")
print("valori null: ")
print(movies.isna().sum())
#gestire i valori null

print("========================================")
print("titolo: sono 6 righe che hanno NAN anche vote average e vote count - decido di eliminarli: ")
#titolo: sono 6 righe che hanno NAN anche vote average e vote count - decido di eliminarli
print(movies[movies["title"].isna()])
movies = movies.drop(movies[movies["title"].isna()].index)
print("Righe dopo la rimozione:", movies.shape)
print(movies[movies["title"].isna()])

print("========================================")
print("altri nan: ")
print(movies[movies["release_date"].isna()])
print(movies[movies["revenue"].isna()])
print(movies[movies["runtime"].isna()])
print(movies[movies["original_language"].isna()])
#commento queste due ultime stampe perchè abbiamo già eliminato le righe con vote avg e count NAN prima (title)
#print(movies[movies["vote_average"].isna()])
#print(movies[movies["vote_count"].isna()])

print("========================================")
print("prima di decidere come gestire gli altri valori null voglio controllare se ci sono righe con + di un val null: ")
#prima di decidere come gestire gli altri valori null voglio controllare se ci sono righe con + di un val null
missing = movies.isna().sum(axis=1)
print(missing.value_counts().sort_index())

missing = movies.isna().sum(axis=1)

print("========================================")
print("noto che nei film con due NAN, budget è a 0, revenue è a 0... possiamo eliminarli: ")
print(movies[missing == 2].to_string())
#noto che nei film con due NAN, budget è a 0, revenue è a 0... possiamo eliminarli
movies = movies[missing < 2]

print("========================================")
print("controllo quanti film hanno 0 a budget, revenue, runtime o release date: ")
#controllo quanti film hanno 0 a budget, revenue, runtime o release date
print("Budget = 0:", (movies["budget"] == 0).sum())
print("Revenue = 0:", (movies["revenue"] == 0).sum())
print("Release date mancante:", movies["release_date"].isna().sum())
print("Runtime = 0:", (movies["runtime"] == 0).sum())
print("Vote Average = 0:", movies["vote_average"].isna().sum())
print("Vote Count = 0:", (movies["vote_count"] == 0).sum())

print("========================================")
print("controllo quanti film 1, 2, 3, 4, 5, 6 zeri: ")
zero_count = (
    (movies["budget"] == 0).astype(int)
    + (movies["revenue"] == 0).astype(int)
    + (movies["runtime"] == 0).astype(int)
    + movies["release_date"].isna().astype(int)
    + (movies["vote_average"] == 0).astype(int)
    + (movies["vote_count"] == 0).astype(int)
)

print(zero_count.value_counts().sort_index())

zero_columns = pd.DataFrame({
    "budget": movies["budget"] == 0,
    "revenue": movies["revenue"] == 0,
    "runtime": movies["runtime"] == 0,
    "release_date": movies["release_date"].isna(),
    "vote_average": movies["vote_average"] == 0,
    "vote_count": movies["vote_count"] == 0,
})

print(zero_columns.value_counts())

print("========================================")
print("elimino film con 6 zeri: ")
movies = movies[zero_count < 6]

print("========================================")
print("controllo valori impossibili: ")
print(movies["id"].duplicated().sum())

print((movies["budget"] < 0).sum())
print((movies["revenue"] < 0).sum())
print((movies["runtime"] < 0).sum())
print((movies["vote_average"] < 0).sum())
print((movies["vote_average"] > 10).sum())
print((movies["vote_count"] < 0).sum())

print("========================================")
print("date min e max: ")
print(movies["release_date"].min())
print(movies["release_date"].max())

print("========================================")
print("budget min e max: ")
print(movies["budget"].min())
print(movies["budget"].max())

print("========================================")
print("revenue min e max: ")
print(movies["revenue"].min())
print(movies["revenue"].max())

print("========================================")
print("runtime min e max: ")
print(movies["runtime"].min())
print(movies["runtime"].max())

print("========================================")
print("vote_average min e max: ")
print(movies["vote_average"].min())
print(movies["vote_average"].max())

print("========================================")
print("vote_count min e max: ")
print(movies["vote_count"].min())
print(movies["vote_count"].max())

print("========================================")
print("dato che rappresentano dati mancanti trasformo gli 0 di budget, revenue, runtime in null: ")
movies["budget"] = movies["budget"].replace(0, np.nan)
movies["revenue"] = movies["revenue"].replace(0, np.nan)
movies["runtime"] = movies["runtime"].replace(0, np.nan)

print(movies.info())
print(movies.isna().sum())
print(movies.dtypes)

columns = [
    "id",
    "title",
    "release_date",
    "genres",
    "budget",
    "revenue",
    "runtime",
    "original_language",
    "vote_average",
    "vote_count"
]

movies = movies[columns]
os.makedirs("data/processed", exist_ok=True)
movies.to_csv("data/processed/movies_clean.csv", index=False)

