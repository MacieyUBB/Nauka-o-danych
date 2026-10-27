# Autor: Maciej Grochowski, nr albumu 66190

# Zadanie 1
from pathlib import Path

import kagglehub
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# Zadanie 2
ramka_ze_slownika = pd.DataFrame(
    {
        "osoba": ["Ala", "Bartek", "Celina"],
        "punkty": [12, 15, 18],
    }
)
print(ramka_ze_slownika)


# Zadanie 3
ramka_z_listy = pd.DataFrame(
    [["Ala", 12], ["Bartek", 15], ["Celina", 18]],
    columns=["osoba", "punkty"],
)
print(ramka_z_listy)


# Zadanie 4
sciezka = Path(kagglehub.dataset_download("yasserh/titanic-dataset"))
pliki_csv = sorted(sciezka.glob("*.csv"))
if not pliki_csv:
    raise FileNotFoundError(f"Nie znaleziono pliku CSV w katalogu {sciezka}")
plik_csv = pliki_csv[0]
df = pd.read_csv(plik_csv)
pliki_xlsx = sorted(sciezka.glob("*.xlsx")) + sorted(sciezka.glob("*.xls"))
if pliki_xlsx:
    df_xlsx = pd.read_excel(pliki_xlsx[0])
    print(df_xlsx.head())
else:
    print("Zbiór zawiera plik CSV; pliku XLSX nie ma w pobranym zbiorze.")
print(df.head())


# Zadanie 5
print(df.transpose())


# Zadanie 6
print(df.head(10))


# Zadanie 7
print(df.tail(10))


# Zadanie 8
df.info()


# Zadanie 9
liczba_wierszy, liczba_kolumn = df.shape
print(f"Wiersze: {liczba_wierszy}, kolumny: {liczba_kolumn}")


# Zadanie 10
kolumny_liczbowe = df.select_dtypes(include=np.number).columns.tolist()
statystyka_liczbowa = df[kolumny_liczbowe].describe()
print(statystyka_liczbowa)


# Zadanie 11
kolumny_kategoryczne = df.select_dtypes(exclude=np.number).columns.tolist()
statystyka_kategoryczna = df[kolumny_kategoryczne].describe()
print(statystyka_kategoryczna)
for kolumna in kolumny_kategoryczne:
    najpopularniejsza = df[kolumna].mode(dropna=True).iloc[0]
    czestosc = df[kolumna].value_counts(dropna=True).iloc[0]
    print(
        kolumna,
        "unikalne:",
        df[kolumna].nunique(dropna=True),
        "najpopularniejsza:",
        najpopularniejsza,
        "częstość:",
        czestosc,
    )


# Zadanie 12
df = df.dropna().reset_index(drop=True)
print(f"Rozmiar po usunięciu braków: {df.shape}")


# Zadanie 13
print(df.loc[0:2, ["Name", "Age", "Fare"]])
print(df.iloc[0:3, 0:4])
print(df[["Name", "Sex"]].iloc[[0, 2, 4]])
print(df.loc[df.index[:3], "Name":"Fare"])


# Zadanie 14
wiersze_z_drogim_biletem = df.loc[df["Fare"] > df["Fare"].median()]
print(wiersze_z_drogim_biletem)


# Zadanie 15
wiersze_kobiet_z_klasy_pierwszej = df.loc[
    (df["Sex"] == "female") & (df["Pclass"] == 1)
]
print(wiersze_kobiet_z_klasy_pierwszej)


# Zadanie 16
wiersze_z_woman = df.loc[df["Name"].str.contains("Mrs|Miss", case=False, na=False)]
print(wiersze_z_woman)


# Zadanie 17
wiersze_bez_woman = df.loc[~df["Name"].str.contains("Mrs|Miss", case=False, na=False)]
print(wiersze_bez_woman)


# Zadanie 18
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
print(df[["SibSp", "Parch", "FamilySize"]].head())


# Zadanie 19
df_bez_kabiny = df.drop(columns=["Cabin"])
print(df_bez_kabiny.head())


# Zadanie 20
df = df.rename(columns={"Fare": "TicketFare"})
print(df.head())


# Zadanie 21
plik_wynikowy = Path.cwd() / "titanic_po_analizie.csv"
df.to_csv(plik_wynikowy, index=False)
print(f"Zapisano plik: {plik_wynikowy}")


