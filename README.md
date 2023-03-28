# AFD & AFN - Cordunianu Radu 133 

# Rulare AFD
Modificarea AFD-ului se face in fisierul "AFD.txt"

Format fisier:

Alfabet - pe o singura linie separata prin spatii

Stari - pe o singura linie separata prin spatii

Stare initiala 

Stari finale - pe o singura linie separata prin spatii

Tranzitii:

- Pentru fiecare simbol se va concatena starea la care duce prin simbolul ':'
- Pentru fiecare stare se va scrie pe cate o linie simbolurile respectiv starea la care duc
- Exemplu: a:q1 b:q0 c:q0

<h3><b>Executarea programului</b></h3>


Pentru un input dat de la tastatura
```commandline
python3 afd.py
```
Pentru un input dat din fisier (In cazul de mai jos, cu un exemplu atasat in repository)
```commandline
python3 afd.py<inputuri/ex_input_afd.txt
```

# Rulare AFN
Modificarea AFN-ului se face in fisierul "AFN.txt"

Formatul fisierului este acelasi ca la AFD cu o singura diferenta:

Tranzitii:

- Pentru fiecare simbol se pot scrie mai multe stari catre care pot duce, starile fiind separate prin caracterul ','
  - Exemplu: 0:q0,q1 1:q2,q3,q4 2:q1

<h3><b>Executarea programului</b></h3>


Pentru un input dat de la tastatura
```commandline
python3 afn.py
```
Pentru un input dat din fisier
```commandline
python3 afn.py<fisier_intrare.txt
```