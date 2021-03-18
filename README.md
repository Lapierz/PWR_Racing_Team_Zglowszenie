# Program znajdujący najmniejszy koszt przejazdu

Rozwiązanie zostało napisane przy pomocy języka **Python 3.9** i biblioteki **numpy**.

Program implementuje algorytm **Djikstry**, który do wyznaczenia minmalnego kosztu przejazdu wykorzystuje macierz wag krawędzi grafu powstałą poprzez pomnożenie, podanych przez użytkownika kosztów przejazdu oraz długości odcinka.

Do uruchomienia programu wymagane jest podanie
listy ponumerowanych od 1 do n wierzchołków  oraz
listy krawędzi w postaci [V1, V2, color, distance], gdzie V1 i V2 to wierzchołki grafu, color to wartość enumeratywna odpowiadająca kolorowi odcinka, a distance to długość odcinka. Ponadto program przyjmuje na wejściu indeksy wierzchołka początkowego i końcowego. Pomiędzy którymi ma być znaleziona droga o najmniejszym koszcie.
 
Program na wyjściu prezentuje minimalny koszt i drogę przejazdu.