# Zadanie 22
srednia_cena = df["TicketFare"].mean()
maksymalna_cena = df["TicketFare"].max()
minimalna_cena = df["TicketFare"].min()
print(
    f"Cena biletu: średnia={srednia_cena:.2f}, "
    f"maksymalna={maksymalna_cena:.2f}, minimalna={minimalna_cena:.2f}"
)
print(
    f"Interpretacja ceny biletu: mediana wynosi {df['TicketFare'].median():.2f}, "
    f"czyli mniej niż średnia {srednia_cena:.2f}; drogie bilety odstające "
    "podwyższają średnią."
)


# Zadanie 23
print(f"Liczba wierszy: {len(df)}")


# Zadanie 24
print(df["Embarked"].unique())


# Zadanie 25
print(df["Pclass"].value_counts().sort_index())


# Zadanie 26
print(df.sort_values("TicketFare").head())
print(df.sort_values("TicketFare", ascending=False).head())


# Zadanie 27
print(df.nlargest(10, "TicketFare"))
print(df.nsmallest(10, "TicketFare"))


# Zadanie 28
print(df.loc[df["Sex"] == "female"].nlargest(10, "TicketFare"))


# Zadanie 29
kolumny_numeryczne_po_zmianie = df.select_dtypes(include=np.number).columns
grupowanie_zlozone = df.groupby(["Sex", "Pclass"], observed=True)[
    kolumny_numeryczne_po_zmianie
].mean()
print(grupowanie_zlozone)


# Zadanie 30
grupowanie = df.groupby("Sex", observed=True).agg(
    srednia_wieku=("Age", "mean"),
    srednia_ceny=("TicketFare", "mean"),
    liczba_rekordow=("PassengerId", "count"),
    mediana_ceny=("TicketFare", "median"),
)
print(grupowanie)


# Zadanie 31
print(grupowanie_zlozone.index.names)


# Zadanie 32
print(grupowanie_zlozone.sort_index(level=["Pclass", "Sex"]))


# Zadanie 33
tabela_przestawna = pd.pivot_table(
    df,
    values="TicketFare",
    index="Sex",
    columns="Pclass",
    aggfunc="mean",
)
print(tabela_przestawna)


# Zadanie 34
print("Indeksy:", tabela_przestawna.index)
print("Kolumny:", tabela_przestawna.columns)


# Zadanie 35
tabela_przestawna_zlozona = pd.pivot_table(
    df,
    values="TicketFare",
    index=["Sex", "Embarked"],
    columns="Pclass",
    aggfunc="mean",
)
print(tabela_przestawna_zlozona)
print(tabela_przestawna_zlozona.index)


# Zadanie 36
from matplotlib import pyplot


# Zadanie 37
if "get_ipython" in globals():
    get_ipython().run_line_magic("matplotlib", "inline")


# Zadanie 38
tabela_przestawna.plot(kind="bar", figsize=(8, 5))
plt.title("Średnia cena biletu według płci i klasy")
plt.xlabel("Płeć")
plt.ylabel("Średnia cena biletu")
plt.tight_layout()
plt.show()
print(
    "Interpretacja wykresu: średnia cena biletu różni się między klasami "
    "i płciami; bilety pierwszej klasy są przeciętnie droższe."
)


# Zadanie 39
df["Age"].plot(kind="hist", bins=15, figsize=(8, 5))
plt.title("Rozkład wieku pasażerów")
plt.xlabel("Wiek")
plt.ylabel("Liczba pasażerów")
plt.tight_layout()
plt.show()
print(
    "Interpretacja histogramu: najwięcej pasażerów to osoby dorosłe, "
    "ale w zbiorze występują również dzieci i osoby starsze."
)


# Zadanie 40
mapowanie_klas = pd.DataFrame(
    {
        "Pclass": [1, 2, 3],
        "ClassName": ["Pierwsza", "Druga", "Trzecia"],
    }
)
polaczenie_merge = df.merge(mapowanie_klas, on="Pclass", how="left")
polaczenie_concat = pd.concat([df.head(3), df.tail(3)], ignore_index=True)
print(polaczenie_merge.head())
print(polaczenie_concat)


# Zadanie 41
df["FarePerPersonInFamily"] = df["TicketFare"] / df["FamilySize"]
df["AgeSquared"] = df["Age"] ** 2
print(df[["TicketFare", "FamilySize", "FarePerPersonInFamily", "AgeSquared"]].head())


# Zadanie 42
df["AgeGroup"] = df["Age"].apply(
    lambda wiek: "dziecko" if wiek < 18 else "dorosły"
)
df["FareLevel"] = df["TicketFare"].apply(
    lambda cena: "wysoka" if cena >= df["TicketFare"].median() else "niska"
)
print(df[["Age", "AgeGroup", "TicketFare", "FareLevel"]].head())


