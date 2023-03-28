def verifica(input_string):
    stare_curenta = stare_initiala
    rez=stare_curenta+", "
    for c in input_string:
        if c not in alfabet:
            raise ValueError(f"Caracter invalid: {c}.")
        try:
            stare_curenta = tranzitii[stare_curenta][c]
        except KeyError:
            raise Exception(f"Sir invalid: {input_string}") from None
        rez+=stare_curenta+", "
    return stare_curenta in stari_finale, rez

f=open("inputuri/AFD.txt","r")
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
    rez,str_rez=verifica(s)
    if rez is True:
        print(f"{s} => Acceptat: {str_rez.strip(' ,')}")
    else:
        print(f"{s} => Neacceptat")