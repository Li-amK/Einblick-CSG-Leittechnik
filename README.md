# Einblick-CSG-Leittechnik

In diesem Repository befindet sich ein kleiner Einblick in mein bisher größtes Projekt: die CSG Leittechnik.

Um es zum Laufen zu bringen, MongoDB starten (muss leider (noch) lokal installiert werden), die Datenbank importieren und anschließend die API.py und die Node.js Applikation starten.

Der Benutzername und das Passwort sind nach Import der leittechnik.users.json Datei in eine MongoDB namens leittechnik in der Tabelle users zweimal 'liam'.

Ergebnisse lassen sich durch die print() und console.log() Befehle beobachten, es sei den Sie haben, die Möglichkeit sich mit einem Siemens KNX Bus zu verbinden.

P.S.: Ich verwende Node.js Version 20.10.0 LTS und Python 3.12

## Info:
Dieses Repo habe ich folgendermaßen getestet: als gesamtes geklont und in Visual Studio Code (aus dem Backend Ordner) eine virtuelle Umgebung mit der requirements.txt erstellt und dann (aus dem Frontend Ordner) 'npm install' und 'node .' ausgeführt.