# Zadanie 43
liczba_wierszy_z_chunksize = 0
sumy_w_chunks = []
for fragment in pd.read_csv(plik_csv, chunksize=100):
    liczba_wierszy_z_chunksize += len(fragment)
    sumy_w_chunks.append(fragment["Fare"].sum())
print("Liczba wierszy odczytanych fragmentami:", liczba_wierszy_z_chunksize)
print("Suma cen biletów odczytanych fragmentami:", sum(sumy_w_chunks))


# Zadanie 44
wartosci_wieku = df["Age"]
srednia_pandas = wartosci_wieku.mean()
srednia_numpy = np.mean(wartosci_wieku)
print("Średnia wieku pandas:", srednia_pandas)
print("Średnia wieku numpy:", srednia_numpy)
print(f"Typowy pasażer miał około {srednia_pandas:.2f} lat.")


# Zadanie 45
mediana_pandas = wartosci_wieku.median()
mediana_numpy = np.median(wartosci_wieku)
print("Mediana wieku pandas:", mediana_pandas)
print("Mediana wieku numpy:", mediana_numpy)
print(
    f"Mediana wynosi {mediana_pandas:.2f} lat, a średnia {srednia_pandas:.2f}; "
    "niewielka różnica oznacza, że nietypowe wieku nie przesuwają silnie średniej."
)


# Zadanie 46
odchylenie_pandas = wartosci_wieku.std()
odchylenie_numpy = np.std(wartosci_wieku, ddof=1)
print("Odchylenie standardowe pandas:", odchylenie_pandas)
print("Odchylenie standardowe numpy:", odchylenie_numpy)
print(
    f"Typowa odległość wieku od średniej wynosi około {odchylenie_pandas:.2f} lat."
)


# Zadanie 47
wariancja_pandas = wartosci_wieku.var()
wariancja_numpy = np.var(wartosci_wieku, ddof=1)
print("Wariancja pandas:", wariancja_pandas)
print("Wariancja numpy:", wariancja_numpy)
print(
    "Kwadrat odchylenia standardowego:",
    odchylenie_pandas**2,
    "Różnica:",
    abs(wariancja_pandas - odchylenie_pandas**2),
)


# Zadanie 48
kolumna_a = df["Age"]
kolumna_b = df["TicketFare"]
korelacja_pandas = kolumna_a.corr(kolumna_b)
korelacja_numpy = np.corrcoef(kolumna_a, kolumna_b)[0, 1]
print("Korelacja pandas:", korelacja_pandas)
print("Korelacja numpy:", korelacja_numpy)
kierunek = "dodatni" if korelacja_pandas > 0 else "ujemny"
print(f"Zależność ma kierunek {kierunek} i siłę około {abs(korelacja_pandas):.2f}.")


# Zadanie 49
kowariancja_pandas = kolumna_a.cov(kolumna_b)
kowariancja_numpy = np.cov(kolumna_a, kolumna_b, ddof=1)[0, 1]
print("Kowariancja pandas:", kowariancja_pandas)
print("Kowariancja numpy:", kowariancja_numpy)
print(
    "Kowariancja zachowuje jednostki obu zmiennych i pokazuje wspólny kierunek "
    "zmienności, natomiast korelacja jest znormalizowana do przedziału [-1, 1]."
)
print(
    f"Interpretacja korelacji i kowariancji: korelacja wynosi "
    f"{korelacja_pandas:.3f}, więc zależność wieku i ceny biletu jest bardzo "
    f"słaba i ma kierunek {kierunek}; wiek prawie nie wyjaśnia ceny biletu."
)


# Zadanie 50
podsumowanie = pd.DataFrame(
    {
        "średnia": [kolumna_a.mean(), kolumna_b.mean()],
        "mediana": [kolumna_a.median(), kolumna_b.median()],
        "odchylenie_standardowe": [kolumna_a.std(), kolumna_b.std()],
    },
    index=["Age", "TicketFare"],
)
print(podsumowanie)
print(
    f"Wiek ma średnią {kolumna_a.mean():.2f}, medianę {kolumna_a.median():.2f} "
    f"i odchylenie {kolumna_a.std():.2f}; cena biletu ma średnią "
    f"{kolumna_b.mean():.2f}, medianę {kolumna_b.median():.2f} i odchylenie "
    f"{kolumna_b.std():.2f}."
)
print(
    f"Korelacja wieku z ceną biletu wynosi {korelacja_pandas:.3f}, a kowariancja "
    f"{kowariancja_pandas:.3f}. Zależność ma kierunek {kierunek}; wartości są "
    "rozproszone w stopniu opisanym przez odchylenia standardowe."
)
