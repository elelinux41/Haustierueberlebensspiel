# -*- coding: utf-8 -*-
import random
class Tier():
    def __init__(self,name,zeitraum):
        self.name = name.title()
        self.zeitraum = zeitraum
        self.zeitseitfüttern = 2
        self.tierarzt = 0
        self.lebt = True
        self.todesursache = ''
        self.zeit = 0
        self.geld = self.zeitraum
        self.futteranzahl = 0
        self.zeitseitaktion = 2
    def warten(self):
        länge = input('Wie lange willst du in Stunden warten: ')
        try:
            länge = int(länge)
        except ValueError:
            return
        else:
            if länge < 0:
                print('Du kannst nicht in die Zeit zurückreisen.')
            else:
                länge = round(länge,0)
                self.zeit += länge
                self.zeitseitfüttern += länge
                self.zeitseitaktion += länge
    def füttern(self):
        if self.futteranzahl >= 1:
            print('Dein Tier wurde gefüttert')
            if self.zeitseitfüttern <= 1:
                self.tierarzt1('überfressen')
            self.zeitseitfüttern = 0
            self.futteranzahl -= 1
        else:
            print('Dein Tier kann nicht gefüttert werden, da du kein Futter hast.')
    def kaufen(self):
        futter_anzahl = input('Wie viel Futter willst du kaufen: ')
        try:
            futter_anzahl = int(futter_anzahl)
        except ValueError:
            return
        else:
            if self.geld > (futter_anzahl * 15):
                round(futter_anzahl,0)
                if futter_anzahl > 7:
                    prüfen0 = input('Willst du wirklich ' + str(futter_anzahl) + ' Portionen Futter kaufen(j/n): ')
                    prüfen0 = prüfen0.lower()
                    prüfen0 = prüfen0.strip()
                if futter_anzahl <= 7 or prüfen0 == 'j' or prüfen0 == 'ja':
                    self.futteranzahl += futter_anzahl
                    self.geld -= 15 * futter_anzahl
                    self.zeit += 1
                    self.zeitseitfüttern += 1
                    self.zeitseitaktion += 1
                    print('Du hast für ' + self.name, str(futter_anzahl) + ' Portionen Futter gekauft.')
            else:
                print('Du hast nich genug Geld, um dir das Futter zu kaufen')
    def tierarzt1(self, grund):
        if grund == 'erkrankt':
            erkrankungen = ['Diabetis','Schnupfen','Borelliose','Tumor']
            grund = random.choice(erkrankungen)
        if grund == 'verhungert' and self.zeitseitfüttern > 72:
            self.lebt = False
            self.todesursache = 'verhungert'
            self.zeit = self.zeit - (self.zeitseitfüttern - 72)
        elif self.tierarzt >= 3:
            self.lebt = False
            self.todesursache = grund
            if grund == 'verhungert':
                self.zeit = self.zeit - (self.zeitseitfüttern - 36)
        elif self.tierarzt < 3:
            if self.geld >= 50:
                if grund == 'verhungert':
                    print(self.name + ' ist am verhungern und muss zum Tierarzt gebracht werden, das dauert 2h.')
                elif grund == 'überfressen':
                    print(self.name + ' hat sich überfressen und muss zum Tierarzt gebracht werden, das dauert 2h.')
                else:
                    if grund == 'Tumor':
                        print(self.name + ' ist an einem Tumor erkrankt und muss zum Tierarzt gebracht werden, das dauert 2h.')
                    else:
                        print(self.name + ' ist an ' + grund + ' erkrankt und muss zum Tierarzt gebracht werden, das dauert 2h.')
                self.zeit += 2
                self.zeitseitfüttern = 0
                self.zeitseitaktion += 2
                self.tierarzt += 1
                self.geld -= 45
            else:
                self.lebt = False
                self.todesursache = grund
                print('Du hast kein Geld um zum Tierarzt zu gehen, ' + self.name + ' stirbt.')

