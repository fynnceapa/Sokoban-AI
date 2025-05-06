Stan Andrei Razvan - 333CA

# Tema1 IA - Sokoban

### Fisiere
Tot codul scris de mine se afla in `main.py` si in folderul `search_methods`:
1. beam_search.py - aici am implementat clasa `BeamSearch` impreuna cu metoda `search` care reprezinta algoritmul propriu-zis.
2. lrtastar.py - aici am implementat clasa `LRTAStar` impreuna cu metoda `search`.
3. heuristics.py - aici am toate functiile euristice folosite pentru testarea algoritmilor. 
4. solver.py - include clasa `Solver` alaturi de toate metodele pentru rularea codului si crearea de grafice.

### Cum rulam codul?
Am implementat in main un CLI pentru a putea rula codul in diferite situatii.

Astfel ca, putem rula codul in urmatoarele moduri:
1. Un algoritm specific ruleaza pe toate testele folosind o functie euristica specificata.
2. Un algoritm specific ruleaza pe un singur test folosind toate euristicile.

### Euristici
Primele doua implementate (`euclidian` si `manhattan`) nu sunt mai mult decat niste formule aplicate deci nu voi discuta in detaliu despre ele.

**Functia euristica `Matrix`** practic calculeaza cat de departe sunt cutiile de locurile in care trebuie sa fie asezate.
Face asta folosind o **matrice de costuri** care reprezinta costul (distanta) de la o cutie pana la un target.

    `matrice[i][j] = distanta de la cutia i la target-ul j`

Pentru a calcula distanta am folosit formula de distanta Manhattan pentru functia `matrix1` si distanta Euclidiana pentru `matrix2`

**Functia euristica `minimum_manhattan`** se foloseste de distanta Manhattan dar cauta minimul posibil pentru asta.

### Algoritmi implementati
Am implementat doi algoritmi: `Beam Search` si `LRTA*`.

## 1. Beam Search
Acest algoritm functioneaza bine pentru a gasi o solutie pentru o harta de joc Sokoban deoarece acest joc poate ajunge complicat foarte rapid,
astfel ca un algoritm de cautare clasic (ex. DFS) ar dura foarte mult. 

Beam search foloseste o functie euristica pentru a se ghida pe harta de joc si mereu verifica doar cele mai bune `beam_width` stari (adica cele cu valoarea din functia euristica mai mica).

In implementarea mea am folosit un beam_width de 50, dar am observat ca unele teste pot fi rezolvate si cu un width mai mic, astfel algortmul fiind mai rapid.
Am folosit urmatoarea bucata de cod pentru a optimiza latimea pentru fiecare test.
Am comentat-o insa in codul final.

        width = [2, 5, 10, 20, 50]
        for w in width:
            beam = BeamSearch(self.map, w, 10000, function)
            path, time_taken = beam.search()
            if path:
                return path, time_taken
        return [], float('inf')`

De asemenea, pentru a nu intra in bucle infinite sau a rula prea mult algoritmul, m-am asigurat ca acesta va face doar `max_iter` iteratii.

***
### Performanta cu diferite functii euristice
Pentru grafice voi folosi doua teste dintre cele mai complicate pentru a putea pune in evidenta diferentele dintre euristici mai bine.

![Beam search super_hard_map1 with all heuristic functions](/images/Figure_1.png)

Pe testul `super_hard_map1` din punct de vedere al timpului cele 'naive' dau rezultate valide intr-un timp destul de lung comparativ cu euristicile mai performante.

Se poate observa ca euristicile naive (euclidian si manhattan) produc drumuri mult mai lungi.

O comparatie directa intre euristica euclidiana si cea matrix poate fi vazuta in urmatoarele imagini:

![beam search with euclidian on all maps](/images/Figure_3.png)
![beam search with matrix on all maps](/images/Figure_2.png)

Se poate observa ca euristica euclidiana produce rezultate lungi si intr-un timp mult mai lung decat cea matriceala.
## 2. LRTA*

disclaimer: nu cred ca am cea mai buna implementare pentru acest algoritm dar voi analiza datele pe care le am.

### Performanta cu diferite functii euristice

Performanta pe testul `large_map2`:

![lrtastar with all heuristics on large map 2](/images/Figure_132.png)

Se poate observa ca toate euristicile produc rezultate asemanatoare ca lungime a path-ului gasit dar difera foarte mult din punct de vedere al timpului, cele mai bune fiind euristicile `matrix` si `matrix2`.
***

![lrastar with matrix on all maps](/images/Figure_10.png)

Chiar daca timpul este foarte lung pe hartile mai complicate (ex. super_hard_map1) **rezultatele sunt mult mai bune** chiar si decat **algoritmul Beam Search**, lungimile drumurilor netrecand de 35 nici in cele mai nefavoabile cazuri, folosind o euristica precum `matrix`.

Cu toate ca euristica matrix pe care am implementat-o este una mai performanta in teorie, se pare ca in combinatie cu algortmul LRTA* implementat de mine nu functioneaza atat de optim, desi drumurile oferite sunt corecte.

Din urmatorul grafic se pare ca **euristica simpla euclidiana** intoarce rezultate asemanatoare ca distanta in timpi semnificativ redusi.

![lrtastar with euclidian on all maps](/images/Figure_7.png)

Nu inteleg exact de ce se intampla asta, poate ca nu am cea mai buna implementare pentru LRTA*...

## Comparatie intre cele doua

Dupa cum am stabilit, LRTA* este mai incet in cazul meu, dar produce rezultate mai bune indiferent de euristica folosita comparativ cu Beam Search. Acest lucru se poate observa din urmatorul grafic:

![compare both](/images/Figure_rand.png)


***

### Cum arata o solutie

Am generat gif-uri pentru Beam Search cu euristica matrix is pentru LRTA* cu aceeasi euristica.

**Beam Search**

![gif1](/images/super_hard_map1_matrix_heuristic.gif)

**LRTAStar**

![gif2](/images/super_hard_map1_matrix_heuristic%202.gif)















