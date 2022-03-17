# `Poročilo: Računalništvo 2 - Vaje 17. 3. 2022 Floyd Warshall`

**Ime:** Tit Arnšek

**Datum:** 17. 3. 2022


## Vsebina 
* Na tablo smo ponovili Floyd Warshall-ov algoritem
* Naredili smo primer najkraših poti met dvsemi vozlišči s pomočjo zgoraj omenjenega vozlišča


## Komentarji in opombe


# Odgovori na vprašanja

## 1) Kaj računa in kako deluje Floyd Warshallov algoritem? Kakšna je časovna zahtevnost?
Floyd Warshallov algoritem računa dolžino najkrajših povezav med vsemi pari vozlišč v usmerjenem uteženem grafu (lahko so negativne uteži). Pogoj: graf ne sme vsebovati negativnih ciklov. 
* Bellmanova enačba: 

    $Pot_{i,j}(k) = min(Pot_{i,j}(k-1),Pot_{i,k}(k-1)+Pot_{k,j}(k-1)  )$

* Časovna zahtevnost je $O(n^3)$

## 2) Za spodnji graf izračunaj vse najkrajše poti s pomočjo Floyd Warshalovega algoritma:

* Nato dodamo vozlišče 10 in povezavo (5 -> 10) z utežjo -1 in (10 -> 6) z utežjo 2. Kako uporabil prejšnje rezultate, da bi izračunal nove najkrajše poti?

## 3) Na predavanjih ste poleg izračuna matrike D(n) izračunali tudi P(n). Kaj lahko iz njih razberemo? Kako dobimo najkrajšo pot med i in j?
Mesto $P_{i,j}$ v matriki $P(n)$ nam poda zadnje vozlišče v najkrajši poti med vozliščema $i$ in $j$.
Algoritem:
```python
def min_pot(i,j):
    '''
    Vrne najkrajšo pot med vozliščema i in j
    '''
    sez = []
    zacetek = i
    konec = j
    while zacectek != konec:
        sez.append(konec)
        konec = P[i][j]
    sez.append(konec)
    return sez[::-1]
```

## 4) Ali imamo v omrežju lahko več najkrajših poti med dvema vozliščema? Kaj FW naredi v tem primeru? Konstruiraj graf, ki ima ogromno najkrajših poti. Bi lahko preštel vse take poti?
Da, lahko imamo več najkrajših poti med dvema vozliščema. V tem primeru se FW ne spremeni. Vrne še vedno pravilno rešitev. Če pa želimo potem skonstuirati najkrajšo pot, pa bomo v matriki $P(n)$ dobili vozlišča odvisna od implementacije. (Odvisno kako smo definirali primer, ko smo do vozlišča v $k$-tem koraku prišli enako hitro, če smo šli preko vozlišča $k$ ali pa brez njega)
## 5) Kako bi s FW algoritmom odkrili, če v grafu obstajajo negativni cikli? Kaj vrne FW, če graf vsebuje negativen cikel?
V matriki, bi se na diagonali pojavilo negativno število. V tem primeru bi FW vrnil neko rešitev, vendar ne bi bile vse vrednosti pravilne! 

## 6) Uteži sedaj dodamo še na vozlišča. Kako bi sedaj poiskal vse najkrajše poti?

Problem bi preoblikoval v problem, ki ga znamo rešiti. To bi storil tako, da vsem povezavam, ki kažejo na vozlišče povečal utež za utež, ki je na vozlišču. Nato bi na novem omrežju izvedel FW algoritem.



-----


Slika semaforja:

![Semafor iz Tomota](semafor4.png)

# Kviz
Kviza na teh vajah ni bilo

# Viri

1. Projekt Tomo, [https://www.projekt-tomo.si/](https://www.projekt-tomo.si/), 12. 3. 2022





