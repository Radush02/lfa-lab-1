def verifica(input_string):
    stari_curente = set(stare_initiala)
    rez=stare_initiala[0]+", "
    for c in input_string:
        stari_urm = set()
        if c not in alfabet:
            raise ValueError(f"Caracter invalid: {c}.")
        for stare in stari_curente:
            try:
                if tranzitii[stare][c] != set():
                    stari_urm = stari_urm | tranzitii[stare][c]
            except KeyError:
                pass
        stari_curente=stari_urm
        rez+=str(stari_urm)+", "
    if set(stari_curente) & stari_finale:
        return True, rez
    return False, rez


f=open("inputuri/AFN.txt","r")
alfabet = set([str(x) for x in f.readline().strip().split()])
stari = f.readline().strip().split()
stare_initiala = f.readline().strip().split()
stari_finale = set(f.readline().strip().split())
tranzitii={}
for index,sir in enumerate(f.readlines()):
    string=sir.strip().split(sep=' ')
    tranzitii[stari[index]]={k[:k.find(':')]:set(k[k.find(':')+1:].split(",")) for k in string}


print("Introduceti input")
input_strings=input().strip().split()
for s in input_strings:
    rez,str_rez=verifica(s)
    if rez is True:
        print(f"{s} => Acceptat: {str_rez.strip(' ,')}")
    else:
        print(f"{s} => Neacceptat")