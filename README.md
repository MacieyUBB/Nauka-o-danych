# Nauka o danych I — zadania

Autor: **Maciej Grochowski**  
Numer albumu: **66190**

## Struktura projektu

```text
Zad_1/
├── zadania.py
├── README.md
├── README.txt
├── titanic_po_analizie.csv
├── zrzuty/
│   ├── 01_pierwsze_10_wierszy.jpg
│   ├── 02_informacje_o_ramce.jpg
│   ├── 03_wykres_tabeli_przestawnej.jpg
│   ├── 04_histogram_wieku.jpg
│   └── 05_statystyki_koncowe.jpg
└── .git/
```s

Folder `.git` jest lokalną częścią repozytorium i zawiera historię commitów.
Nie jest wyświetlany na stronie GitHub jako zwykły folder.

## Opis

Plik [zadania.py](./zadania.py) zawiera realizację zadań 1–49 z części A i B
oraz zadania podsumowującego. Wszystkie zadania wykonują się w jednym pliku
Python, a kolejne fragmenty są oznaczone komentarzami z numerami zadań.

Analiza korzysta ze zbioru **Titanic Dataset** pobieranego automatycznie przez
Kaggle Hub:

<https://www.kaggle.com/datasets/yasserh/titanic-dataset>

Zbiór zawiera między innymi kolumny kategoryczne (`Sex`, `Embarked`) oraz
liczbowe (`Age`, `Fare`, `Pclass`), dzięki czemu można wykonać wszystkie
wymagane operacje.

## Wymagania

Potrzebne są:

- Python 3,
- połączenie z internetem przy pierwszym uruchomieniu,
- biblioteki `kagglehub`, `pandas`, `numpy`, `matplotlib` oraz `openpyxl`.

Instalacja bibliotek:

```powershell
python -m pip install kagglehub pandas numpy matplotlib openpyxl
```

## Uruchomienie

W katalogu projektu wykonaj:

```powershell
python .\zadania.py
```

Przy pierwszym uruchomieniu Kaggle Hub pobierze zbiór danych i zapisze go
w lokalnym katalogu pamięci podręcznej. Skrypt wyświetla wyniki kolejnych
operacji, informacje o ramce danych, statystyki, tabele oraz dwa wykresy.

Przy uruchamianiu skryptu należy zamknąć okna wykresów, aby program mógł
przejść do kolejnych zadań i wyświetlić końcowe statystyki.

## Zakres zadań

- **1–5:** import pandas, tworzenie ramek, wczytanie danych i transpozycja,
- **6–11:** podgląd ramki i statystyki opisowe,
- **12–21:** czyszczenie, wybór danych, zmiany kolumn i zapis CSV,
- **22–28:** agregacje, sortowanie i wybieranie rekordów,
- **29–35:** grupowanie, indeks złożony i tabele przestawne,
- **36–39:** matplotlib i wykresy,
- **40–43:** łączenie ramek, kolumny obliczane i `chunksize`,
- **44–49:** średnia, mediana, odchylenie standardowe, wariancja, korelacja
  i kowariancja,
- **50:** podsumowanie statystyczne dla wieku i ceny biletu.

## Pliki generowane podczas uruchomienia

Skrypt zapisuje w katalogu projektu plik:

```text
titanic_po_analizie.csv
```

Jest to kopia oczyszczonej ramki danych z dodatkowymi kolumnami obliczonymi
w trakcie analizy.

## Zrzuty ekranu

Folder `zrzuty` zawiera dowody wykonania analizy:

- `01_pierwsze_10_wierszy.jpg` — wynik `df.head(10)`,
- `02_informacje_o_ramce.jpg` — wynik `df.info()`,
- `03_wykres_tabeli_przestawnej.jpg` — średnia cena biletu według płci
  i klasy,
- `04_histogram_wieku.jpg` — rozkład wieku pasażerów,
- `05_statystyki_koncowe.jpg` — wyniki miar statystycznych i podsumowanie.

## Repozytorium projektu

Pełny projekt, wszystkie pliki, zrzuty ekranu oraz historia commitów są
dostępne w repozytorium GitHub:

[Otwórz repozytorium Macieja Grochowskiego o nicku MacieyUBB w MacieyUBB/Nauka-o-danych na GitHubie](https://github.com/MacieyUBB/Nauka-o-danych)

Historia zawiera osobne commity dotyczące kodu, dokumentacji, danych
wynikowych, zrzutów ekranu i poprawek interpretacji wyników.