class TierHund(Tier):
    def __init__(self,name,zeitraum):
        super().__init__(name, zeitraum)
        self.art = 'Hund'
        self.geräusch = 'Wau '
        self.zeitseitgassi = 0
    def aktion(self):
        self.zeit += 1
        self.zeitseitaktion = 0
        self.zeitseitfüttern += 1
        print('Du bist mit ' + self.name + ' eine Stunde Gassi gegangen.')
    def keineaktion(self):
        self.lebt = False
        self.todesursache = 'von Auto überfahren'
        self.tot()
        print( self.name + ' ist dir ausgerissen, weil du nich mit ihm Gassi gegangen bist, dann wurde er von einem Auto überfahren.')
    def tot(self):
        print('In deinem Ort ist scheinbar der Hund verreckt.')
    def regeln(self):
        print('''Folgende Regeln gelten:
-alle 36h muss ihr Hund gefüttert werden, sonst muss er zum Tierarzt
-ihr Hund stirbt, wenn sie 72h nicht gefüttert wurde
-wenn ihr Hund zwei mal in einer Stunde gefüttert wird, muss er zum Tierarzt, weil er sich überfressen hat
-wenn ''' + self.name + ''' über drei mal beim Tierarzt war, stirbt er/sie.
-eine Portion Hundefutter kostet 15€
-ein Tierarztbesuch kostet 45€
-du musst alle zwei Tage mit deinem Hund Gassi gehen
-dein Hund kann auch krank werden''')

class TierKatze(Tier):
    def __init__(self,name,zeitraum):
        super().__init__(name, zeitraum)
        self.art = 'Katze'
        self.geräusch = 'Miau '
    def aktion(self):
        self.zeit += 1
        self.zeitseitaktion = 0
        self.zeitseitfüttern += 1
        print('Du hast ' + self.name + ' eine Stunde lang gestreichelt.')
    def keineaktion(self):
        self.lebt = False
        self.todesursache = 'von Auto überfahren'
        self.tot()
        print( self.name + ' ist dir ausgerissen, weil du sie/ihn nicht gestreichelt hast, dann wurde er/sie von einem Auto überfahren.')
    def tot(self):
        print('Deine Katze ist tot.')
    def regeln(self):        
        print('''Folgende Regeln gelten:
-alle 36h muss ihre Katze gefüttert werden, sonst muss sie zum Tierarzt
-deine Katze stirbt, wenn sie 72h nicht gefüttert wurde
-wenn deine Katze zwei mal in einer Stunde gefüttert wird, muss sie zum Tierarzt, weil sie sich überfressen hat
-wenn deine Katze über drei mal beim Tierarzt war, stirbt sie
-du musst alle zwei Tage ''' + self.name + ''' streicheln
-eine Portion Katzenfutter kostet 15€
-ein Tierarztbesuch kostet 45€
-deine Katze kann auch krank werden''')

class TierFisch(Tier):
    def __init__(self,name,zeitraum):
        super().__init__(name, zeitraum)
        self.art = 'Fisch'
        self.geräusch = 'Blub '
    def aktion(self):
        self.zeit += 1
        self.zeitseitaktion = 0
        self.zeitseitfüttern += 1
        print('Du hast das Wasser deines Aquariums gewechselt.')
    def keineaktion(self):
        self.lebt = False
        self.todesursache = 'erstickt'
        self.tot()
        print('Da du in deinem Aquarium nicht das Wasser gewechselt hast, sind deine Fische erstickt.')
    def tot(self):
        print('Seltsam, deine Fische schwimmen mit dem Bauch an der Wasseroberfläche.')
    def tierarzt1(self, grund):
        if grund == 'erkrankt':
            erkrankungen = ['Kiemenfäule','Flossenfäule','Schnupfen','Würmer']
            grund = random.choice(erkrankungen)
        if grund == 'verhungert' and self.zeitseitfüttern > 72:
            self.lebt = False
            self.todesursache = 'verhungert'
            self.zeit = self.zeit - (self.zeitseitfüttern - 72)
        elif self.tierarzt >= 3:
            self.lebt = False
            self.todesursache = grund
            if grund == 'verhungert':
                self.zeit = self.zeit - (self.zeitseitfüttern - 36)
        elif self.tierarzt < 3:
            if grund == 'verhungert':
                print('Deine Fische sind am verhungern du solltest ihnen schnellstens etwas zum essen geben.')
            if grund == 'überfressen':
                print('Deine Fische haben sich überfressen, einige sind gestorben.')
            else:
                if grund == 'Würmer':
                    print('Fische wurden von Würmern befallen, einige davon sind gestorben.')
                else:
                    print('In deinem Aquarium ist die Krankheit ' + grund + ' ausgebrochen, einige Fische sind gestorben.')
            self.tierarzt += 1
    def regeln(self):
        print('''Folgende Regeln gelten:
-alle 36h müssen deine Fische gefüttert werden, sonst sterben einige
-alle Fische sterben, wenn sie 72h nicht gefüttert wurde
-wenn deine Fische zwei mal in einer Stunde gefüttert werden, sterben einige, weil sie sich überfressen haben
-wenn drei mal einige Fische gestorben sind sind ale Fische tot
-eine Portion Katzenfutter kostet 15€
-du musst alle zwei Tage das Aquariumwasser wechseln
-deine Fische können auch krank werden''')

