# Program znajdujący najmniejszy koszt przejazdu

Rozwiązanie zostało napisane przy pomocy języka **Python 3.9** i biblioteki **numpy**.

Program do znajdowania najbardziej ekonomicznej drogi przejazdu wykorzystuje algorytm **Djikstry**, który wykorzystuje macierz kosztu krawędzi powstałą poprzez przemnożenie poprzez pomnożenie kosztu przejazdu po danym kolorze nawierzchni i jej długości.

Do uruchomienia programu wymagane jest podanie
listy ponumerowanych wierzchołków od 1 do n oraz
listy krawędzi w postaci [V1, V2, color, distance], gdzie V1 i V2 to wierzchołki grafu, color to wartość enumeratywna odpowiadająca kolorowi odcinka, a distance to długość odcinka.

 Ponadto program
przyjmuje na wejściu indeksy wierzchołka początkowego i końcowego. Pomiędzy którymi ma być znaleziona droga o najmniejszym koszcie.
 
Program na wyjściu prezentuje minimalny koszt oraz składającą się z poszczególnych wierzchołków, optymalną drogę przejazdu.
