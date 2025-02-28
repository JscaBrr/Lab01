import random
#verde è nel repository locale ma non su repository github (ancora non sono stati collegati)
#ho fatto delle modifiche nella mia working copy, voglio salvarle nel repository locale -> fare il commit -> si apre la finestra di commit -> file verdi sono nel repository e rossi no -> selezionare file da salvare e commentare

class Domanda:
    def __init__(self, testo, difficolta, rispostacorretta, risposteerrate):
        self.testo = testo
        self.difficolta = difficolta
        self.rispostacorretta = rispostacorretta
        self.risposteerrate = risposteerrate
    def __str__(self):
        return self.testo

    def mescolarisposte(self):
        risposte = [self.rispostacorretta]
        risposte.extend(self.risposteerrate)
        random.shuffle(risposte)
        return risposte

def caricadomande(file_path):
    domande = []
    with open (file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    i = 0
    while i < len(lines):
        if lines[i].strip():
            testo = lines[i].strip()
            difficolta = int(lines[i+1].strip())
            rispostacorretta = lines[i+2].strip()
            risposteerrate = [lines[i+3].strip(), lines[i+4].strip(), lines[i+5].strip()]
            domanda = Domanda(testo, difficolta, rispostacorretta, risposteerrate)
            domande.append(domanda)
            i+=6
        else:
            i+=1
    return domande

class Gioco:
    def __init__(self, domande):
        self.domande = domande
        self.punteggio = 0
        self.livello = 0

    def gioca(self):
        domandecopia = self.domande
        levels = []
        for domanda in domandecopia:
            levels.append(domanda.difficolta)

        for domanda in domandecopia:
            if domanda.difficolta == self.livello:
                domandecopia.remove(domanda)
                print(f"\nLivello {self.livello}) {domanda.testo}")
                risposte = domanda.mescolarisposte()

                for i, j in enumerate(risposte, 1):
                    print(f"\t{i}. {j}")

                rispostautente = input("Inserisci la risposta: ")
                if risposte[int(rispostautente) - 1] == domanda.rispostacorretta:
                    print("Risposta corretta!")
                    self.punteggio += 1
                    self.livello += 1
                    if self.livello == max(levels)+1:
                        print("Hai raggiunto il livello massimo!")
                        break
                else:
                    print(f"Risposta sbagliata! La risposta corretta era: {domanda.rispostacorretta}")
                    break




def salvapunteggio(nickname, punteggio):
    try:
        with open("punti.txt", "a", encoding = 'utf-8') as file:
            file.write(f"{nickname} {punteggio}\n")

        with open("punti.txt", "r", encoding='utf-8') as file:
            linee = file.readlines()
            linee = sorted(linee, key=lambda x: int(x.split()[1]), reverse = True)

        with open("punti.txt", "w", encoding='utf-8') as file:
            file.writelines(linee)

    except Exception as e:
        print(f"Errore nel salvataggio dei punteggi: {e}")

def main():
    domande = caricadomande("domande.txt")
    gioco = Gioco(domande)
    gioco.gioca()
    nickname = input("Inserisci il tuo nickname:")
    salvapunteggio(nickname, gioco.punteggio)

if __name__ == "__main__":
    main()