def modus1():
    global tier
    print()
    modus = input('Welche Spielmethode willst du nutzen, Standard(s), Zufällig(z) oder Benutzerdefiniert(b): ')
    modus = modus.lower()
    modus = modus.strip()
    if modus == 's' or modus == 'standard':
        datei = open('name.txt','r')
        name3 = datei.read()
        datei.close()
        datei = open('zeit.txt','r')
        zeit3 = datei.read()
        zeit3 = int(zeit3)
        datei.close()
        datei = open('tier.txt','r')
        tier3 = datei.read()
        datei.close()
        if tier3 == 'h':
            tier = TierHund(name3,zeit3)
        if tier3 == 'k':
            tier = TierKatze(name3,zeit3)
        if tier3 == 'f':
            tier = TierFisch(name3,zeit3)
    elif modus == 'z' or modus == 'zufällig' or modus == 'zufall':
        hundename = ['Happo','Keks','Charly','Brutus','Lassie','Goethe','Gildo']
        katzenname = ['Kitty','Menu','Jacqueline','Uschi','Schnitzel','Alf']
        fischname = ['Nemo','Sharky','Sir Charles','Blubb','Gräte','Doktor Einstein']
        zufallszahl0 = random.randint(1,3)
        zufallszahl1 = random.randint(3,21)
        zufallszahl1 *= 24
        if zufallszahl0 == 1:
            tier = TierHund(random.choice(hundename),zufallszahl1)
        if zufallszahl0 == 2:
            tier = TierKatze(random.choice(katzenname),zufallszahl1)
        if zufallszahl0 == 3:
            tier = TierFisch(random.choice(fischname),zufallszahl1)
    elif modus == 'b' or modus == 'benutzerdifiniert':
        def name7():
            global name2
            name2 = input('Wie heißt dein Tier: ')
            name2 = name2.title()
            name2 = name2.strip()
            if name2 == '':
                print('Du hast nichts eigegeben.')
                name7()
        def zeitraum1():
            global zeitraum
            zeitraum = input('Wie lange willst du das Tier in Tagen betreuen: ')
            try:
                zeitraum = int(zeitraum)
            except ValueError:
                print('Bitte gebe eine Zahl ein!')
                zeitraum1()
            else:
                zeitraum = round(zeitraum,0)
                if zeitraum < 1:
                    print('Du musst dein Tier mindestens 1 Tag betreuen.')
                    zeitraum1()
                zeitraum *= 24
        def tier1():
            global tier
            tier0 = input('Bitte wähle ein Tier, willst du dich um einen Hund(h), eine Katze(k) oder Fische(f) kümmern: ')
            tier0 = tier0.lower()
            if tier0 == 'h' or tier0 == 'hund':
                tier = TierHund(name2,zeitraum)
            elif tier0 == 'k' or tier0 == 'katze':
                tier = TierKatze(name2,zeitraum)
            elif tier0 == 'f' or tier0 == 'fisch' or tier0 == 'fische':
                tier = TierFisch(name2,zeitraum)
            else:
                print('Dieser Wert ist nicht verfübar.')
                tier1()
        name7()
        zeitraum1()
        tier1()
    elif modus == 'h' or modus == 'hilfe':
        print('''Sie können eingeben:
-standard(s)            Es werden die Standardeinstellungen für dieses Spiel verwendet
-benutzerdifiniert(b)   Du kannst entscheiden, wie dein Tier heißen soll, wie lange du spielen willst und was du für ein Tier haben willst
-einstellungen(e)       Du kannst die Standardeinstellungen verändern
-aus(a)                 Das Spiel wird abgebrochen
-handbuch(t)            Dir wird das Handbuch angezeigt
-hilfe(h)               Alle auführbaren Befehle werden angezeigt''')
        modus1()
    elif modus == 'a' or modus == 'aus':
        print('Schade, dass du gehst, vieleich hättest du gewonnen.')
        input()
        exit()
    elif modus == 'e' or modus == 'einstellungen':
        def änderung0():
            print()
            änderung = input('Wechen Standartwert willst du ändern, den Namen(n) deines Tieres, den Zeitraum(z) oder die Tierart(t), sie können jederzeit mit aus(a) abbrechen oder sie setzen das Spiel mit Werkseinstellung(w) zurück: ')
            änderung = änderung.lower()
            änderung = änderung.strip()
            if änderung == 'aus' or änderung == 'a':
                print('Schade, dass du gehst, vieleich hättest du gewonnen.')
                print()
                exit()
            elif änderung == 'werkseinstellung' or änderung == 'w':
                datei = open('name.txt','w')
                datei.write('Happo')
                datei.close()
                datei = open('zeit.txt','w')
                datei.write('186')
                datei.close()
                datei = open('tier.txt','w')
                datei.write('h')
                datei.close()
                datei = open('zeit.txt','w')
                datei.write('186')
                datei.close()
                datei = open('strt.txt','w')
                datei.write('1')
                datei.close()
                modus1()
            elif änderung == 'name' or änderung == 'n':
                def änderung7():
                    name4 = input('Wie soll dein neuer Standardname für dein Tier heißen: ')
                    name4 = name4.title()
                    name4 = name4.strip()
                    if name4 == '':
                        print('Du kannst nicht keinen Namen vergeben, mit "aus" beendest du.')
                        änderung7()
                    elif name4 == 'aus' or name4 == 'a':
                        input()
                        exit()
                    else:
                        datei = open('name.txt','w')
                        datei.write(name4)
                        datei.close()
                änderung7()
                modus1()
            elif änderung == 'zeit' or änderung == 'zeitraum' or änderung == 'z':
                def änderung8():
                    zeit4 = input('Wie lange willst du künftig standardmäßig in Tagen spielen: ')
                    zeit4 = zeit4.strip()
                    if zeit4 == 'aus' or zeit4 == 'a':
                        input()
                        exit()
                    try:
                        zeit4 = int(zeit4)
                    except ValueError:
                        print('Du musst eine Zahl eingeben, du kannst mit "aus beenden"')
                        änderung8()
                    else:
                        round(zeit4,0)
                        zeit4 = zeit4 * 24
                        datei = open('zeit.txt','w')
                        datei.write(str(zeit4))
                        datei.close()
                änderung8()
                modus1()
            elif änderung == 'tier' or änderung == 't':
                def änderung9():
                    def speichern0():
                        nonlocal tier4
                        datei = open('tier.txt','w')
                        datei.write(tier4)
                        datei.close()
                    tier4 = input('Soll dein Standardtier ein Hund(h), eine Katze(k) oder ein Fisch(f) sein: ')
                    tier4 = tier4.lower()
                    tier4 = tier4.strip()
                    if tier4 == 'aus' or tier4 == 'a':
                        input()
                        exit()
                    elif tier4 == 'hund' or tier4 == 'h':
                        tier4 = 'h'
                        speichern0()
                    elif tier4 == 'katze' or tier4 == 'k':
                        tier4 = 'k'
                        speichern0()
                    elif tier4 == 'fisch' or tier4 == 'fische' or tier4 == 'f':
                        tier4 = 'f'
                        speichern0()
                    else:
                        print('Dieser Befehl existiert nicht, sie können mit "aus" beenden.')
                        änderung9()
                änderung9()
                modus1()
            else:
                print('Du kannst nur die oben genannten Werte eingeben')
                änderung0()
        änderung0()
    elif modus == 't' or modus == 'handbuch':
        print()
        print('----------------------------------------------------------------------------------------------------------')
        print()
        datei = open('buch.txt','r')
        print(datei.read())
        datei.close()
        print()
        print('----------------------------------------------------------------------------------------------------------')
        modus1()
    else:
        print('Dieser Wert ist nich verfügbar, geben sie "s" ein um ein Standardspiel zu spielen oder "b" für ein benutzerdefiniertes Spiel.')
        modus1()

