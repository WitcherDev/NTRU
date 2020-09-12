# NTRU
Własna implementacja generatora parametrów dla kryptosystemu NTRU.
Następnie obliczam prawdopodobieństwo wystąpienia elementu odwrotnego dla losowego wielomianu generowanego w pierścieniu zależnym od N oraz q

# Założenia

## W celu przeprowadzenia doświadczenia do zadanego zadania przyjąłem następujące założenia:

* __p__ - losowa liczba pierwsza z zakresu 4 do 512
* __q__ - losowa liczba pierwsza z zakresu 4 do 512, z założeniem, że:

  ![equation](https://latex.codecogs.com/svg.latex?%5Cfrac%7BN%7D%7B2%7D%3C%20q%20%3C%20N%20-1)

* __N__ - liczba z zakresu od 2 do 400, względnie pierwsza z p

* __Pierścien NTRU:__

  ![equation](https://latex.codecogs.com/svg.latex?R_%7Bq%7D%28N%29%3D%5Cfrac%7BZ_%7Bq%7D%5Bx%5D%7D%7Bx%5E%7BN%7D-1%7D)

* __Element pierścienia__ - losowo wybrany element z wcześniej utworzonego pierścienia

* __Prawdopodobieństwo obliczane jest według wzoru:__

  ![equation](https://latex.codecogs.com/svg.latex?%281-%5Cfrac%7B1%7D%7Bq%7D%29%5Cprod_%7Bk%7D%5E%7B2%7D%281-%5Cfrac%7B1%7D%7Bq%5E%7Bk%7D%7D%29)
