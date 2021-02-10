---------------DATI.TXT-------------------------------------------------------------------------------------------------------------------------------------------------------
Modena
-Mantova,50Km
-Bologna,60Km
Reggio Emilia
-Modena,20Km
Milano
-Parma,100Km
-Verona,70Km
-Bari,80Km
---------------
Modena: [{Mantova: 50}, {Parma: 60}], Mantova: [{Bologna: 40}]
---------------
with open('dati.txt') as f:
    f = f.readlines()

citta = {}
for l in f:
    l = l.strip()
    if len(l) > 0:
        if '-' not in l:
            key = l
            citta[key] = []

        else:
            s = l.replace('-', '')
            x = l.replace('Km', '')
            dest = {}
            dest['Destinazione'] = s.split(',')[0]
            dest['Km'] = x.split(',')[1]
            citta[key].append(dest)
for key, value in citta.items():
    print(key, value)   
    
    
    
---------------DATI.TXT-------------------------------------------------------------------------------------------------------------------------------------------------------
Juve-Milan
3-2
Higuain,Dybala,Higuain-Niang,Niang

Napoli-Roma
1-2
Insigne-Totti,Totti

Milan-Juve
1-1
Niang,Higuain
---------------
{'Juve-Milan': [{'Gol': '3-2'}, {'Giocatori': ['Higuain,Dybala,Higuain', 'Niang,Niang']}]}
---------------
with open('dati.txt') as f:
    l = f.read().splitlines()

for i in range(int(len(l))):
    if '' in l:
        for x in l:
            if len(x) == 0:
                l.remove(x)

partita = []
for i in range (0, len(l), 3):
    p1 = {
        l[i]:[{'Gol': l[i+1]}, {'Giocatori': l[i+2].split('-')}]
    }
    partita.append(p1)
for d in partita:
    print(d)
    
    
    
---------------DATI.TXT-------------------------------------------------------------------------------------------------------------------------------------------------------
Torta di Mele
-Mele,4
-Zucchero,5
-Farina,6
-Uova,2

Spaghetti in Bianco
-Spaghetti,100

Pasta
-Sale,2
-Acqua,1000
---------------
Torta di mele: [{mele:4}, {uova,6}]
---------------
with open('dati.txt') as f:
    f = f.readlines()

ricetta = {}
for l in f:
    l = l.strip()
    if len(l) > 0:
        if '-' not in l:
            key = l
            ricetta[key] = []

        else:
            s = l.replace('-', '')
            ingr = {}
            ingr['Ingrediente'] = s.split(',')[0]
            ingr['Quantita'] = s.split(',')[1]
            ricetta[key].append(ingr)

for key, value in ricetta.items():
    print(key, value)



---------------DATI.TXT-------------------------------------------------------------------------------------------------------------------------------------------------------
Via Emilia-->Via Amendola
Via Amendola-->Via Botti
Via Amendola-->Via Grande
Via Emilia-->Via Castello
---------------
1) {'Via Emilia': 'Via Amendola'}
2) ['Via Emilia', 'Via Amendola'] 
---------------
1)
with open('dati.txt') as f:
    f = f.readlines()
    for l in f:
        vie = {}
        l = l.strip()
        if len(l) > 0:
            k = l.split('-->')[0]
            v = l.split('-->')[1]
            vie[k] = v
        print(vie)
2)
vie = []

with open('dati.txt', encoding='utf-8') as f:
    for l in f:
        l = l.strip()
        if len(l) > 0:
            s = l.split('-->')
            vie.append(s)
for s in vie:
    print(s)



---------------DATI.TXT-------------------------------------------------------------------------------------------------------------------------------------------------------
A,1,2,3

A,4,5,6
B,1,4
A,7,8,9

B,2,3
C,3,3,4
---------------
{'A': [[1, 2, 3], [4, 5, 6], [7, 8, 9]], ...
---------------
matrici = {}
with open('dati.txt', encoding='utf-8') as f:
    for l in f:
        l = l.strip()
        if len(l) > 0:
            s = l.split(',')
            r = [int(s[i]) for i in range(1, len(s))]
            if s[0] in matrici:
                matrici[s[0]].append(r)
            else:
                matrici[s[0]] = [r]
print(matrici)



---------------DATI.TXT-------------------------------------------------------------------------------------------------------------------------------------------------------
Nome:A
Valori:1,2,3,4,5
Nome:A
Valori:1,1,3
Nome:B

Valori:2,2
---------------
{'A': [[1, 2, 3, 4, 5], [1, 1, 3]], 'B':[[2, 2]]}
---------------
dati = {}
with open('dati.txt') as f:
    for l in f:
        l = l.strip()
        if len(l) > 0:
            #print(l)
            if l.startswith('Nome'):
                gruppo = l.split(':')[1]
            else:
                v = [int(x) for x in l.split(':')[1].split(',')]
                if gruppo in dati:
                    dati[gruppo].append(v)
                else:
                    dati[gruppo] = [v]
print(dati)



---------------DATI.TXT-------------------------------------------------------------------------------------------------------------------------------------------------------
Data:11-07-2015 Da:Marco A:Franco Testo:come va?
Data:11-07-2015 Da:Franco A:Marco Testo:Ciao!
---------------
{'data': '11-07-2015', 'da': 'Marco', 'a': 'Franco', 'testo': 'come va?'}
---------------
def parse(l):
    s = l.strip().split(' ')
    data = s[0]
    da = s[1]
    a = s[2]
    testo = s[3]
    for i in range(4, len(s)):
        testo += ' '+s[i]
    return {'data':data.split(':')[1], 'da':da.split(':')[1], 'a':a.split(':')[1], 'testo':testo.split(':')[1]}

with open('messaggio.txt') as f:
    msg = [parse(l) for l in f if len(l.strip()) > 0]

for m in msg:
    print(m)



---------------DATI.TXT-------------------------------------------------------------------------------------------------------------------------------------------------------
1:1,2,3,4,5
2:3,4,5
3:2,3,4

A:2,3
B:1
---------------
{'A': ['3', '4', '5']}
{'A': ['2', '3', '4']}
{'B': ['1', '2', '3', '4', '5']}
---------------
with open('dati.txt') as f:
    d1 = {}
    d2 = {}
    for l in f:
        l = l.strip().splitlines()
        if len(l) > 0:
            for elem in l:
                if elem.split(':')[0].isalpha():
                    k1 = elem.split(':')[0]
                    v1 = elem.split(':')[1].split(',')
                    d1[k1] = v1
                else:
                    k2 = elem.split(':')[0]
                    v2 = elem.split(':')[1].split(',')
                    d2[k2] = v2

    for k1, v1 in d1.items():
        d3 = {}
        for e in v1:
            for k2, v2 in d2.items():
                if e == k2:
                    d3[k1] = v2
            print(d3)


---------------DATI.TXT-------------------------------------------------------------------------------------------------------------------------------------------------------

---------------

---------------