datei = open('strt.txt','r')
if datei.read() == '1':
    datei.close()
    print('Das Handbuch zum Spiel:')
    print()
    print('----------------------------------------------------------------------------------------------------------')
    print()
    datei = open('buch.txt','r')
    print(datei.read())
    datei.close()
    print()
    print('----------------------------------------------------------------------------------------------------------')
    datei = open('strt.txt','w')
    datei.write('0')
    datei.close()
modus1()
print()
if tier.art == 'Hund' or tier.art == 'Fisch':
    print('In diesem Spiel musst du dich ' + str(tier.zeitraum // 24) + ' Tage lang um den ' + tier.art, tier.name + ' deiner Nachbarn kümmern.')
if tier.art == 'Katze':
    print('In diesem Spiel musst du dich ' + str(tier.zeitraum // 24) + ' Tage lang um die Katze ' + tier.name + ' deiner Nachbarn kümmern.')
print('Sie können alle Befehle die sie eingeben können über "Hilfe" abrufen, die Spielregeln finden sie unter "Regeln".')
spiel_aktiv = True
befehl = 'x'
while spiel_aktiv:
    if befehl != '':
        print()
    befehl = input('> ')
    befehl = befehl.lower()
    befehl = befehl.strip()
    if befehl == 'aus':
        spiel_verlassen = input('Willst du wirklich das Spiel verlassen(j/n): ')
        spiel_verlassen = spiel_verlassen.lower()
        spiel_verlassen = spiel_verlassen.strip()
        if spiel_verlassen == 'j' or spiel_verlassen == 'ja':
            print('Schade, dass du gehst, vielleicht hättest du gewonnen.')
            input()
            exit()
    elif befehl == 'hilfe':
        print('''Du kannst folgende Befehle eigeben:
-aus                Spiel wird beendet
-hilfe              Es werden alle Befehle angezeigt
-regeln             Es werden die Spielregeln angezeigt
-füttern            Du fütterst dein Tier
-warten             Du lässt die Zeit vergehen
-zeit               Die vergangene und verbleibende Zeit wird abgerufen
-geld               Kontostand sehen
-kaufen             Futter kaufen
-portionen          Futterportionen anzeigen
-sprich             Tier macht geräusche
-zeit seit füttern  Die vergange Zeit seit der letzten Fütterrung wird ausgegeben
-leben              Tierarztbesuche Anzeigen beziehungsweise anzeigen wie viele Fische gestorben sind''')
        if tier.art == 'Hund':
            print('-gassi              Hund wird Gassi geführt')
            print('-zeit seit gassi    Vergangene Zeit seit dem letzen Gassi gehen wird ausgegeben')
        if tier.art == 'Katze':
            print('-streicheln         Katze wird gestreichelt')
            print('-zeit seit streicheln: Vergangene Zeit seit dem letzen streicheln wird ausgegeben')
        if tier.art == 'Fisch':
            print('-wasser wechseln    Aquriumwasser wird gewechselt')
            print('-zeit seit wasser wechseln: Vergangene Zeit seit dem letzen Mal Wasser wechseln wird abgerufen')
    elif befehl == 'füttern':
        tier.füttern()
    elif befehl == 'regeln':
        tier.regeln()
    elif befehl == 'warten':
        tier.warten()
    elif befehl == 'zeit':
        print('Vergangene Zeit: ' + str(tier.zeit // 24) + 'd und ' + str(tier.zeit % 24) + 'h')
        print('Verbleibende Zeit: ' + str((tier.zeitraum - tier.zeit) // 24) + 'd und ' + str((tier.zeitraum - tier.zeit) % 24) + 'h')
    elif befehl == 'geld':
        print('Verbleibendes Geld: ' + str(tier.geld) + '€')
        print('Ausgegebenes Geld: ' + str(tier.zeitraum - tier.geld) + '€')
    elif befehl == 'kaufen':
        tier.kaufen()
    elif befehl == 'portionen':
        print('Deine Futterportionen: ' + str(tier.futteranzahl))
    elif befehl == 'sprich':
        print(3 * tier.geräusch)
    elif befehl == 'zeit seit füttern':
        print('Letzte Fütterung: vor ' + str(tier.zeitseitfüttern) + 'h')
    elif befehl == 'leben':
        if tier.art != 'Fisch':
            print('Du warst schon ' + str(tier.tierarzt) + ' Mal beim Tierarzt.')
        else:
            print('Es dürfen nur noch ' + str(3 - tier.tierarzt) + ' Mal einige Fische sterben.')
    elif befehl == 'gassi' or befehl == 'streicheln' or befehl == 'wasser wechseln':
        if (befehl == 'gassi' and tier.art == 'Hund') or \
            (befehl == 'streicheln' and tier.art == 'Katze') or \
            (befehl == 'wasser wechseln' and tier.art == 'Fisch'):
                tier.aktion()
        else:
            print('Dieser Befehl existiert nicht')
    elif befehl == 'zeit seit gassi' or befehl == 'zeit seit streicheln' or befehl == 'zeit seit wasser wechseln':
        if befehl == 'zeit seit gassi' and tier.art == 'Hund':
            print('Letzes mal Gassi gehen: vor ' + str(tier.zeitseitaktion) + 'h')
        elif befehl == 'zeit seit streicheln' and tier.art == 'Katze':
            print('Letzes mal Katze streicheln: vor ' + str(tier.zeitseitaktion) + 'h')
        elif befehl == 'zeit seit wasser wechseln' and tier.art == 'Fisch':
            print('Letzes mal Aquariumwasser gewechselt: vor ' + str(tier.zeitseitaktion) + 'h')
        else:
            print('Dieser Befehl existiert nicht')
    elif befehl == '':
        befehl = ''
    else:
        print('Dieser Befehl existiert nicht')
    if befehl == 'kaufen' or \
        befehl == 'warten' or \
        befehl == 'füttern' or \
        befehl == 'sprich' or \
        (befehl == 'gassi' and tier.art == 'Hund') or \
        (befehl == 'streicheln' and tier.art == 'Katze') or \
        (befehl == 'wasser wechseln' and tier.art == 'Fisch'):
            if tier.zeitseitfüttern > 36:
                tier.tierarzt1('verhungert')
            elif tier.zeitseitaktion > 48:
                tier.keineaktion()
            elif random.randint(1,700) == 1:
                tier.lebt = False
                tier.todesursache = 'altersschwäche'
                tier.tot()
                print( tier.name + ' ist an Alterschwäche gestorben.')
            elif random.randint(1,60) == 1 and tier.lebt == True:
                tier.tierarzt1('erkrankt')
            if tier.lebt == False:
                print()
                tier.tot()
                print('Du hast verloren, ' + tier.name + ' ist bei dir gestorben und deine Nachbarn schauen dich seltsamer weise, wenn du ihnen über den Weg läufst, immer grimmig an.')
                print('Todesursache: ' + tier.todesursache)
                print('Lebende Zeit des Tieres: ' + str(tier.zeit // 24) + 'd und ' + str(tier.zeit % 24) + 'h.')
                spiel_aktiv = False
            if tier.zeit >= tier.zeitraum and tier.lebt == True:
                spiel_aktiv = False
                print('Du hast gewonnen, ' + tier.name + ' hat bei dir überlebt und deine Nachbarn sind glücklich.')
                print('Zeit: ' + str(tier.zeitraum / 24) + 'd')
input()
exit()
