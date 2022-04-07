# `Poročilo: Računalništvo 2 - Vaje 17. 3. 2022 Floyd Warshall`

**Ime:** Tit Arnšek

**Datum:** 17. 3. 2022


## Vsebina 
* Na tablo smo ponovili Floyd Warshall-ov algoritem
* Naredili smo primer najkraših poti met dvsemi vozlišči s pomočjo zgoraj omenjenega vozlišča


### 1) `Ponovitev Primovega algoritma (vhod, izhod, ideja algoritma, časovna zahtevnost)`
* Računa minimalna vpeta drevesa
* 
* $O(v^2)$....naivna metoda
* S prioritetno vrsto, kjer bi shranjevali povezave, je ČZ $O(|E|*log|E|)$
```python

```

Minimalnih vpetih je lahko več, algoritem vrne eno izmed njih

Lahko so negativne uteži, celo negativni cikli

### 2) `Simulacija Primovega algoritma na grafu:`


### 3) `Pokaži, da je MVD enolično, če so vse uteži. v grafu različne. Namig: protislovje`

Imamo podan graf $G$, vse uteži RAZLIČNE.
Recimo, da imamo dva drevesa $T_1$ in $T_2$, ki sta MVD; $T_1$ ni $T_2$.To pomeni, da vsaj ena povezava različna.
Torej obstajata $e_1$ $\in$ $T_1$, $e_1$ $\notin$ $T_2$ in $e_2$ $\in$ $T_2$, $e_2$ $\notin$ $T_1$. Predpostavimo $e_1  \le e_2$(Z najmanjšo utežjo) 

$e_2$ dodamo v $T_1$.  Dobimo cikel. Na ciklu najdemo $v \in T1/T2$.
Naredimo novo drevo $T'$: $T'$ = $T_1$ + $e_2$ - $v$.  
$\Rightarrow$ $w(T')$ = $w(T_1)$ + $w(e_2)$ - $w(v)$
$w(e_2)$ - $w(v)$ $\le$ 0
$w(T_2)$ $\le$ $w(T')$ $\Rightarrow$ $w(T_2)$ = $w(T')$ $\Rightarrow$ 0 = $w(e_2)$ - $w(v)$
$\Rightarrow$ $w(e_2)$ = $w(v)$... protislovje
$\Rightarrow$


### 4) `Kako bi poiskal najdražje vpeto drevo?`
Algoritem bi bil zelo podoben Primovemu, samo da bi vedno izbrali najdražjo povezavo, ki je na voljo.


### 5) `Naj bo T MVD in T' drevo najkrajših razdalj od vozlišča s do vseh ostalih. Vsaki uteži sedaj prištejemo 1. Ali se T in T' spremenita?`
$T$ se ne spremeni.
* V algoritmu na vsakem koraku izberemo enake povezave
* Vsem vpetim drevesom se cena poveča za $n-1$ $\Rightarrow$ $T$ je še vedno MVD

$T'$ se spremeni.
* Daljše poti 'kaznujemo' bolj kot krajše poti


### 6) `Recimo, da imamo utežen graf G in njegovo MVD T (eno izmed možnih). Sedaj določeni povezavi e spremenimo utež. Opiši čim bolj učinkovit algoritem, ki popravi T.`

$T = MVD$

$e \in G$

Imamo več možnosti:
* $+$, $e \notin T$. $T$ se ne premeni
* $-$, $e \in T$. $T$ se ne premeni 

* $+$, $e \in T$
        
    $e$ odstranimo, $T$ razpoade na  $T_1$ in $T_2$. Poiščemo najkrajšo povezavo med $T_1$ in $T_2$. Dobimo $T$. (Naredimo en korak)

* $-$, $e \notin T$

    $e$ dodamo v $T$, pri tem nastane cikel $C$. Iz cikla $C$ odstranimo najdražjo povezavo.
### 7) `* Kako bi poiskal "drugo" najcenejše vpeto drevo? Tretje? Kako bi poiskal vsa MVD v grafu?`
$F$ = množica vseh vpetih dreves v grafu G. ($G = K_n$ $\Rightarrow$ $|F| = n^{n-2}$)

Zgradimo graf $T(G):$
* vozlišča so drevesa v $F$($V(T(G)) = F$)
* $T$, $T' \in F(G)$ sta soseda če $|T \cap T'| = k-1$

Recimo, da vzamemo $T \in F(G)$. $d(T) = O(k * n^2)$