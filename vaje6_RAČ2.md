# `Poročilo: Računalništvo 2 - Vaje 17.3.2022 Floyd Warshall`

**Ime:** Tit Arnšek

**Datum:** 24. 3. 2022


## Vsebina 
* Dijkstrov algoritem:
    * Imamo grag $G(E,V)$, usmerjen, utežen, nenegativne uteži
    * Vhod: $G, s el V(G)$
    * Izhod: najkrajše poti od $s$ do ostalih vozlišč
    * ČZ: $O(n^2)$
 

## Komentarji in opombe


# Odgovori na vprašanja

## 1) Simuliraj Dijkstrov algoritem na spodnjem grafu.

```


```
## 2)
Predstavitev grafa:

1) $A$...matrika sosednosti,
$a_{i,j} =\, w_{i,j};(i,j)el E(G) ali O,sicer $
* Morali bi dati -1, za mesta, kjer ne obstaja povezava

2) Seznam sosednosti:
$[\cdots   [(i,w_{i,j})] \cdots ]$


```python
def DijkstraSez(G,s):
    '''G seznam sosednosti, s index vozlišča'''
    n = len(G)
    razd = [inf] * n
    obisk = [False] * n
    razd[s] = 0
    Q = set(V(G))
    while len(Q) != 0: #while Q gre tudi
        min_vozlisce = dobiMin(razd,obisk)
        doMin = razd[min_vozlisce]
        for i,w in G[min_vozlisce]:
            if doMin + w < razd[i]:
                razd[i] = doMin + w
        obisk[min_vozlisce] = True
        Q.remove(min_vozlisce)
    return razd
```
$O(|V|^2)$

----
Prednostna vrsta import heap
PQ = $[\cdots   [(p,v)] \cdots ]$
PQ.push((p,v))...O(log n)
PQ.pop()... O(log|PQ|)

```python
def DijkstraPQ(G,s):
    '''G seznam sosednosti, s index vozlišča'''
    n = len(G)
    razd = [inf] * n
    obisk = [False] * n
    razd[s] = 0
    PQ = [(0,s)]
    while len(PQ) != 0:
        doMin,min_vozlisce = PQ.pop()
        if obisk[min_vozlisce]:
            continue
        obisk[min_vozlisce] = True
        razd[min_vozlisce] = doMin
        for i,w in G[min_vozlisce]:
            if not obisk[i]:
                PQ.push((doMin+w,i))
    
    return razd
```

$O(|E| + |V|*log(||))$


## 3) Kako bi modificiral Dijkstrov algoritem, da bi poleg najcenejše vrnil še najkrajšo pot (ali kakšno drugo "sestavljeno" metriko")?
V kopici si shranjujemo (teža)

## 4) Poizkusi opustiti predpostavko o nenegativnih utežeh, tako da vsem povezavam prišteješ tako število, da postanejo nenegativne. Kje je glavni problem tega pristopa?
Ta rešitev ni v redu, saj najkrajšim potem z velikim številom vmesnih poti prišteje več, kot potem z malim številom poti.
## 5) Probaj modificirat Dijkstro, da poišče najdaljšo pot. Kje je problem? Pokaži, da je problem najdaljše poti v grafu "zelo težak" (Namig: Hamiltonova pot). Za kakšne grafe bi lahko poiskali najdaljšo pot/poti? Kakšen algoritem bi tam uporabili?

Naprimer, da imamo algoritem naj_pot(G), ki vrne seznam vozlišč na najdaljši poti.
```python
def Hamiltonova_pot(G):
    '''pove ali obstaja Hamiltonova pot v grafu G'''
    #uteži v grafu G nastavimo na 1/0
    pot = naj_pot(G)
    if len(pot) == |G|:
        return True
    return False
```
* Za katere grafe lahko poiščemo?
    * Za usmerjene grafe brez ciklov.
    * Za drevesa (neusmerjen, brez ciklov)


# Viri
/





