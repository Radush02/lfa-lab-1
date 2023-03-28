def verifica(input_string):
    stari_curente = set(stare_initiala)
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
    if set(stari_curente) & stari_finale:
        return True
    return False


f=open("AFN.txt","r")
alfabet = set([str(x) for x in f.readline().strip().split()])
stari = f.readline().strip().split()
stare_initiala = f.readline().strip().split()
stari_finale = set(f.readline().strip().split())
tranzitii={}
for index,sir in enumerate(f.readlines()):
    string=sir.strip().split(sep=' ')
    tranzitii[stari[index]]={k[:k.find(':')]:set(k[k.find(':')+1:].split(",")) for k in string}
print(tranzitii)


input_strings=input().strip().split()
for s in input_strings:
    print(f"{s}: {verifica(s)}")