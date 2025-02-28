import random
#1-dopo aver eseguito il fork e get from VCS
#verde è nel repository locale ma non su repository github (ancora non sono stati collegati)
#2-ho fatto delle modifiche nella mia working copy, voglio salvarle nel repository locale -> fare il commit -> si apre la finestra di commit -> file verdi sono nel repository e rossi no -> selezionare file da salvare e commentare > repository e working copy sono allineati sulla mia macchina
#blu = file è nel repository locale ma anche nel repository remoto (è collegato il logate al sito github)
#3-trasferire il repository locale sul repository che viene salvato sul sito web > push: stai prendendo il main e lo stai mandando nel main dell'origin == repository github
class Domanda:
    def __init__(self, testo, livello, rispostacorretta, risposteerrate):
        self.testo = testo
        self.livello = livello
        self.rispostacorretta = rispostacorretta
        self.risposteerrate = risposteerrate

domande = []
livelli = []
def creadomande(file_path):
    with open (file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    i = 0
    while i < len(lines):
        t = lines[i].strip()
        l = lines[i+1].strip()
        livelli.append(l)
        rc = lines[i+2].strip()
        re = [lines[i+3].strip(), lines[i+4].strip(), lines[i+5].strip()]
        domanda = Domanda(t,l,rc,re)
        domande.append(domanda)
        i += 7
        if i == len(lines)-1:
            break

creadomande("domande.txt")
duplicadomande = domande.copy()
random.shuffle(duplicadomande)

class Persona:
    def __init__(self, nickname, punteggio):
        self.nickname = nickname
        self.punteggio = punteggio

i = int(min(livelli))
punteggio = 0
while len(duplicadomande) > 0:
    d = random.choice(duplicadomande)
    if int(d.livello) == i:
        print(f"{d.testo}\n" )
        risposte = d.risposteerrate.copy()
        risposte.extend([d.rispostacorretta])
        random.shuffle(risposte)
        for j in risposte:
            print(f"{risposte.index(j)+1}) {j}")
        answer = input("\nInserisci la risposta corretta:")
        if int(answer)-1 == risposte.index(d.rispostacorretta):
            print("Risposta esatta !\n")
            punteggio += 1
            i += 1
            duplicadomande.remove(d)
            if i == int(max(livelli)):
                print("Hai raggiunto il livello massimo")
                break
        else:
            print("Risposta errata !")
            break
    else:
        continue
n = input("Inserisci il nickame:")
p = Persona(n, punteggio)
try:
    with open("punti.txt", "a", encoding='utf-8') as file:
        file.write(f"{p.nickname} {p.punteggio}\n")

    with open("punti.txt", "r", encoding='utf-8') as file:
        linee = file.readlines()
        linee = sorted(linee, key = lambda x: int(x.split()[1]), reverse = True)

    with open("punti.txt", "w", encoding='utf-8') as file:
        file.writelines(linee)
except Exception as e:
    print(f"Errore nel salvataggio dei punteggi: {e}")






