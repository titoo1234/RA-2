
# <span style="color:red">Poročilo: Računalništvo 2 - Vaje 21.4.2022 Zgoščevalne funkcije</span>

**Ime:** Tit Arnšek

**Datum:** 21. 4. 2022

---


## Vsebina 
 * Zgoščevalne funkcije

---
### Uvod
Množica $U$

Množica $V: |V| = m, u>>m$

$S$...množica ključev $|S| = n$.

$h: U \rightarrow V$

---


### 1) `V zgoščevalno tabelo velikosti 11 (n = 11) vstavimo ključe iz seznama [23, 1, 13, 11, 24, 33, 18, 42, 31] z zgoščevalno funkcijo h(x) = x mod n`

`Kakšna izgleda tabela glede na različne pristope reševanja trkov. Uporabi veriženje ter linearno in kvadratično iskanje(probing). Do kakšnih problemov lahko pridemo pri teh pristopih? Kaj bi bilo, če bi uporabili kakšno drugo zgoščevalno funkcijo oblike h(x) = ax mod n za nek a različen od 0 in manjši od n? Bi lahko za poljuben a našel zaporedje ključev, ki bi ustvaril veliko trkov? Naštej še kakšne standardne zgoščevalne funkcije.`

    h(x) = x % 11
     veriženje    linearno   kvadratično
     -----------------------------------
    0| 11, 33  |     11    |   11
    1| 23,1    |     23    |   23 
    2| 13,24   |     1     |   1 
    3|         |     13    |   13
    4|         |     24    |   24
    5|         |     33    |  
    6|         |           |  
    7| 18      |     18    |   18
    8|         |           |  
    9|42,31    |     42    |   42
    10         |     31    |   31

    Za iskanje je kvadratična boljša ker je manj korakov

Če bi vzeli  $h(x) = ax \: \%  \: n$ ne bi spremenili ničesar, ker se ostanki ohranjajo

Druge zgoščevalne funkcije:
* $ h(x) = a\cdot x + b\: \% \:n $


### `2) Univerzalno zgoščevanje`
$H$ podmnozica $\{ U \rightarrow V\}$
H je univerzalna če : $\forall x \neq y $ : $P(h(x) = h(y)) \leq 1/n; \: h \in H$



### <span style="color:orange">2.1) Pokaži, da je H = {$ax  \: mod \:n : a$ $iz\: Z_n$} univerzalna družina.</span>

$h_a(x) = ax$ je bijekcija

$x \neq y \in U$

$a \in Z_n$ naključen 

$ax = ay + kn$

$a(x-y) = kn$... enakomerno porazdelljeno od 0 do $n-1$.

### <span style="color:orange">2.2) Naj bo h zgoščevalna funkcija iz univerzalne družine (izbrana naključno). Recimo, da želimo v tabelo shranit m ključev. Definiramo "load factor" alpha = m/n. Koliko je povprečno število trkov? Kaj lahko poveš o dolžini najdaljše verige? Namig: Indikatorji, linearnost pričakovane vrednosti</span>

$|V| = m$

$|S| = n$

$\alpha = n/m \leq 1  $

$h \in H$ univerzalna

$x \in U$

$L(x) = |\{y \in S|h(x) = h(y)\}|$

$E(L(x)) = 1 + \sum_{y \in S} E(I_y) \leq 1 + (n-1)\cdot 1/m \leq 1+\alpha \leq 2 $

$$ 
I_y = 
\begin{aligned}

1,h(x)=h(y) \\

0, sicer  \\

\end{aligned}
$$

$E(I_y)$ = $P(I_y = 1) = P( h(x) = h(y)) \leq 1/m$


