NAUKA O DANYCH I — ZADANIA

Autor: Maciej Grochowski
Numer albumu: 66190

STRUKTURA PROJEKTU

Zad_1/
|-- zadania.py
|-- README.md
|-- README.txt
|-- titanic_po_analizie.csv
|-- zrzuty/
|   |-- 01_pierwsze_10_wierszy.jpg
|   |-- 02_informacje_o_ramce.jpg
|   |-- 03_wykres_tabeli_przestawnej.jpg
|   |-- 04_histogram_wieku.jpg
|   `-- 05_statystyki_koncowe.jpg
`-- .git/

Folder .git jest lokalna czescia repozytorium i zawiera historie commitow.
Nie jest wyswietlany na stronie GitHub jako zwykly folder.

OPIS

Plik zadania.py zawiera realizację zadań 1–49 z części A i B oraz zadania
podsumowującego. Wszystkie zadania wykonują się w jednym pliku Python,
a kolejne fragmenty są oznaczone komentarzami z numerami zadań.

Analiza korzysta ze zbioru Titanic Dataset pobieranego automatycznie przez
Kaggle Hub:
https://www.kaggle.com/datasets/yasserh/titanic-dataset

Zbiór zawiera między innymi kolumny kategoryczne (Sex, Embarked) oraz
liczbowe (Age, Fare, Pclass), dzięki czemu można wykonać wszystkie wymagane
operacje.

WYMAGANIA

Potrzebne są:
- Python 3,
- połączenie z internetem przy pierwszym uruchomieniu,
- biblioteki kagglehub, pandas, numpy, matplotlib oraz openpyxl.

Instalacja bibliotek:
python -m pip install kagglehub pandas numpy matplotlib openpyxl

URUCHOMIENIE

W katalogu projektu wykonaj:
python .\zadania.py

Przy pierwszym uruchomieniu Kaggle Hub pobierze zbiór danych i zapisze go
w lokalnym katalogu pamięci podręcznej. Skrypt wyświetla wyniki kolejnych
operacji, informacje o ramce danych, statystyki, tabele oraz dwa wykresy.

Przy uruchamianiu skryptu nalezy zamknac okna wykresow, aby program mogl
przejsc do kolejnych zadan i wyswietlic koncowe statystyki.

ZAKRES ZADAŃ

1–5: import pandas, tworzenie ramek, wczytanie danych i transpozycja.
6–11: podgląd ramki i statystyki opisowe.
12–21: czyszczenie, wybór danych, zmiany kolumn i zapis CSV.
22–28: agregacje, sortowanie i wybieranie rekordów.
29–35: grupowanie, indeks złożony i tabele przestawne.
36–39: matplotlib i wykresy.
40–43: łączenie ramek, kolumny obliczane i chunksize.
44–49: średnia, mediana, odchylenie standardowe, wariancja, korelacja
i kowariancja.
50: podsumowanie statystyczne dla wieku i ceny biletu.

PLIKI GENEROWANE PODCZAS URUCHOMIENIA

Skrypt zapisuje w katalogu projektu plik:
titanic_po_analizie.csv

Jest to kopia oczyszczonej ramki danych z dodatkowymi kolumnami obliczonymi
w trakcie analizy.

ZRZUTY EKRANU

Folder zrzuty zawiera dowody wykonania analizy:
- 01_pierwsze_10_wierszy.jpg — wynik df.head(10),
- 02_informacje_o_ramce.jpg — wynik df.info(),
- 03_wykres_tabeli_przestawnej.jpg — srednia cena biletu wedlug plci
  i klasy,
- 04_histogram_wieku.jpg — rozklad wieku pasazerow,
- 05_statystyki_koncowe.jpg — wyniki miar statystycznych i podsumowanie.

REPOZYTORIUM PROJEKTU

Pelny projekt, wszystkie pliki, zrzuty ekranu oraz historia commitow sa
dostepne w repozytorium GitHub Macieja Grochowskiego o nicku MacieyUBB:
https://github.com/MacieyUBB/Nauka-o-danych

Historia zawiera osobne commity dotyczace kodu, dokumentacji, danych
wynikowych, zrzutow ekranu i poprawek interpretacji wynikow.
