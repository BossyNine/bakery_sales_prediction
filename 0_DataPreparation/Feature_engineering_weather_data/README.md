Script to create some new features based on weather data (from Pauline)
Additionally precipitation data is used from weather statio in Kiel Holtenau
Delete this folder as soon as the script is incorporated into the other folders!
(Ich will nur gerade an den anderen Sachen nichts kaputt machen und steige auch noch nicht ganz durch!)

Edit (Jonna):
Ultra cool, die Ideen und Wege zu den ganzen Variablen!
Notizen, was übernommen oder noch angepasst werden sollte:
- genial mit den Niederschlagsdaten! Die evtl noch mit den Wettercodes kombinieren? (also davon ablesen, was die Codes bedeuten? Und: könnten die Niederschlagsdaten auch die Wettercodes ersetzen, falls diese mal fehlt, aber alle anderen Daten da sind?)
- die Codierung des Datums in Wochentage ist super! (vorher noch darauf achten, dass die Datumsspalte auch sicher im datetime Format ist)
- die Idee mit den averages über mehrere Tage ist super, um Lücken zu füllen.
- und auch, um besonders kalte oder besonders warme Tage rauszufiltern. Da ist einerseits eine 7-Tage average vielleicht gut, aber vielleicht auch länger? Also über 4 Wochen? Oder aber wie doll die Temperatur vom Monatsmittel, oder sogar Jahreszeitenmittel abweicht? Also Jahreszeiten sind auf jeden Fall auch ein gutes KRiterium

Nächste Schritte:
- Recherchieren, ob die Wettercodes einer Niederschlagsmenge entsprechen
- Kategorien ausdenken und ausprobieren, wonach die Wettercodes aufteilen in Klassen
- dann die Regressions Gerade berechnen und mit Kategorien rumprobieren. Und auch den Zusammenhang zwischen den Kategorien/Variablen darstellen? Und die Wichtigkeit der einzelnen Variablen herausfinden.