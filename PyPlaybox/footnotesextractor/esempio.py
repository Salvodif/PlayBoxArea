import re


def extract_footnotes(input_string):
    # Definiamo un pattern regex per estrarre le chiavi e i valori delle footnote
    pattern = r"footnote(\d+)\)\\t', '(.+?)'"

    # Inizializziamo un dizionario vuoto per memorizzare le coppie chiave-valore
    footnote_dict = {}

    # Troviamo tutte le corrispondenze nel testo
    matches = re.findall(pattern, input_string)

    for match in matches:
        key = match[0]
        value = match[1]

        if "Ivi" in value or "Ibidem" in value:
            continue

        footnote_dict[key] = value

    return footnote_dict


# La tua stringa di input
stringa_footnote = (
    "[['footnote1)\\t', ' Cf. Benedetto XVI, Discorso all’Assemblea Generale della Conferenza Episcopale Italiana, 27 maggio 2010.']], "
    "[['footnote2)\\t', ' Cf. Francesco, Messaggio per la LVII giornata mondiale della pace: Intelligenza artificiale e pace, 1° maggio 2024.']], "
    "[['footnote3)\\t', ' Cf. P. Benanti, Le Macchine sapienti: Intelligenze artificiali e decisioni umane, Marietti 1820, Bologna 2019, 92.']], "
    "[['footnote4)\\t', ' Cf. L. Floridi, La quarta rivoluzione: Come l’infosfera sta trasformando il mondo, Raffaello Cortina, Milano 2017, 99-100.']], "
    "[['footnote5)\\t', ' Cf. Ivi, 101.']], "
    "[['footnote6)\\t', ' B. Mondin, Dizionario Enciclopedico del pensiero di San Tommaso d’Aquino, ESD, Bologna 1991, 74-75.']], "
    "[['footnote7)\\t', ' Cf. E.J. Hobsbawm, La rivoluzione industriale e l’impero. Dal 1750 ai giorni nostri, Piccola Biblioteca Einaudi, Torino 1972, 29.']], "
    "[['footnote8)\\t', ' Cf. Ivi, 28.']], "
    "[['footnote9)\\t', ' Cf. Ivi, 34.']], "
    "[['footnote10)\\t', ' Cf. Ivi, 59.']], "
    "[['footnote11)\\t', ' Cf. Ivi, 54-55.']], "
    "[['footnote12)\\t', ' Cf. Ivi, 69.']], "
    "[['footnote13)\\t', ' Cf. Ivi, 117-119.']], "
    "[['footnote14)\\t', ' Cf. Ivi, 193-194.']], "
    "[['footnote15)\\t', ' Cf. Ivi, 196.']],"
    "[['footnote16)\\t', ' Cf. Ivi, 197.']], "
    "[['footnote17)\\t', ' Cf. Ivi, 234-235.']], "
    "[['footnote18)\\t', ' Cf. Ivi, 238.']], "
    "[['footnote19)\\t', ' Cf. P. Benanti, Le macchine sapienti, 52.']], "
    "[['footnote20)\\t', ' P. Harpe – H. Hegt – A. van Roermund, Smart AD and DA Conversion, Springer Netherlands, Dordrecht 2012, 1.']], "
    "[['footnote21)\\t', ' H. Lala, Storia dell’ingegner Mario Tchou dell’Olivetti, che riuscì a battere sul tempo l’Ibm, Wired Italia, 20 gennaio 2021, in https://www.wired.it/economia/business/2021/01/20/olivetti-mario-tchou-elea-ibm/ (Consultato: 6 aprile 2024)']], "
    "[['footnote22)\\t', ' J. Rifkin, The Third Industrial Revolution: How Lateral Power Is Transforming Energy, the Economy, and the World, St. Martin’s Press 2011, 113.']], "
    "[['footnote23)\\t', ' Cf. J. Abbate, Inventing the Internet, MIT Press, Massachusetts 1999, 140.']], "
    "[['footnote24)\\t', ' Cf. Ivi, 250.']], "
    "[['footnote25)\\t', ' Cf. J. Rifkin, The Third Industrial Revolution, 203.']], "
    "[['footnote26)\\t', ' Cf. Ivi, 135.']]"
)

# Estraiamo le chiavi e i valori
risultato = extract_footnotes(stringa_footnote)

# Stampa il risultato
for key, value in risultato.items():
    print(f"Chiave: {key}\nValore: {value}\n")
