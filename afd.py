def verifica(input_string):
    stare_curenta = stare_initiala
    for c in input_string:
        if c not in alfabet:
            raise ValueError(f"Caracter invalid: {c}.")
        stare_curenta = tranzitii[stare_curenta][c]
    return stare_curenta in stari_finale

f=open("AFD.txt","r")
alfabet = f.readline().strip().split()
stari = f.readline().strip().split()
stare_initiala = f.readline().strip()
stari_finale = f.readline().strip().split()
tranzitii={}
for index,sir in enumerate(f.readlines()):
    string=sir.strip().split(sep=' ')
    tranzitii[stari[index]]={k[:k.find(':')]:k[k.find(':')+1:] for k in string}


print("Introduceti input")
input_strings=input().strip().split()
for s in input_strings:
    print(f"{s}: {verifica(s)}")